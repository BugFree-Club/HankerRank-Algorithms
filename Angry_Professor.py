cases = int(input())


def timing(num):
    if int(num) <= 0:
        return 1
    else:
        return 0


for i in range(cases):
    rule, student = list(map(int, input().strip().split())), list(map(timing, input().strip().split()))
    print('YES' if sum(student) < rule[1] else 'NO')
