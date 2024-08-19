import json

filename='username.json'
with open(filename,'r') as fObj:
    username=json.load(fObj)
print("Welcome back,",username,"!")

