store=['pastramin','pastramin','pastramin']

while store:
    result=input('Do you want to bug pastramin?(yes/no)')
    if result == 'yes':
        store.pop()
    else:
        continue
    print('pastramin is sold, storage is',len(store))
