import argparse

from geoip_geosite_list.generate import generate
from geoip_geosite_list._version import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="geoip-geosite-list",
        description="A tool for generating a .txt file with domains supported by geosite.",
    )

    parser.add_argument(
        "-v", "--version", action="store_true", help="Show application version."
    )
    parser.add_argument(
        "-g",
        "--generate",
        action="store_true",
        help="Generate .txt file with domains.",
    )

    args = parser.parse_args()

    if args.version:
        print(f"version: {__version__}")
    elif args.generate:
        try:
            generate()
        except Exception as e:
            print(f"Error generating domains: {e}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
