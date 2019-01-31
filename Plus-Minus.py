n = eval(input())
li = input()
li = li.split(' ')
pstv = 0
ngtv = 0
zero = 0
for i in li:
    if eval(i) > 0:
        pstv += 1
    elif eval(i) < 0:
        ngtv += 1
    else:
        zero += 1
print('{:.6f}\n{:.6f}\n{:.6f}'.format(pstv/n, ngtv/n, zero/n))
