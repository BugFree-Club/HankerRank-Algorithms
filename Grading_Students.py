li = []
for i in range(int(input())):
    score = int(input())
    if score >= 38 and score % 5 >= 3:
        score += (5 - score % 5)
    li.append(i)
for i in li:
    print(i)
