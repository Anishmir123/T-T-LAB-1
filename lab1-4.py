import cmath

a = int(input("Enter the Number (a!=0):"))
b = int(input("Enter the Number b:"))
c = int(input("Enter the Number c :"))

d = (b**2) - (4*a*c)

root1=(-b-cmath.sqrt(d))/2*a
root2=(-b+cmath.sqrt(d))/2*a

print("Enter The Root :",root1,"and",root2)