#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
        birth=ar[0]
        t=0
        count=0
        while t<ar_count:
            if ar[t]>birth:
                birth=ar[t]
            t+=1
        d=0
        while d<ar_count:
            if ar[d]==birth:
                count+=1
            d+=1    
        return count          
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
