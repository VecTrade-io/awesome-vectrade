"""Tests for awesome-vectrade list validation."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
README_FILE = ROOT / "README.md"
CONTRIBUTING_FILE = ROOT / "CONTRIBUTING.md"
LICENSE_FILE = ROOT / "LICENSE"


@pytest.fixture
def readme_content():
    """Load README content."""
    return README_FILE.read_text()


@pytest.fixture
def readme_lines(readme_content):
    """Split README into lines."""
    return readme_content.splitlines()


@pytest.fixture
def contributing_content():
    """Load CONTRIBUTING content."""
    return CONTRIBUTING_FILE.read_text()


# ============================================================
# File existence tests
# ============================================================


class TestFilesExist:
    """Verify required files exist."""

    def test_readme_exists(self):
        assert README_FILE.is_file()

    def test_contributing_exists(self):
        assert CONTRIBUTING_FILE.is_file()

    def test_license_exists(self):
        assert LICENSE_FILE.is_file()

    def test_readme_not_empty(self, readme_content):
        assert len(readme_content.strip()) > 100

    def test_contributing_not_empty(self, contributing_content):
        assert len(contributing_content.strip()) > 100


# ============================================================
# README structure tests
# ============================================================


class TestReadmeStructure:
    """Verify README follows awesome-list conventions."""

    def test_has_h1_title(self, readme_content):
        assert re.search(r"^# Awesome VecTrade", readme_content, re.MULTILINE)

    def test_has_awesome_badge(self, readme_content):
        assert "awesome.re/badge" in readme_content

    def test_has_ci_badge(self, readme_content):
        assert "actions/workflows/ci.yml/badge.svg" in readme_content

    def test_has_license_badge(self, readme_content):
        assert "License" in readme_content and "badge" in readme_content.lower()

    def test_has_description(self, readme_content):
        # Should have a > blockquote description
        assert re.search(r"^>", readme_content, re.MULTILINE)

    def test_has_contents_section(self, readme_content):
        assert "## Contents" in readme_content

    def test_has_contributing_section(self, readme_content):
        assert "## Contributing" in readme_content

    def test_has_license_section(self, readme_content):
        assert "## License" in readme_content

    def test_contents_has_links(self, readme_content):
        # Contents section should have anchor links
        contents_match = re.search(
            r"## Contents\n\n((?:- \[.+\]\(#.+\)\n?)+)", readme_content
        )
        assert contents_match, "Contents must have anchor links"

    def test_ends_with_newline(self, readme_content):
        assert readme_content.endswith("\n")


class TestReadmeSections:
    """Verify required sections are present and in order."""

    REQUIRED_SECTIONS = [
        "Official SDKs",
        "Package Managers",
        "AI & MCP Integrations",
        "Developer Tools",
        "Example Projects",
        "Contributing",
        "License",
    ]

    def test_all_required_sections_present(self, readme_content):
        for section in self.REQUIRED_SECTIONS:
            assert f"## {section}" in readme_content, f"Missing section: {section}"

    def test_sections_in_order(self, readme_content):
        positions = []
        for section in self.REQUIRED_SECTIONS:
            pos = readme_content.find(f"## {section}")
            assert pos != -1, f"Section not found: {section}"
            positions.append(pos)
        assert positions == sorted(positions), "Sections are not in expected order"

    def test_contents_links_match_sections(self, readme_content):
        # Extract TOC entries
        toc_links = re.findall(r"- \[([^\]]+)\]\(#([^)]+)\)", readme_content)
        # Extract actual h2 sections (excluding Contents, Contributing, License)
        h2_sections = re.findall(r"^## (.+)$", readme_content, re.MULTILINE)
        h2_sections = [
            s for s in h2_sections if s not in ("Contents", "Contributing", "License")
        ]

        # Each TOC entry should correspond to an actual section
        for text, anchor in toc_links:
            # Convert section name to anchor format
            expected_anchor = text.lower().replace(" ", "-").replace("&", "").replace("--", "-")
            # At least check the text matches a section
            assert any(
                text.lower() in s.lower() for s in h2_sections
            ), f"TOC entry '{text}' has no matching section"


# ============================================================
# Entry format tests
# ============================================================


class TestEntryFormat:
    """Verify list entries follow the awesome-list format."""

    def test_entries_have_links(self, readme_content):
        """All non-placeholder entries should be markdown links."""
        # Find lines that start with "- " but aren't placeholders
        entry_lines = [
            line
            for line in readme_content.splitlines()
            if line.startswith("- ") and "_Your " not in line
        ]
        for line in entry_lines:
            if line.startswith("- ["):
                assert re.match(
                    r"- \[[^\]]+\]\([^)]+\)", line
                ), f"Bad link format: {line}"

    def test_entries_have_descriptions(self, readme_content):
        """All linked entries should have a description after the em dash."""
        entries = re.findall(
            r"^- \[[^\]]+\]\([^)]+\)(.*)$", readme_content, re.MULTILINE
        )
        for desc in entries:
            desc = desc.strip()
            if desc:  # Some entries in TOC don't have descriptions
                assert desc.startswith("—"), f"Description must start with em dash: '{desc}'"

    def test_descriptions_end_with_period(self, readme_content):
        """All descriptions should end with a period."""
        entries = re.findall(
            r"^- \[[^\]]+\]\([^)]+\) — (.+)$", readme_content, re.MULTILINE
        )
        for desc in entries:
            assert desc.rstrip().endswith("."), f"Description must end with period: '{desc}'"

    def test_no_duplicate_entries(self, readme_content):
        """No duplicate URLs in the list."""
        urls = re.findall(r"- \[[^\]]+\]\(([^)]+)\)", readme_content)
        # Filter out anchor links
        urls = [u for u in urls if not u.startswith("#")]
        seen = set()
        duplicates = []
        for url in urls:
            if url in seen:
                duplicates.append(url)
            seen.add(url)
        assert not duplicates, f"Duplicate URLs: {duplicates}"


# ============================================================
# Link validation tests
# ============================================================


class TestLinks:
    """Verify links are well-formed."""

    def test_all_urls_are_https(self, readme_content):
        """All external URLs should use HTTPS."""
        http_urls = re.findall(r"\(http://[^)]+\)", readme_content)
        assert not http_urls, f"Non-HTTPS URLs found: {http_urls}"

    def test_github_urls_format(self, readme_content):
        """GitHub URLs should follow standard format."""
        github_urls = re.findall(
            r"https://github\.com/([^)\"]+)", readme_content
        )
        for url in github_urls:
            # Should be owner/repo or owner/repo/tree/...
            parts = url.strip("/").split("/")
            assert len(parts) >= 2, f"Invalid GitHub URL path: {url}"

    def test_internal_links_valid(self, readme_content):
        """Internal file links should point to existing files."""
        internal_links = re.findall(
            r"\[([^\]]+)\]\((?!https?://|#)([^)]+)\)", readme_content
        )
        for text, path in internal_links:
            file_path = ROOT / path
            assert file_path.exists(), f"Broken internal link: [{text}]({path})"

    def test_anchor_links_valid(self, readme_content):
        """Anchor links in TOC should reference existing headings."""
        anchors = re.findall(r"\]\(#([^)]+)\)", readme_content)
        # Generate valid anchors from headings (GitHub-style)
        headings = re.findall(r"^##+ (.+)$", readme_content, re.MULTILINE)
        valid_anchors = set()
        for h in headings:
            anchor = h.lower()
            anchor = re.sub(r"[^\w\s-]", "", anchor)
            anchor = anchor.replace(" ", "-")
            valid_anchors.add(anchor)

        for anchor in anchors:
            assert anchor in valid_anchors, (
                f"Anchor '#{anchor}' not found. Valid: {sorted(valid_anchors)}"
            )


# ============================================================
# VecTrade ecosystem alignment tests
# ============================================================


class TestEcosystemAlignment:
    """Verify the list covers the full VecTrade ecosystem."""

    OFFICIAL_REPOS = [
        "vectrade-python",
        "vectrade-node",
        "vectrade-cli",
        "vectrade-mcp",
        "vectrade-openapi",
        "finkit",
    ]

    DISTRIBUTION_REPOS = [
        "homebrew-vectrade",
        "scoop-vectrade",
    ]

    def test_all_official_sdks_listed(self, readme_content):
        """All official repos should be mentioned."""
        for repo in self.OFFICIAL_REPOS:
            assert repo in readme_content, f"Missing official repo: {repo}"

    def test_all_distribution_repos_listed(self, readme_content):
        """All distribution repos should be mentioned."""
        for repo in self.DISTRIBUTION_REPOS:
            assert repo in readme_content, f"Missing distribution repo: {repo}"

    def test_mentions_vectrade_ai_provider(self, readme_content):
        assert "vectrade-ai-provider" in readme_content

    def test_mentions_openapi_spec(self, readme_content):
        assert "vectrade-openapi" in readme_content

    def test_mentions_sdk_generator(self, readme_content):
        assert "vectrade-sdk-generator" in readme_content


# ============================================================
# Formatting tests
# ============================================================


class TestFormatting:
    """Verify markdown formatting conventions."""

    def test_no_trailing_whitespace(self, readme_lines):
        for i, line in enumerate(readme_lines, 1):
            assert line == line.rstrip(), f"Trailing whitespace on line {i}"

    def test_no_tabs(self, readme_content):
        assert "\t" not in readme_content, "README must not contain tabs"

    def test_no_consecutive_blank_lines(self, readme_content):
        assert "\n\n\n" not in readme_content, "No triple+ blank lines allowed"

    def test_headings_have_blank_line_before(self, readme_lines):
        for i, line in enumerate(readme_lines):
            if line.startswith("## ") and i > 0:
                # Previous line should be blank (or ---) unless it's line 1
                prev = readme_lines[i - 1]
                assert prev.strip() == "" or prev.startswith("---"), (
                    f"Heading on line {i + 1} needs a blank line before it"
                )

    def test_single_h1(self, readme_content):
        h1_count = len(re.findall(r"^# ", readme_content, re.MULTILINE))
        assert h1_count == 1, f"Should have exactly 1 H1, found {h1_count}"


# ============================================================
# CONTRIBUTING.md tests
# ============================================================


class TestContributing:
    """Verify CONTRIBUTING.md is comprehensive."""

    def test_has_guidelines_section(self, contributing_content):
        assert "## Guidelines" in contributing_content

    def test_has_quality_standards(self, contributing_content):
        assert "Quality Standards" in contributing_content

    def test_has_entry_format(self, contributing_content):
        assert "Format" in contributing_content or "format" in contributing_content

    def test_has_process_section(self, contributing_content):
        assert "## Process" in contributing_content

    def test_mentions_pr(self, contributing_content):
        assert "Pull Request" in contributing_content or "PR" in contributing_content

    def test_has_categories(self, contributing_content):
        assert "Categories" in contributing_content or "categories" in contributing_content
