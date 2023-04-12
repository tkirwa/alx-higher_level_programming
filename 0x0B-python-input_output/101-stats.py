#!/usr/bin/env python3
import sys
import signal

def print_stats(total_file_size, status_codes):
    print("File size: {}".format(total_file_size))
    for k in sorted(status_codes.keys()):
        if status_codes[k]:
            print("{}: {}".format(k, status_codes[k]))

def parse_line(line):
    parts = line.split()
    return (int(parts[-2]), int(parts[-1]))

def main():
    total_file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    def signal_handler(signal, frame):
        print_stats(total_file_size, status_codes)
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        line_count += 1
        try:
            status_code, file_size = parse_line(line)
            total_file_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except:
            pass

        if line_count == 10:
            print_stats(total_file_size, status_codes)
            line_count = 0

    print_stats(total_file_size, status_codes)

if __name__ == "__main__":
    main()
