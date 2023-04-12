#!/usr/bin/python3
import sys


def print_stats(file_size, status_codes):
    """Prints the current stats"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line, status_codes):
    """Parses a log line and updates the status codes and file size"""
    try:
        line_parts = line.split()
        status = line_parts[-2]
        if status in status_codes:
            status_codes[status] += 1
        file_size = int(line_parts[-1])
    except:
        return 0
    return file_size


if __name__ == "__main__":
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for i, line in enumerate(sys.stdin, 1):
            file_size += parse_line(line, status_codes)
            if i % 10 == 0:
                print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
