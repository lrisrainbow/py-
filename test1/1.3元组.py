#元组也属于序列，相关操作可实现
#元组不可变，没有增删改操作，只能获取元素，类似定长数组
#1.直接创建元组
t=('hello',[10,20,30],'python')
print(t)
#2.函数，对传入的对象操作变为元组，无论它是什么
t=tuple([10,20,30])#把这个列表对象变为元组
print(t)

#序列的方法
print('是否存在',(10 in t))
print('max,min',max(t),min(t))
print('sum',sum(t))
print('index',t.index(10))

#元组数据类型的变化
t=(10,20,30,[10,20,30])
print(t.__class__)
t=(10)
print(t.__class__)
t=(10,)
print(t.__class__)

#元组的遍历
t=('pt','aa','kk')
print(t[0])
t2=t[::]#元组属于序列，也能切片
print(t2)

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])
print()
for i in range(1,len(t)):
    print(t[i])
print()
for it,i in enumerate(t):
    print(it,i)