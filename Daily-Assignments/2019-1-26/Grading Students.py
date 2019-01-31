#!/bin/python3

import os
import sys

n=int(input())

for i in range(n):

    grade = int(input())

    if grade >= 38 and grade % 5 >= 3:

        grade = (grade + 5) // 5 * 5

    print(grade)

