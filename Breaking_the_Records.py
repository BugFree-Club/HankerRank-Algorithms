# cant figure it out why it doesnt work
n = input()
scores, mn, mx = list(map(int, input().split(' '))), 0, 0
mn, mx = scores[0], scores[0]
cmn, cmx = 0, 0
for i in scores:
    if i < mn:
        mn = i
        cmn += 1
    elif i > mx:
        mx = i
        cmn += 1
print(cmn, cmx)
