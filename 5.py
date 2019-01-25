Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zero=plus=negative=0
    i=0
    n=len(arr)
    for i in arr:
        if i==0:
            zero += 1
        if i>0:
            plus += 1
        if i<0:
            negative += 1

    print("%.6f" % ((plus/n)))
    print("%.6f" % ((negative/n)))
    print("%.6f" % ((zero/n)))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
