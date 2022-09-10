#!/usr/bin/env python
import argparse
from gendiff.diff_with_formatter import generate_diff


def main():
    program_name = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=program_name)
    first_file = parser.add_argument("first_file")
    second_file = parser.add_argument("second_file")
    format_file = parser.add_argument("-f", "--format",
            help="set format of output")
    args = parser.parse_args()
    print(
      generate_diff(args.first_file, args.second_file))



if __name__ == '__main__':
    main()

