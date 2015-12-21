#!/usr/bin/env python
"""string list

INPUT SAMPLE:

The first argument will be the path to the input filename containing the test data. Each line in this file is a separate test case. Each line is in the format: N,S i.e. a positive integer, followed by a string (comma separated). E.g.

1,aa
2,ab
3,pop

OUTPUT SAMPLE:

Print all of the possible ways to write a string of length N from the characters in string S comma delimited in alphabetical order, with no duplicates. E.g.

a
aa,ab,ba,bb
ooo,oop,opo,opp,poo,pop,ppo,ppp

"""
import sys

try:
	test_case = open(sys.argv[1], 'r')
except:
	print "No input file specified"
	sys.exit()


def g(depth):       
        for  i in range(len(t1)):
                tmp_string[depth] = t1[i]
                if depth != num - 1:                
                        g(depth+1)
                if depth == num -1:
                        result.append(''.join(tmp_string))
                if depth == num - 1 and i == len(t1) - 1:
                        return
                
for test in test_case:
        [num_txt, text] = test.split(',')
        num = int(num_txt)
        text = text.strip()
        tmp_string = [''] * num
        result=[]
        depth = 0
        t1 = text
        g(depth)
        print ','.join(sorted(set(result)))
        
test_case.close()

