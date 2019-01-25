time = input()
h, m, s = map(int, time[:-2].split(':'))
p = time[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))


'''%[(name)][flags][width].[precision]typecode
(name)为命名
flags可以有+,-,' '或0。+表示右对齐。-表示左对齐。' '为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0表示使用0填充。
width表示显示宽度
precision表示小数点后精度
typecode为类型码例如：%d,%s'''
