info = list(map(int,input().split(' ')))
x1, v1, x2,v2 = info[0],info[1],info[2],info[3]
if x2 > x1 and v2 >= v1 or x2 < x1 and v2<=v1:
    print('NO')
elif x2 > x1 and v2 < v1 or x2 > x1 and v2 > v1:
    if (x2 - x1) % (v2 - v1) == 0:
        print('YES')
    else:
        print('NO')