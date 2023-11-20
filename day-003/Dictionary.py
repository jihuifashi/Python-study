Logo_code = {
 'BIDU':'Baidu',
 'SINA':'Sina',
 'YOKU':'Youku'
 }#字典数据，可变长
#字典是一种键-值”(key-value)映射类型，字典的关键字必须为不可变类型，且不能重复。创建空字典使用 {}
print(Logo_code)
# 输出{'BIDU': 'Baidu', 'YOKU': 'Youku', 'SINA': 'Sina'}

print (Logo_code['SINA'])       # 输出键为 'one' 的值

print (Logo_code.keys())   # 输出所有键

print (Logo_code.values()) # 输出所有值

print (len(Logo_code))  # 输出字段长度
a={'om':8,'jerry':7}
print(a['om'])
b=dict(om=8,jerry=7)
print(b['om'])
if'jerry'in a:
  print(a['jerry'])
a['spike']=10
a['tyke']=3
a.update({'tuffy':2,'two shoes':42})
print(a.values())
