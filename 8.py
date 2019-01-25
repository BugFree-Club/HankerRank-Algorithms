#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
        sumi=sum(arr)
        mini=arr[0]
        maxi=arr[0]
        t=1
        n=len(arr)
        while t<n:
            if arr[t]<=mini:
                mini=arr[t]
            if arr[t]>=maxi:
                maxi=arr[t]
            t+=1
        print(sumi-maxi,end=" ") 
        print(sumi-mini)
               
                     

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)