#!/bin/python3

import math
import os
import random
import re
import sys

year = int(input().strip())

if year%400==0 or ( year%4 == 0 and (year%100) != 0 ) :

    print ("%02s.09.%d" % ("12",year) )

else :

    print ("%02s.09.%d" % ("13",year) )
