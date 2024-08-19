from collections import OrderedDict

favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for key,val in favorite_languages.items():
    print(key.title()+"'s favorite languages is ",val.title()+".")