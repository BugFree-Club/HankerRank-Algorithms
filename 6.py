#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
        positive=negetive=zero=0
        t=0
        while t<n:
            if(arr[t]<0):
                negetive+=1
            elif(arr[t]==0):
                positive+=1
            else:
                zero+=1
            t+=1    
        print('%.6f'%(zero/n))
        print('%.6f'%(negetive/n))
        print('%.6f'%(positive/n))                

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
