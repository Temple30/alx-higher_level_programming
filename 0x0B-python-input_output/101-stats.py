#!/usr/bin/python3
import sys
from collections import defaultdict

def print_statistics(total_size, status_count):
    print(f"Total file size: {total_size}")
    for code in sorted(status_count.keys()):
        print(f"{code}: {status_count[code]}")

def main():
    total_size = 0
    status_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            if len(parts) == 7:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                status_count[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_count)

    except KeyboardInterrupt:
        print_statistics(total_size, status_count)

if __name__ == "__main__":
    main()
