#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""prefix expression

CHALLENGE DESCRIPTION:

You are given a prefix expression. Write a program which evaluates it.


INPUT SAMPLE:

Your program should accept a file as its first argument. The file contains one prefix expression per line.

For example:

* + 2 3 4

Your program should read this file and insert it into any data structure you like. Traverse this data structure and evaluate the prefix expression. Each token is delimited by a whitespace. You may assume that sum ‘+’, multiplication ‘*’ and division ‘/’ are the only valid operators appearing in the test data.


OUTPUT SAMPLE:

Print to stdout the output of the prefix expression, one per line.

For example:

20

CONSTRAINTS:

The evaluation result will always be an integer ≥ 0.
The number of the test cases is ≤ 40.

"""
import sys
import re

class stack():

        def __init__(self):
                self.items = []
        def push(self, item):
                self.items.append(item)
        def pop(self):
                return self.items.pop()
        def size(self):
                return len(self.items)
        def empty(self):
                return self.size() == 0
        
              
def calc_result(calc_exp):
        if calc_exp[-1] == '*':
                return str(float(calc_exp[-2]) * float(calc_exp[-3]))
        elif calc_exp[-1] == '+':
                return str(float(calc_exp[-2]) + float(calc_exp[-3]))
        elif calc_exp[-1] == '/':
                return str(float(calc_exp[-2]) / float(calc_exp[-3]))
        
try:
	test_case = open(sys.argv[1], 'r')
except:
	print "No input file specified"
	sys.exit()
                
for test in test_case:
        
        stack_l = stack()
        stack_r = stack()
     
   
        for i in test.strip().split(' '):
                stack_l.push(i)
        while stack_l.size() > 0:
                element = stack_l.pop()
                stack_r.push(element)
                if element.isdigit():
                        pass
                else:
                        calc_exp = stack_r.items[-3:]
                        tmp_result = calc_result(calc_exp)
                        stack_r.pop()
                        stack_r.pop()
                        stack_r.pop()
                        stack_r.push(tmp_result)
      
        print int(float(stack_r.pop()))
                        
     

        
test_case.close()

