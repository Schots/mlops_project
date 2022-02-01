"""Tests for Conventional commit for Machine Learning Ops."""

from conventional_commits_for_mlops import (
    check_msg_size,
    check_msg_prefix,
    check_header_is_meaningful,
    SPECIAL_PREFIXES,
    check_special_prefixes,
)


def test_special_prefixes():
    """If the commit message starts with one of the special prefixes, it will
    be ignored."""

    assert all([check_special_prefixes(prefix) for prefix in SPECIAL_PREFIXES])
    assert not check_special_prefixes("merge")


def test_msg_size():
    """Test commit message size."""
    long_msg = "a" * 80
    short_msg = "a" * 70
    assert not check_msg_size(long_msg)
    assert check_msg_size(short_msg)


def test_msg_prefix():
    """Test commit message prefix."""
    assert not check_msg_prefix("update README.md")
    assert not check_msg_prefix("fix update README.md")
    assert check_msg_prefix("fix: update README.md")
    assert check_msg_prefix("fix(something): update README.md")
    assert check_msg_prefix("fix(something)!: update README.md")
    assert check_msg_prefix("fix!: update README.md")


def test_header_is_meanigful():
    """Test commit message header is meaningful."""
    assert not check_header_is_meaningful("fix: update README.md")
    assert check_header_is_meaningful(
        "feat(api)!: send an email to the customer when a product is shipped"
    )
