#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


if __name__ == "__main__":
    import sys

    total_size = 0
    status_count = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                file_size = int(parts[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            try:
                status_code = parts[-2]
                if status_code in valid_codes:
                    status_count[status_code] = status_count.get(status_code, 0) + 1
            except IndexError:
                pass

            if line_count % 10 == 0:
                print_stats(total_size, status_count)
                total_size = 0
                status_count = {}

        print_stats(total_size, status_count)

    except KeyboardInterrupt:
        print_stats(total_size, status_count)
        raise
