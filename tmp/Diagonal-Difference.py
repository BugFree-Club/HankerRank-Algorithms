useful = input()
li = []
for i in range(eval(useful)):
    li.append(input())
liinter = []

lidone = []
for i in li:
    liinter = i.split(' ')
    liinter2 = []
    for j in liinter:
        liinter2.append(eval(j))
    lidone.append(liinter2)
counta = 0
suma = 0
for x in lidone:
    suma += x[counta]
    counta += 1
countb = 0
sumb = 0
lidone = reversed(lidone)
for x in lidone:
    sumb += x[countb]
    countb += 1
print(abs(suma - sumb))
