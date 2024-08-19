class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
         """初始化属性name和age"""
         self.name=name
         self.age=age

    def sit(self):
         """mock dog sit"""
         print(self.name.title(),"is now sitting.")

    def rollOver(self):
         """mock roll over"""
         print(self.name.title(),"rolled over.")


myDog=Dog("willie",15)
print("My dog's name is",myDog.name.title()+".")
print("My dog is",myDog.age, "years old.")
myDog.sit()
myDog.rollOver()
