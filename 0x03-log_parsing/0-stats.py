#!/usr/bin/python3
"""
Log parsing
"""


import sys
import signal


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line, total_size, status_codes):
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        total_size += file_size

        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status_code not in status_codes:
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1

        return total_size, status_codes
    except (ValueError, IndexError):
        return total_size, status_codes


def main():
    total_size = 0
    status_codes = {}
    line_count = 0

    signal.signal(signal.SIGINT, lambda signum, frame: print_stats(
        total_size, status_codes) or sys.exit(0))

    for line in sys.stdin:
        line = line.strip()
        total_size, status_codes = parse_line(line, total_size, status_codes)
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
