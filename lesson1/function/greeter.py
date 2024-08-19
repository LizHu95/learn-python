def greet_user(firstname='jade',lastname='Ma'):
    """显示简单的问候语"""
    print("Hello!",firstname.title(),lastname.title())

greet_user(lastname="hu",firstname='liz')
greet_user('liz',"hu")
greet_user()