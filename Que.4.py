#Write a program to enter P, T, R and calculate simple Interest

#take input
p = int(input('Enter the principal:'))
r = int(input('Enter the rate :'))
t = int(input('Enter the time :'))

#calculate simple interest
SI = (p * r * t) / 100

#display simple interest
print(f'Simple interest is {SI}')