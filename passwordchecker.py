username = input("Enter your username")
thePassword = input("Enter a password")
passwordLen = len(thePassword)
hidePassword = '*' * passwordLen
print("Hello" ,username, "your password" ,hidePassword, "is" ,passwordLen, "characters long")