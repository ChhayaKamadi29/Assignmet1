#Write a program to enter P, T, R and calculate Compound Interest

#take input
p = float(input('Enter the p:'))
r = float(input('Enter the r:'))
t = float(input('Enter the t :'))

#calculate compound interest
A = p * (1 + r / 100) ** t
CI = A - p

#display Compound interest
print(f'Compound interest is {CI}')

