import cmath

#take input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

#calculate discriminant
d = b**2 - 4*a*c

#calculate roots
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

#display roots
print("Root 1 =", root1)
print("Root 2 =", root2)