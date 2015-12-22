#!/usr/bin/python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.strip()
    	stack1 = reversed(test.split(' '))
    	stack2 = []
    	for i in stack1:
    		if i.isdigit():
			stack2.append(i)
		else:
			op1 = float(stack2.pop())
			op2 = float(stack2.pop())
			if i == '*':
				stack2.append(op1 * op2)
			elif i == '+':
				stack2.append(op1 + op2)
			elif i == '/':
				stack2.append(op1 / op2)
	print int(stack2.pop())
	
test_cases.close()
