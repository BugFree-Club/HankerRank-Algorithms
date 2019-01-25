Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    kong=n-1
    jing=1
    for x in range(n):
        for y in range(kong):
            print(" ",end="")
        kong-=1
        for z in range(jing):
            print("#",end="")
        jing+=1
        print("\n",end="")
        
if __name__ == '__main__':
    n = int(input())

