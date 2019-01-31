# need to be improved but i dont know how to

houseLR = list(map(int,input().split(' ')))
AOtrees = list(map(int,input().split(' ')))
AOfruits = list(map(int,input().split(' ')))
apl = list(map(int,input().split(' ')))
orng = list(map(int,input().split(' ')))
capl,corng = 0,0
for x in apl:
    if houseLR[0] <= abs(AOtrees[0] + x) <= houseLR[1]:
        capl += 1
for y in orng:
    if houseLR[0] <= abs(AOtrees[1] + y) <= houseLR[1]:
        corng += 1
print(capl)
print(corng)
