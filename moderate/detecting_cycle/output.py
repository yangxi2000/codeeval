#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Detecting Cycles

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename containing a sequence of numbers (space delimited). The file can have multiple such lines. E.g

2 0 6 3 1 6 3 1 6 3 1
3 4 8 0 11 9 7 2 5 6 10 1 49 49 49 49
1 2 3 1 2 3 1 2 3

OUTPUT SAMPLE:

Print to stdout the first cycle you find in each sequence. Ensure that there are no trailing empty spaces on each line you print. E.g.

6 3 1
49
1 2 3

The cycle detection problem is explained more widely on wiki 

Constrains: 
The elements of the sequence are integers in range [0, 99] 
The length of the sequence is in range [0, 50]
"""

def detecting_cycle(a):
    len_a = len(a)
    found = 0

    #思路是先确定要搜索的子列表的长度，和子列表的初始位置，比如要搜索[0,1,3,4,3,4]，那么有可能的重复子列表的长度分别是1，2，3
    #对于每个子列表，都有一个初始位置。比如子列表长度是2，那么初始位置为0时将[0,1]和[3,4]比较，初始位置为1时[1,3]和[4,3]比较，
    #初始位置为2时[3,4]和[3,4]比较
    
    #确定寻要要搜寻的子列表的长度范围。
    for len_sub_a in range(1, len_a/2+1):
        if len_a - 2 * len_sub_a >= 0:

            #确定要搜索的初始位置，比如列表长度是6，字列表长度是2，那么初始位置可能是
            #[0, 1, 2]，如果列表长度是7， 子列表长度是2，那么搜索初始位置可能是
            #[0, 1, 2, 3]
            for start_pos in range(len_a - 2 * len_sub_a + 1):

                #在每个初始位置，开始看这个初始位置开始的长度为len_sub_a的字列表
                #是否有一个紧跟着的重复的字列表。这需要比较字列表的每一个字符和下一个字列表的每一个字符
                for index in range(len_sub_a):
                    if a[start_pos + index] == a[start_pos + index+ len_sub_a]:

                        #如果找到一个相同的字符，比如搜索初始位置是0，子列表长度是3，列表长度是7的情况下，a[1] = a[4]
                        #那么将标志位置1，并比较字列表的下一个字符
                        found = 1
                    else:
                        #如果找到任何一个不相等的字符，比如比如搜索初始位置是0，子列表长度是3，列表长度是7的情况下，a[2] != a[5]
                        #那么标志位置0，退出循环。开始搜索下一个初始位置
                        found = 0
                        break

                #如果标志位为1，那么表示在这个初始位置开始的子列表和紧跟着的下一个字列表的所有字符都相同，那么找到重复的字列表。   
                if found == 1:
                    print ' '.join(a[start_pos:start_pos+len_sub_a])
                    break
                
        #如果找到第一个重复的子列表，那么退出循环        
        if found == 1:
            break
    
def main():
    import sys
    try:
        test_case = open(sys.argv[1], 'r')
    except:
        print("No input file specified")
        sys.exit()

    for test in test_case:
        digits = test.strip().split(' ')
        detecting_cycle(digits)
        
    test_case.close()

if __name__ == '__main__':
    main()
    
