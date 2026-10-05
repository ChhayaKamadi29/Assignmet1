#Write a Program to input two angles from user and find third angle of the triangle

#take input

a1 = int(input('Enter the angle 1 :'))
a2 = int(input('Enter the angle 2 :'))

#calculate angle
a3 = 180 - (a1 + a2)

#display third angle
print(f'Third angle of triangle is {a3}')
