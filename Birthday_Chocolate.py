# lenchoco = int(input())
# numchoco = list(map(int, input().split(' ')))
# Ronbirth = list(map(int, input().split(' ')))
# d,m = Ronbirth[0],Ronbirth[1]
# forum
def birthday(s, d, m, n):
    count = 0
    for i in range(n - m + 1):
        if (sum(s[i:m + i]) == d):
            count = count + 1
    return count

# ↑don't understand ↓does't work
# s = input()
# n = list(map(int, input().strip().split()))
# dm = list(map(int, input().strip().split()))
# d, m = dm[0], dm[1]
# print(birthday(s,d,m,n))
