Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(Weekday[0])   # 输出 Monday
# 队列list是可变长度的数据
# 列表可以完成大多数集合类的数据结构实现。
# 列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）
# list 队列 类似数组，首位从0开始，a.index搜索
print(Weekday.index("Wednesday"))

#list 增加元素
Weekday.append("new")
print(Weekday)

# list 删除
Weekday.remove("Thursday")  
print(Weekday)
