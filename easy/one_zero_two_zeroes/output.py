#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""ONE ZERO, TWO ZEROS...

CHALLENGE DESCRIPTION:

Our agent uncovered a global criminal money-laundering network that used offshore companies to defraud international organizations of total $1,000,000,000! The agent changes his location each hour, but he manages to send us the code that we need to decipher. 
Deciphering code includes many stages, and you are taking part in one of them. Therefore, your task is the following: you have two numbers – the first one is the number of zeros in a binary code and the second one shows the range from 1 to this number, where you have to find these zeros. 
For example, for the given numbers 2 and 4, you convert all numbers from 1 to 4 inclusive into the binary system. As a result, you get 1, 10, 11, and 100. As the first given number is 2, this means that we are looking for numbers with two zeros, so only 100 suits us. Hence, the result will be 1: there is only one number with two zeros.

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case with two numbers: the first one is the number of zeros in a binary code that we need to find and the second one is the range from 1 to this number where you have to find these zeros.

For example:

1 8
2 4

OUTPUT SAMPLE:

Print the total number of numerals that contain the needed amount of zeros in a binary system.

For example:

3
1

CONSTRAINTS:

Range can be from 5 to 1000.
Number of zeros does not exceed the length of binary code number.
The number of test cases is 40.
"""

import sys


def main():
	try:
		test_cases = open(sys.argv[1], 'r')
	except:
		sys.exit()
	
	for test in test_cases:
		
		test = test.strip().split(' ')
		expect_zeroes = int(test[0])
		num = int(test[1])
		found_num = 0
		for i in range(1, num+1):
			found_zeroes = 0
			while i > 1:
				if i % 2 == 0:
					found_zeroes += 1
				i = i >> 1
			if found_zeroes == expect_zeroes:
				found_num += 1
		print found_num
     	
	test_cases.close()

if __name__ == "__main__":
    main()
