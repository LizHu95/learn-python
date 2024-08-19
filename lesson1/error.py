try:
    print(5/0) 
except ZeroDivisionError:
    print("You can't divide by zero!")

try:
    print(1+"sad")
except TypeError:
     print("You can't origize int and string!")

print("Give me two number, and i'll divide them.")
print("Enter 'q' to exit")
while True:
    num1=input("\nFirst number:")
    if num1 =='q':
        break
    num2=input("\nSencod number:")
    if num2 =='q':
        break

    try:
        answer=int(num1)/int(num2)
    except ZeroDivisionError:
        print("You can't divide by zero!")  
    else:
        print(num1 ,"/",num2,"=",answer)  
        