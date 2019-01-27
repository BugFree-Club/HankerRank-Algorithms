#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxn=scores[0]
    
    minn=scores[0]
    
    H=0
    
    L=0
    
    for i in range(n) :
        
        if maxn<scores[i] :
            
            maxn=scores[i]
            
            H+=1
            
        if minn>scores[i] :
            
            minn=scores[i]
            
            L+=1
            
    return H,L

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
