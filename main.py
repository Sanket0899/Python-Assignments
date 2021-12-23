#1.	Write a Python program to print "Hello Python"?
print("Hello Python")
#2.	Write a Python program to do arithmetical operations addition and division.?
def add_div(a,b):
    add=a+b
    div=a/b
    return add,div

print(add_div(4,2))

#3.	Write a Python program to find the area of a triangle?
def area_triangle(BASE,HEIGHT):
    area=0.5*BASE*HEIGHT
    return area

print(area_triangle(5,4))

#4.	Write a Python program to swap two variables?

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b

    return(a,b)

a,b=swap(10,12)
print("a and b after swapping are a={a} b={b}".format(a=a,b=b))

#5.	Write a Python program to generate a random number?!

import random
print(random.randint(0,10))


