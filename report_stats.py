# coding:utf-8
with open('E:/report.txt') as f:
    lines = f.readlines()
results = []
for line in lines:
    single = line.split()
    sum = 0
    for i in single[1:]:
        sum += int(i)
    single.append(sum)
    single.append(round(sum / 9.0, 1))
    print single
    results.append(single)
results.sort(key=lambda x:x[11],reverse=True)
print results