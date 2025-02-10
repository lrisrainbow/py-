#列表属于序列，所有对序列的操作，运算均可用
#列表可存储多种数据类型，用,分割
#直接创建
lst=[1,2,3,4,5,"hello1"]
print(lst)
#内置函数创建
list2=list(range(1,10,2))
lst3=list("heel")
print(list2)
print(lst3)
print('-'*10)
print(list2+lst3)
print(len(list2))
print(max(list2))
print(min(list2))
print(sum(list2))
print(list2.count(2))
#删除列表
#del(list2)

print("==="*4,"正常循环",1)
for item in list2:
  print(item)
print("==="*4,"枚举循环",2)
#枚举
for index,item in enumerate(list2):
  print(index,item)#index是序号，不是索引
print("--"*10,"修改索引")
for index,item in enumerate(list2,start=1):
  print(index,item)