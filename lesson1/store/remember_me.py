import json

username=input("What's your name?")
filename='username.json'
with open(filename,'w') as fObj:
    json.dump(username,fObj)

