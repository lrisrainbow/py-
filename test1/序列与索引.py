#正向递增

s='helloworld'
for i in range(0,len(s)):
    print(s[i],end='\t')
print()
print('--------------------')
#逆向索引
for n in range(-10,0):
    print(s[n],end='\t')
#切片操作
print()
print("切片操作-------------")
d=s[0:5:2]
print(d)
d=s[:5:2]
print(d)
d=s[5:]
print(d)
d=s[::]#全部省略默认打印该字符串，实际为[0:len(s):1]
print(d)

print("序列相乘操作----------------")
#序列的相乘操作
s="+"
print(s*10)
s="helloworld"
print("e"in s)
print("v" not in s)
#序列对象的方法
print("-"*10)
print(s.count("e"))
print(s.index("e"))
#内置函数的使用
print("+"*10)
print(max(s))
print(min(s))


