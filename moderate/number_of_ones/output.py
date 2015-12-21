#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Number of Ones

INPUT SAMPLE:

The first argument is a path to a file. The file contains integers, one per line.

For example:

10
22
56

OUTPUT SAMPLE:

Print to stdout the number of ones in the binary form of each number.

For example:

2
3
3

"""
# import pdb
# pdb.set_trace()
def calc_ones(num):
	
	index = 0
	while 2 ** index < num:
		index += 1
	ones = 0
	for i in range(index):
		if ((num & (2 ** i)) >> i) == 1:
			ones += 1
	print ones	
	
    
def main():
    import sys
    try:
        test_case = open(sys.argv[1], 'r')
    except:
        print("No input file specified")
        sys.exit()

    for test in test_case:
        num = int(test.strip()) 
        calc_ones(num)       
    test_case.close()

if __name__ == '__main__':
    main()
    
