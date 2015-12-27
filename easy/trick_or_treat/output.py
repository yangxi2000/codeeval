#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""TRICK OR TREAT

CHALLENGE DESCRIPTION:

Everyone knows what Halloween is and how children love it. Children in costumes travel from house to house asking for treats with a phrase "Trick or treat". After that, they divide the treats equally among all. This year, they collected tons of candies, and need your help to share everything equally. 
You know that children receive different number of candies depending on their costume: vampire gets 3 candies from one house, zombie – 4 candies, and witch – 5 candies. 
That is, three children in three different costumes get 3+4+5=12 candies from one house.

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case with number of vampires, zombies, witches, and houses that they visited.

For example:


Vampires: 1, Zombies: 1, Witches: 1, Houses: 1
Vampires: 3, Zombies: 2, Witches: 1, Houses: 10

OUTPUT SAMPLE:

You need to print number of candies that each child will get. If the number is not integer, round it to the lower: for example, if the resulting number is 13.666, round it to 13.

For example:


4
36
CONSTRAINTS:

Number of vampires, zombies, witches, and houses can be from 0 to 100.
If the final number of candies is not integer, round it to the lower.
The number of test cases is 40.
"""

import sys

def main():
	try:
		test_cases = open(sys.argv[1], 'r')
	except:
		sys.exit()
	
	for test in test_cases:
		
		(v, z, w, h) = test.strip().split(', ')
		rule = {'Vampires':3, 'Zombies':4, 'Witches':5}
		num_v = int(v.split(': ')[1])
		num_z = int(z.split(': ')[1])
		num_w = int(w.split(': ')[1])
		num_h = int(h.split(': ')[1])
		sum = num_v * rule['Vampires'] + num_z * rule['Zombies'] + num_w * rule['Witches']
		sum *= num_h
		
		print int(sum / (num_v + num_z + num_w)) 
		
     
	test_cases.close()

if __name__ == "__main__":
    main()
