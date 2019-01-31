#!/bin/python3

a = []

b = 0

for i in range(int(input())):

    a = list(map(int, input().split()))

    b += a[i] - a[- 1 - i]

print(abs(b))