cases = int(input())
li1 = []
for i in range(cases):
    treetall = 1
    case = int(input())
    if case == 1:
        treetall = treetall * 2
    elif case != 0:
        for terms in range(case // 2):
            treetall = treetall * 2 +1
        if case % 2 == 1:
            treetall = treetall * 2
    li1.append(treetall)

for y in li1:
    print(y)