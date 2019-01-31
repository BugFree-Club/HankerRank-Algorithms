# n = input()
# birds = list(map(int, input().split(' ')))
# sbirds = set(birds)
# li = []
# for i in sbirds:
#     li.append(birds.count(i))
# print(set.)
# print(dic.get(max(dic.values())))

# 老办法是理出一个新的包含不重复元素的li1和对应次数li2反推li1得出结果
# here is the way from forum
input()
count = [0]*6
for t in map(int,input().strip().split()):
    count[t] += 1
print(count.index(max(count)))