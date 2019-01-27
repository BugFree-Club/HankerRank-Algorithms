#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges, m, n):
    apple=0

    orange=0

    for i in range(m) :
        if a + apples[i] >= s and a + apples[i] <= t :
            apple+=1
            
    for j in range(n) :
        if b + oranges[j] >= s and b + oranges[j] <= t :
            orange+=1
            
    print(apple)
    
    print(orange)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])#房左

    t = int(st[1])#房右

    ab = input().split()

    a = int(ab[0])#苹果树

    b = int(ab[1])#橘子树

    mn = input().split()

    m = int(mn[0])#苹果数

    n = int(mn[1])#橘子数

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges, m, n)
