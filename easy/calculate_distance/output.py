#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""calculate distance

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following

(25, 4) (1, -6)
(47, 43) (-25, -11)
All numbers in input are integers between -100 and 100.

OUTPUT SAMPLE:

Print results in the following way.

26
90
You don't need to round the results you receive. They must be integer numbers.
"""

import sys
import re

def main():
	
    try:
        test_cases = open(sys.argv[1], 'r')
    except:
        sys.exit()

    for test in test_cases:
        a = test.strip()
        coordinates = re.sub('\s+', ' ', re.sub('\,', ' ', re.sub('\)', ' ', re.sub('\(', ' ', a)))).strip().split(' ')
        distance = ((int(coordinates[0]) - int(coordinates[2])) ** 2 + (int(coordinates[1]) - int(coordinates[3])) ** 2) ** 0.5
        print int(distance)		
    test_cases.close()

if __name__ == "__main__":
    main()
