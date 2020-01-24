birthdays = {'Alice': 'Apr 1', 'Bob' : 'Dec 12' , 'Carol' : 'Mar 4'}

while True:
    print('Enter a name. Enter nothing to quit')
    name = input()
    if name == '':
        break
    elif name == 'all':
        for k, v in birthdays.items():
            print('Name: ' + k + ' Birthday: ' + str(v))
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
            
        
        else:
            print('I do not have the birthday for ' + name)
            print ('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('New birthday added!')
        
    
