catNames = []
while True:
    print ('Enter a name of a cat' +str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name =='':
        break
    catNames = catNames + [name]
print ('The cats are: ')
for name in catNames:
    print('   ' + name)
