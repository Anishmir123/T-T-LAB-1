//Python Program to Calculate the Area of a Triangle
a = int(input("Enter The Lenght of First Side: "))
b = int(input("Enter The Lenght of Second Side:"))
c = int(input("Enter The Lenght of Third Side: "))

p=a+b+c
s = p / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The Area of Triangle: ",area)



