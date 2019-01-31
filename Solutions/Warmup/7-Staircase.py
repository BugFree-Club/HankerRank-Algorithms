#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
     [print( " "*(n-i-1)+"#"*(i+1)) for i in range(n)]

     
if __name__ == '__main__':
    n = int(input())

    staircase(n)
