#!/usr/bin/python3 
'''A script that reads stdin line by line and computes HTTP metrics.'''

import sys

# Dictionary to count HTTP status codes
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        # Ensure the line has enough parts for processing
        if len(line_list) > 4:
            code = line_list[-2]  # Extract the status code
            size = int(line_list[-1])  # Extract the size

            # Count the occurrences of each status code
            if code in cache.keys():
                cache[code] += 1
            total_size += size  # Accumulate total size
            counter += 1

        # Print metrics every 10 lines
        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass  # Ignore any exceptions

finally:
    # Print final metrics when the script ends
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:

            print('{}: {}'.format(key, value))

