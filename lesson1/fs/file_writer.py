filename="file_writer.txt"
# w模式：只写，没有文件则创建，有则覆写，会清空之前内容
# r模式：只读
# r+模式：读写，没有文件则报错，增量写，不会清空之前内容
# a模式：附加模式，没有文件则创建，有则增量写，不会清空之前内容
with open(filename,'w') as fileObject:
    # content=fileObject.read()
    # print('before write:',content)
    fileObject.write("I love programming.")
    # content=fileObject.read()
    # print('after write:',content)

with open(filename,'a') as fileObject: 
    fileObject.write("I love programming2.") 
with open(filename,'a') as fileObject: 
    fileObject.write("I love programming3.") 

