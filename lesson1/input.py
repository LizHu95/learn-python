# input 输入的是字符串
msg = input('please input your name:')
print("hello",msg)

age = input('please input your age:')
if int(age) >=18:
    print("你成年了")
else:
    print("你未成年")