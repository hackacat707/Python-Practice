# calculator app

print('Welcome to the calculator')

shape = input('What shape would you like? C for circle, T for triangle')
if shape == 'C':
    print('Selecting circle')
    radius = float(input('Enter the radius of the circle'))
    area = 3.14159 * (radius ** 2)
    print(f'The area of the circle with radius {radius} is {area}')

elif shape == 'T':
    print('Selecting triangle')
    base = float(input('Enter the base of the triangle'))
    height = float(input('Enter the height of the triangle'))
    area2 = (base / 2) * height
    print(f'The area of the triangle is {area2}')
else:
    print("That's not a shape")
print('Exiting calculator, now')
