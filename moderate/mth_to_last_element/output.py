#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mth to last element

INPUT SAMPLE:

The first argument is a path to a file. The file contains the series of space delimited characters followed by an integer. The integer represents an index in the list (1-based), one per line.

For example:

a b c d 4
e f g h 2

OUTPUT SAMPLE:

Print to stdout the Mth element from the end of the list, one per line. If the index is larger than the number of elements in the list, ignore that input.

For example:

a
g

"""
# import pdb
# pdb.set_trace()
    
def main():
    import sys
    try:
        test_case = open(sys.argv[1], 'r')
    except:
        print("No input file specified")
        sys.exit()

    for test in test_case:
        txt = test.strip().split(' ')[:-1]
        num = int(test.strip().split(' ')[-1])
        if len(txt) < num:
        	continue
        else:
        	print txt[0-num]
        
    test_case.close()

if __name__ == '__main__':
    main()
    
