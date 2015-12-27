#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""black card
TESTING
CHALLENGE DESCRIPTION:

In many teams, there is a person who tests a project, finds bugs and errors, and prioritizes them.
Now, you have the unique opportunity to try yourself as a tester and test a product. Here, you have two strings - the first one is provided by developers, and the second one is mentioned in design. You have to find and count the number of bugs, and also prioritize them for fixing using the following statuses: 'Low', 'Medium', 'High', 'Critical' or 'Done'.

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case with two strings separated by a pipeline '|'. The first string is the one the developers provided to you for testing, and the second one is from design.


Heelo Codevval | Hello Codeeval
hELLO cODEEVAL | Hello Codeeval
Hello Codeeval | Hello Codeeval

OUTPUT SAMPLE:

Write a program that counts the number of bugs and prioritizes them for fixing using the following statuses: 
'Low' - 2 or fewer bugs; 
'Medium' - 4 or fewer bugs; 
'High' - 6 or fewer bugs; 
'Critical' - more than 6 bugs; 
'Done' - all is done; 

Low
Critical
Done

CONSTRAINTS:

Strings are of the same length from 5 to 40 characters.
Upper and lower case matters.
The number of test cases is 40.
"""

import sys

def main():
	try:
		test_cases = open(sys.argv[1], 'r')
	except:
		sys.exit()
	
	for test in test_cases:
		sev = 0
		(txt, example) = test.strip().split(' | ')
		for op in zip(txt,example):
			if op[0] != op[1]:
				sev += 1
		if sev <= 2 and sev > 0:
			print 'Low'
		elif sev > 2 and sev <= 4:
			print 'Medium'
		elif sev > 4 and sev <= 6:
			print 'High'
		elif sev > 6:
			print 'Critical'
		elif sev == 0:
			print 'Done'
		
     
	test_cases.close()

if __name__ == "__main__":
    main()
