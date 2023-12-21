#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
    - Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size> (if the format is not this one, the line must
    be skipped)
    - After every 10 lines and/or a keyboard interruption (CTRL + C), print
      these statistics from the beginning:
        - Total file size: File size: <total size>
        - where <total size> is the sum of all previous <file size>
        (see input format above)
        - Number of lines by status code:
            - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            - if a status code doesn’t appear or is not an integer, don’t
              print anything for this status code
            - format: <status code>: <number>
            - status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have
the same output as this on
"""
import sys

count = 0
total_size = 0
status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}


def print_metrics():
    """prints the statistics from the beginning"""

    print("File size: {}".format(total_size))

    for key, value in sorted(status_code.items()):
        if value > 0:
            print("{}: {}".format(key, value))

try:
    for line in sys.stdin:

        try:
            code = line.split()[-2]
            if code in status_code.keys():
                status_code[code] += 1
        except BaseException as _:
            pass

        try:
            size = line.split()[-1]
            total_size += int(size)
        except BaseException as _:
            pass

        count += 1
        if (count % 10 == 0):
            print_metrics()

    print_metrics()

except KeyboardInterrupt:
    print_metrics()
    raise