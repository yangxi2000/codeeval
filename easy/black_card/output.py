#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""black card

CHALLENGE DESCRIPTION:

You must have heard about pirates, their customs, pirates code, and the “black spot”. If a pirate is presented with a “black spot”, he is officially pronounced guilty, meaning he will soon be expulsed from the pirate brotherhood or even be dead. 
We don’t have as strict rules as pirates have, and a person who receives a black spot simply leaves the game. 
For example, we have a list of three players: John, Tom, Mary, and a number 5. Starting with the first player (in our case, it’s John), we start to count all players: John – 1, Tom – 2, Mary – 3, and then again starting from the first one John – 4, Tom – 5. As Tom gets number 5, he should leave. Now, we have John and Mary and start counting again. John gets number 5, so he leaves. Thus, the winner is Mary.

INPUT SAMPLE:

The first argument is a path to a file. Each line includes a test case with names of players and a number for a “black spot”. Players and a number are separated by a pipeline '|'.

For example:

John Sara Tom Susan | 3
John Tom Mary | 5

OUTPUT SAMPLE:

Print the name of a winner.

For example:

2
Sara
Mary

CONSTRAINTS:

Always start counting from the first name in a list.
Number of players can be from 3 to 10.
Number of turns can be from 3 to 15.
The number of test cases is 40.
"""

import sys


def main():
    try:
        test_cases = open(sys.argv[1], 'r')
    except:
        sys.exit()

    for test in test_cases:
        (lst, number) = test.strip().split(' | ')
        names = lst.split(' ')
        number = int(number)
        while len(names) > 1:
                del names[number % len(names) - 1]
                
        print names[0]
     
    test_cases.close()

if __name__ == "__main__":
    main()
