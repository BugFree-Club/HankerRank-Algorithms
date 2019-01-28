#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
        k=[0,0,0,0,0,0]

    maxn=0

    for i in range(arr_count) :

        for j in range(1,6) :

            if arr[i]==j :

                k[j]+=1

    for i in range(6) :

        if k[i]>maxn :

            maxn=k[i]

            answer=i

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
