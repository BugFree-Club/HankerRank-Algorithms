#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
        if 'P'in s:
            s[1]+=2
            s[0]+=1

            if s[1]>'9':
                s[1]+=1                
        new_s=s[:-2]
        return new_s



        
        
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
