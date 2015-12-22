#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""hex to decimal

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Each line in this file contains a hex number. You may assume that the hex number does not have the leading 'Ox'. Also all alpha characters (a through f) in the input will be in lowercase. E.g.

9f
11
OUTPUT SAMPLE:

Print out the equivalent decimal number. E.g.

159
17
"""

import sys

def main():
    try:
        test_cases = open(sys.argv[1], 'r')
    except:
        sys.exit()

    hex_to_decimal = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}        
    for test in test_cases:
        result = 0
        index = 0
        hex = test.strip()
        hex = reversed(hex)
        for i in hex:
            if i.isdigit():
                result += int(i) * (16 ** index)

            else:
                result += hex_to_decimal[i] * (16 ** index)

            index += 1
            
        print result

    test_cases.close()

if __name__ == "__main__":
    main()
