#Write a program to calculate the percentage of student based on marks of any 5 subjects.

#Take input

mark1 = int(input('Enter the marks of 1st :'))
mark2 = int(input('Enter the marks of 2nd :'))
mark3 = int(input('Enter the marks of 3rd :'))
mark4 = int(input('Enter the marks of 4th :'))
mark5 = int(input('Enter the marks of 5th :'))

#Calculate  total
total = mark1 + mark2 + mark3 + mark4 + mark5

#calculate percentage
Percentage = (total / 500) * 100

#Display percentage
print(f'Percentage of best 5 is {Percentage}.')


