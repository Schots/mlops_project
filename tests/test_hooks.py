"""Tests for Conventional commit for Machine Learning Ops."""

from hooks.conventional_commits_for_mlops import (
    check_msg_size,
    check_msg_prefix,
    check_header_is_meaningful,
)


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
