# 列表
home=['bedroom','bathroom','kitchen']

print(home)
print(home[0])
print(home[-1])
print(home[-2])

home[0]='living room'
home[-1]='balcony'
print(home)

# 列表方法
print('append=',home.append('basement'))
print('insert=',home.insert(0,'study'))
print(home)

del home[1]
print(home)

print('pop=',home.pop())
print(home)
print('pop1=',home.pop(1))
print(home)

print('remove=',home.remove('balcony'))
print(home)


myList=[3,4,1,23]
print('len=',len(myList))
print('sorted=',sorted(myList))
myList.sort()
print('sort=',myList)
myList.reverse()
print('reverse=',myList)

# for 循环
fruits=["apple",'grapes']
print('====for循环====')
for fruit in fruits:
    print(fruit)
print('===============')

# 函数range
print('====函数range====')
for value in range(1,5):
    print(value)
print('=================')
print('list(range(1,5))=',range(1,5,2),list(range(1,5)))
print('list(range(1,5,2))=',list(range(1,5,2)))

# 列表解析
squares= [value**2 for value in range(1,11)]
print('squares=',squares)

# 列表切片
member=['Liz','Jade','Mary']
print('列表切片member[1:2]',member[1:2])
print('列表切片member[:2]',member[:2])
print('列表切片member[2:]',member[2:])

# 复制列表
newMember=member[:]
print('列表复制member[:]',newMember,)
newMember.append("Jane")
print('列表复制后append',newMember,"\nmember=",member)
