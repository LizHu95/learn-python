def makePizza(*toppings):
    """print all toppings ordered by consumer"""
    """*topping 一个星号会生成元组，将传入所有值存在这个元组里"""
    # 形参不可以不修改，下面会报错
    # toppings[0]="test"
    print(toppings)

makePizza("pepperoni")
makePizza("mushrooms","green peppers")

