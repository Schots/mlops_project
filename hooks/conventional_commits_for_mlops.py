#!/usr/bin/env python

import sys
import re

SEMANTIC_PREFIXES = [
    "feat",
    "fix",
    "ci",
    "revert",
    "model",
    "docs",
    "style",
    "refactor",
    "test",
    "perf",
]


def check_msg_size(msg):
    """Check if the commit message is too long."""
    if len(msg) > 72:
        print(
            "ERROR: Commit message is too long. It should be 72 characters or"
            " less."
        )
        return False
    return True


def check_msg_prefix(msg):
    """Check if the header of the commit message starts with one of the
    semantic prefixes. That is, the commit message should be of the form
    '<prefix>(optional): <message>'

    Parameters
    ----------
    header_msg : str
        The commit message header.

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
        return False
    return True


def check_header_is_meaningful(msg):
    """Check if the commit message header is meaningful.

    Parameters
    ----------
    header : str
        The commit message header.

    Returns
    -------
    prefix : str
        The prefix of the commit message header.
    message : str
        The message of the commit message header.
    """
    if len(msg.split(":")) < 2:
        print(
            "ERROR: Commit message header is not meaningful. It should be of"
            " the form '<prefix>(optional): <message>'",
            file=sys.stderr,
        )
        return False

    prefix, info = msg.split(": ", 1)
    if len(info.split()) < 3:
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

    if not check_msg_size(header):
        sys.exit(1)
    if not check_msg_prefix(header):
        sys.exit(1)
    if not check_header_is_meaningful(header):
        sys.exit(1)
