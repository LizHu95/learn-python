import json

filename='number.json'
with open(filename,'r') as fObj:
    numbers=json.load(fObj)
print(numbers)

