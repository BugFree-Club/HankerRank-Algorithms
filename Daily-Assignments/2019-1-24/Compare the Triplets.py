#!/bin/python3

a = list(map(int, input().split()))

b = list(map(int, input().split()))

Score1 = sum([(1 if a[i] > b[i] else 0) for i in range(3)])

Score2 = sum([(1 if a[i] < b[i] else 0) for i in range(3)])

print(Score1, Score2)