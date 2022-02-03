#!/usr/bin/env python
"""Conventional commit for Machine Learning Ops."""

import sys
import re

SEMANTIC_PREFIXES = [
    "feat",
    "fix",
    "ci",
    "model",
    "eda",
    "report",
    "data",
    "build",
    "docs",
    "style",
    "refactor",
    "test",
    "perf",
    "chore",
    "revert",
]

SPECIAL_PREFIXES = ["Merge", "Bump", "Rebase", "Release"]


def check_special_prefixes(msg):
    """A msg starts with one of the special prefixes, it will be ignored.

    Parameters
    ----------
    msg : str
        The commit message.

    Returns
    -------
    bool
        True if the message starts with a special prefix.
    """
    if any([msg.startswith(prefix) for prefix in SPECIAL_PREFIXES]):
        print("INFO: Commit message starts with a special prefix.")
        return True
    return False


def check_msg_size(msg):
    """Check if the commit message is too long.

    Parameters
    ----------
    msg : str

    Returns
    -------
    bool
    """
    if len(msg) > 72:
        print(
            "ERROR: Commit message is too long. It should be 72 characters or"
            " less."
        )
        return False
    return True


def check_msg_prefix(msg):
    """Check if the header of the commit message starts with one of the
    semantic prefixes.

    That is, the commit message should be of the form
    '<prefix>(optional): <message>'

    Parameters
    ----------
    msg : str
        The commit message header.

    Returns
    -------
    bool
    """
    if all(
        [
            not re.match(f"^{prefix}(\\(.*?\\))?\\!?\\:", msg)
            for prefix in SEMANTIC_PREFIXES
        ]
    ):
        print(
            "ERROR: Commit message does not start with a semantic prefix.",
            file=sys.stderr,
        )
        print("Choose one of this prefixes:")
        print(
            ",".join(
                [f"\x1b[42m{prefix}\x1b[0m" for prefix in SEMANTIC_PREFIXES]
            )
        )
        return False
    return True


def check_header_is_meaningful(msg):
    """Check if the commit message header is meaningful.

    Parameters
    ----------
    msg : str
        The commit message header.

    Returns
    -------
    bool
        True if the commit message header is meaningful.
    """
    if len(msg.split(":")) < 2:
        print(
            "ERROR: Commit message header is not meaningful. It should be of"
            " the form '<prefix>(optional): <message>'",
            file=sys.stderr,
        )
        return False

    prefix, info = msg.split(": ", 1)
    if len(info.split()) < 2:
        print("ERROR: Commit message is too short.", file=sys.stderr)
        return False
    print(prefix, info)
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(0)

    msg_lines = open(sys.argv[1], "r").readlines()
    if len(msg_lines) == 0:
        print("ERROR: Commit message does not have a header.", file=sys.stderr)
        sys.exit(1)

    header = msg_lines[0]

    if check_special_prefixes(header):
        sys.exit(0)
    if not check_msg_size(header):
        sys.exit(1)
    if not check_msg_prefix(header):
        sys.exit(1)
    if not check_header_is_meaningful(header):
        sys.exit(1)
