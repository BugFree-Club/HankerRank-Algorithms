time = input().strip()
h, m, s = map(int, time[:-2].split(':'))
print('%02d' % (h % 12 + 12 if 'PM' in time[-2:] else h % 12)+':%02d:%02d' % (m, s))
