lst = list(map(int, input().split(' ')))
x = sum(lst)
print(x-(max(lst)), (x-(min(lst))))
