while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('PLease enter a number ')

while True:
    print('Select a new password')
    password = input()
    if password.isalnum():
        break
    print('only letters and numbers please ')
