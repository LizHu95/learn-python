import json

numbers=[2,4,1,4,5]
filename='number.json'
with open(filename,'w') as fObj:
    json.dump(numbers,fObj)

