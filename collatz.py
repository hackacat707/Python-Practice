import sys

def collatz(number):
    print ("You have entered the number " +str(number))
    if number % 2 == 0:
        print ("This number is even")
        print ("Here's the output: " +str(number // 2))
        return number // 2
        
    elif number % 2 == 1:
        print ("This number is odd ") 
        print ("Here's the output: " + str(3 * number + 1))
        return 3 * number + 1
    
nums = input("Please enter a number ")
while nums !=1:
        nums = collatz(int(nums))


