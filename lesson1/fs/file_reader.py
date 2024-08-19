import sys

print(sys.argv[0])

with open("digits.csv") as fileObject:
    content=fileObject.read()
    print(content)
    print(content.rstrip())

print("==================================")

with open("/Users/liz/Documents/code/learn-python/lesson1/fs/digits.txt") as fileObject:
    for line in fileObject:
        print(line.rstrip())  

print("==================================")

with open("/Users/liz/Documents/code/learn-python/lesson1/fs/digits.txt") as fileObject:
    lines=fileObject.readlines()
for line in lines:
    print(line.rstrip())  
linesStr=''
for line in lines:
    linesStr+=line.strip()
print(linesStr)

