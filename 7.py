#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
        t=1
        while t<=n:
            d=1
            while d<=n:
                if d<=n-t:
                    print(" ",end="")
                else :
                    print("#",end="")
                d+=1
            print("")
            t+=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)