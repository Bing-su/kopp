import argparse

from .main import josa


def cli() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="text to convert", type=str)
    args = parser.parse_args()

    print(josa(args.text))


if __name__ == "__main__":
    cli()
