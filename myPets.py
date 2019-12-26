myPets = ['Pooka', 'Kitty', 'Fat-tail']
print ('Enter a pet name')
name = input()
if name not in myPets:
    print('I dont have this pet named ' + name)
else:
    print(name + ' is my pet.')
