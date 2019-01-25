#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    height = list(map(int, input().split()))

    print(height.count(max(height)))
