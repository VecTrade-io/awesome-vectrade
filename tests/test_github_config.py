"""Tests for awesome-vectrade CI workflow and GitHub configuration."""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
CI_FILE = ROOT / ".github" / "workflows" / "ci.yml"
CODEOWNERS_FILE = ROOT / ".github" / "CODEOWNERS"
PR_TEMPLATE_FILE = ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md"
ISSUE_TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
SECURITY_FILE = ROOT / "SECURITY.md"


@pytest.fixture
def ci_content():
    """Load CI workflow content."""
    return CI_FILE.read_text()


@pytest.fixture
def codeowners_content():
    """Load CODEOWNERS content."""
    return CODEOWNERS_FILE.read_text()


@pytest.fixture
def pr_template_content():
    """Load PR template content."""
    return PR_TEMPLATE_FILE.read_text()


@pytest.fixture
def security_content():
    """Load SECURITY.md content."""
    return SECURITY_FILE.read_text()


# ============================================================
# GitHub config file existence
# ============================================================


class TestGitHubConfigExists:
    """Verify GitHub configuration files exist."""

    def test_ci_workflow_exists(self):
        assert CI_FILE.is_file()

    def test_codeowners_exists(self):
        assert CODEOWNERS_FILE.is_file()

    def test_pr_template_exists(self):
        assert PR_TEMPLATE_FILE.is_file()

    def test_issue_template_dir_exists(self):
        assert ISSUE_TEMPLATE_DIR.is_dir()

    def test_security_file_exists(self):
        assert SECURITY_FILE.is_file()

    def test_add_project_template_exists(self):
        assert (ISSUE_TEMPLATE_DIR / "add_project.md").is_file()

    def test_broken_link_template_exists(self):
        assert (ISSUE_TEMPLATE_DIR / "broken_link.md").is_file()


# ============================================================
# CI workflow tests
# ============================================================


class TestCIWorkflow:
    """Verify CI workflow is properly configured."""

    def test_has_name(self, ci_content):
        assert "name: CI" in ci_content

    def test_triggers_on_push_main(self, ci_content):
        assert "push:" in ci_content
        assert "main" in ci_content

    def test_triggers_on_pull_request(self, ci_content):
        assert "pull_request:" in ci_content

    def test_triggers_on_workflow_dispatch(self, ci_content):
        assert "workflow_dispatch:" in ci_content

    def test_has_permissions(self, ci_content):
        assert "permissions:" in ci_content
        assert "contents: read" in ci_content

    def test_uses_checkout_v4(self, ci_content):
        assert "actions/checkout@v4" in ci_content

    def test_has_lint_job(self, ci_content):
        assert "lint:" in ci_content or "Lint" in ci_content

    def test_has_validate_job(self, ci_content):
        assert "validate:" in ci_content or "Validate" in ci_content

    def test_has_links_job(self, ci_content):
        assert "links:" in ci_content or "Links" in ci_content

    def test_runs_pytest(self, ci_content):
        assert "pytest" in ci_content

    def test_uses_python_setup(self, ci_content):
        assert "actions/setup-python@v5" in ci_content

    def test_checks_markdown_structure(self, ci_content):
        assert "markdown" in ci_content.lower() or "section" in ci_content.lower()

    def test_checks_link_format(self, ci_content):
        assert "link" in ci_content.lower() or "format" in ci_content.lower()


# ============================================================
# CODEOWNERS tests
# ============================================================


class TestCodeowners:
    """Verify CODEOWNERS is properly configured."""

    def test_has_global_owner(self, codeowners_content):
        assert "*" in codeowners_content

    def test_references_vectrade_team(self, codeowners_content):
        assert "@VecTrade-io/" in codeowners_content

    def test_no_empty_file(self, codeowners_content):
        assert len(codeowners_content.strip()) > 0


# ============================================================
# PR template tests
# ============================================================


class TestPRTemplate:
    """Verify PR template has useful structure."""

    def test_has_summary_section(self, pr_template_content):
        assert "Summary" in pr_template_content or "summary" in pr_template_content

    def test_has_checklist(self, pr_template_content):
        assert "- [ ]" in pr_template_content

    def test_mentions_format(self, pr_template_content):
        assert "format" in pr_template_content.lower()

    def test_mentions_tests(self, pr_template_content):
        assert "pytest" in pr_template_content or "test" in pr_template_content.lower()

    def test_mentions_duplicates(self, pr_template_content):
        assert "duplicate" in pr_template_content.lower()


# ============================================================
# Issue template tests
# ============================================================


class TestIssueTemplates:
    """Verify issue templates are properly structured."""

    def test_add_project_has_frontmatter(self):
        content = (ISSUE_TEMPLATE_DIR / "add_project.md").read_text()
        assert content.startswith("---")
        assert "name:" in content
        assert "about:" in content

    def test_add_project_has_fields(self):
        content = (ISSUE_TEMPLATE_DIR / "add_project.md").read_text()
        assert "Name:" in content
        assert "URL:" in content
        assert "Category:" in content

    def test_broken_link_has_frontmatter(self):
        content = (ISSUE_TEMPLATE_DIR / "broken_link.md").read_text()
        assert content.startswith("---")
        assert "name:" in content
        assert "about:" in content

    def test_broken_link_has_fields(self):
        content = (ISSUE_TEMPLATE_DIR / "broken_link.md").read_text()
        assert "URL:" in content
        assert "404" in content or "broken" in content.lower()


# ============================================================
# SECURITY.md tests
# ============================================================


class TestSecurity:
    """Verify SECURITY.md is present and correct."""

    def test_mentions_reporting(self, security_content):
        assert "report" in security_content.lower()

    def test_has_email(self, security_content):
        assert "security@vectrade.io" in security_content

    def test_has_response_time(self, security_content):
        assert "48 hours" in security_content or "48h" in security_content
