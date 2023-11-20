from matplotlib import pyplot as plt

a = ["一月份","二月份","三月份","四月份","五月份","六月份"]
#a是一个list
# Python3 中有六个标准的数据类型：Number（数字）、String（字符串）、List（列表）
# Tuple（元组）、Sets（集合）、Dictionary（字典）。
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
b=[56.01,26.94,17.53,16.49,15.45,12.96]

plt.figure(figsize=(20,8),dpi=80)
plt.figure(figsize=(100,8),dpi=80)
plt.bar(range(len(a)),b)

#绘制x轴
plt.xticks(range(len(a)),a)

plt.xlabel("month")
plt.ylabel("num")
plt.title("num per month")

plt.show()