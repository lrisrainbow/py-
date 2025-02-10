#列表属于序列，所有对序列的操作，运算均可用
#列表可存储多种数据类型，用,分割
#直接创建
import random

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

print("列表操作")
lst.append(888)#尾部增加
print(lst)
lst.insert(2,888)#指定位置加入
print(lst)
l=lst.pop(3)#指定index的取出后删除
print(lst)
print(l)
lst.remove(888)#第一次 出现888时删除该元素
print(lst)
lst.reverse()#反转列表
print(lst)

#列表生成式及二维列表
print('#'*20)
lst=[item for item in range(1,10)]
print(lst)
lst=[item*item for item in range(1,10)]
print(lst)
lst=[random.randint(1,10) for i in range(1,10)]
print(lst)

#从列表中选择元素组成新的列表
lst=[i for i in range(1,10) if i%2==0]
print(lst)

#二维列表
#1.直接创建
lst=[['a','b'],['c','d'],['1','2']]
print(lst)
for item in lst:
   for i in item:
     print(i,end='\t')
   print()
#列表生成式
lst=[[j for j in range(1,8)]for i in range(1,10)]
for item in lst:
  for i in item:
    print(i,end='\t')
  print()

