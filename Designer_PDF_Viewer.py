letter_height = list(map(int, input().strip().split()))
str1, li1 = input(), []
for i in str1:
    li1.append(letter_height[ord(i) - 97])  # 通过ASCII对应letter_height位数
print(len(str1) * max(li1))
