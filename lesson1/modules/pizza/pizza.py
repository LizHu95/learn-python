def makePizza(size,*topping):
    """describe pizza"""
    print("Making a "+ str(size)+"-inch pizza with the following toppings:")
    for topping in topping:
        print("-",topping)