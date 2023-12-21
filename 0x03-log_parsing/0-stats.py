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


words = []
size_list = []
status_dict = {'200': 0, '301': 0, '400': 0,
               '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
sum_size = 0

try:
    for line in sys.stdin:
        words.append(line)
        if len(words) % 10 == 0:
            for i in range(len(words)):
                size_file = words[i]
                file_split = size_file.split(' ')
                file_size = file_split[-1]
                status_code = file_split[-2]
                if status_code in status_dict:
                    status_dict[status_code] += 1
                size_list.append(file_size)
            for sizes in size_list:
                sum_size = sum_size + int(sizes)
            print("File size: {}".format(sum_size))
            for k, v in status_dict.items():
                if status_dict[k] != 0:
                    print("{}: {}".format(k, status_dict[k]))
            status_dict = {'200': 0, '301': 0, '400': 0,
                           '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
except KeyboardInterrupt:
    pass
finally:
    for sizes in size_list:
        sum_size = sum_size + int(sizes)
    print("File size: {}".format(sum_size))
    for k, v in status_dict.items():
        if status_dict[k] != 0:
            print("{}: {}".format(k, status_dict[k]))
