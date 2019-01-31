#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
    m = ar[0]
    count = 0
    for i in range(1, len(ar)):
        if m < ar[i]:
            m = ar[i]
    for j in range(0, len(ar)):
        if ar[j] == m:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
