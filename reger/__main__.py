import sys

import reger.versioning.dvc_handler as dvc


def main():
    """The CLI entry point."""
    args = sys.argv[1:]
    print(f"{__name__} count of args {len(args)}")

    for i, arg in enumerate(args):
        print(f"{__name__} arg {i}: {arg}")

    dvc.test(args)


if __name__ == "__main__":
    main()
