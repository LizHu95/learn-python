ages = [12,70,23]
for age in ages:
    if age >20 and age <=50:
        print(str(age)+'岁在20～50之间')
    elif age <=20:
        print(str(age)+'岁小于20岁')
    else:
        print(str(age)+'岁大于50岁')


members =['liz','mary','jade']
if 'jane' not in members:
    print('jane不是会员')


# 空列表布尔值是false
intersts = []
if intersts:
    print('我的兴趣爱好是',intersts)
print('我没有兴趣爱好')
intersts = ['game','guitar','tv']
for interst in intersts:
    print('My interst is',interst)