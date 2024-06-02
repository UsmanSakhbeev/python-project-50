#!/usr/bin/env python3


import argparse


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first file")
    parser.add_argument("second file")

    args = parser.parse_args()

    print()


if __name__ == "__main__":
    main()