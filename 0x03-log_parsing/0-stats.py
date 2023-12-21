#!/usr/bin/env python3
"""
Log parsing interview task
"""

import sys
import signal


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        print(f"{code}: {status_codes[code]}")


def parse_line(line, total_size, status_codes):
    try:
        parts = line.split()
        file_size, status_code = map(int, (parts[-1], parts[-2]))
        total_size += file_size

        valid_status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
        if status_code in valid_status_codes:
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

        return total_size, status_codes
    except (ValueError, IndexError):
        # Skip lines with incorrect format
        return total_size, status_codes


def main():
    total_size = 0
    status_codes = {}
    line_count = 0

    def handle_interrupt(signum, frame):
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_interrupt)

    for line in sys.stdin:
        line = line.strip()
        total_size, status_codes = parse_line(line, total_size, status_codes)
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
