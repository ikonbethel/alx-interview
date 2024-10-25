#!/usr/bin/python3
'''reads stdin line by line and computes metrics'''
import re
import sys


status_code_dict = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }
total_filesize = 0
count = 0


def print_metrics():
    '''Prints the current metrics'''
    print(f"File size: {total_filesize}")
    for key, value in status_code_dict.items():
        if value > 0:
            print(f"{key}: {value}")


try:
    for line in sys.stdin:
        pattern = r"^((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|\w+)\s*-\s*"
        pattern += r"(\[\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}\.\d{6}\]) "
        pattern += r"(\"GET \/projects\/260 HTTP\/1.1\" \w+ \d+)$"
        if re.match(pattern, line):
            split_content = line.split()
            status_code = split_content[-2]
            file_size = split_content[-1]
            pattern = r"\d+"
            if not re.match(pattern, file_size):
                total_filesize += int(file_size)
                count += 1
                continue
            if status_code in status_code_dict:
                status_code_dict[status_code] += 1
            total_filesize += int(file_size)
            count += 1
            if not count % 10:
                print_metrics()
except (KeyboardInterrupt, EOFError) as e:
    print_metrics()
    sys.exit()

print_metrics()
