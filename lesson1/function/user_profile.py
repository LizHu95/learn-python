def buildProfile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    """使用任意数量的关键字实参"""
    """形参**user_info中的两个星号创建一个名为user_info的空字典，并将收到的所有健值对都封装到这个字典中"""
    profile={}
    profile['first']=first
    profile['last']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

print(buildProfile("liz", 'hu',age=28,interst=["guitar","reading"]))