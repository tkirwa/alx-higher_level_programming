#!/usr/bin/python3
import sys


def print_metrics(status_codes, file_size):
    """Prints the computed metrics"""
    print("File size: {}".format(file_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k] > 0:
            print("{}: {}".format(k, status_codes[k]))


def parse_line(line, status_codes, file_size):
    """Parses a single line and updates the status_codes and file_size"""
    try:
        parts = line.split(" ")
        file_size += int(parts[-1])
        status_codes[parts[-2]] += 1
    except:
        pass
    return (status_codes, file_size)


if __name__ == "__main__":
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            status_codes, file_size = parse_line(
                line, status_codes, file_size)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(status_codes, file_size)

    except KeyboardInterrupt:
        print_metrics(status_codes, file_size)
        raise
