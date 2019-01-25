#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    for i in range(n) :
        print(' ' if i<(n-j) else '#',end='')
    print()

if __name__ == '__main__':
    n = int(input())

    j=1
    
    for k in range(n) :
        staircase(n)
        j+=1
