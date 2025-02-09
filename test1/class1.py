
# for i in range(10):
#     print(i)

# print('请输入等级')
# grade=input()
# match grade:
#     case 'A':
#         print('a')
#     case 'B':
#         print('b');
# 
# print('结束')

# arry1 = [1,2,3,4,5,6,7,8,9]
# str1='hello'
# for i in range(3,len(str1)):
#     print(str1[i])
# for index,item in enumerate(str1,start=3):
#     print(index,item)

# list2=list(range(10))
# print(list2)
# list2.reverse()
# print(list2)
# list2.insert(5,1)
# print(list2)
# list2.sort()
# print(list2)
# list2.pop()
# print(list2)
# list2.append(2)
# print(list2)

# a2=(1,2,3,4,5,[1,2,3,4,5])
# i=len(a2)
# for j in range(0,len(a2)):
#     print(a2[j])

a1=(1,2,'a',4)
a2=(1,2,3,4)
i=zip(a1,a2)
i=dict(i)
print(i)

list2=[1,2,3]

i=zip(list2,a1)

print(i)

i=dict(i)
print(i)