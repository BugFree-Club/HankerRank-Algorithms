a = input()
a = a.split(' ')
b = input()
b = b.split(' ')
sa = 0
sb = 0
for i in range(3):
    if eval(a[i]) > eval(b[i]):
        sa += 1
    if eval(a[i]) == eval(b[i]):
        continue
    if eval(a[i]) < eval(b[i]):
        sb += 1
print('{} {}'.format(sa,sb))
