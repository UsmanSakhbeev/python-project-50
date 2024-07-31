#!/usr/bin/env python3


import argparse

from gendiff.generate_difference import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Shows differences.")
    parser.add_argument("first_file", type=str, help="First conf file")
    parser.add_argument("second_file", type=str, help="Second conf file")
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        default="stylish",
        choices=["stylish", "json", "plain"],
        help="set format of output (default: stylish)",
    )

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
