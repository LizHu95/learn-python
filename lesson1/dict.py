# dictionary: like object in java
alient0={'color':"green",'points':'5','oldName':"liz"}
print(alient0['color'],alient0['points'])
alient0['position']=[1,2]
print(alient0)
del alient0['oldName']
print(alient0)

# Traversal dictionary key and value
for key,value in alient0.items():
    print(key+":",value)

# Traversal dictionary key 
for key in alient0.keys():
    print(key)

# Traversal dictionary value 
for val in alient0.values():
    print(val)