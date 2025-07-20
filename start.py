import math

# Vars
x = 1
y = 1
unit_price = 3

# -----------------------------------------------------------------------------------------------------------------------------------
# print func

print("hello world")
print("*" * 10)

# len func -> we use it to know the length of a string
course = "programming"
print(len(course))

print(course[0])  # -> first character 0 indexed

# we can also use -ve index -> but what does it mean ?
# -> it prints the last char in the string -> in other terms it means that it returns the first char from the end of the string
print(course[-1])

# -----------------------------------------------------------------------------------------------------------------------------------
# SLICING

# we can Slice the string -> let's say we need to extract the 1st 3 chars in the strings
print(course[0:3])  # -> this is will print "pro"

# what fi we do this
# this will print from index 0 till the end , so it gonna print the exact same string as the original one
print(course[0:])

# this also gonna return the exact same string as the original
print(course[:])

print(course[:4])  # this gonna logical print from 0 till 4

# -----------------------------------------------------------------------------------------------------------------------------------
# what if we want to add "" inside the string ??
# Crs = "Programming " jana"
# print(Crs)  # this will not work

# so we are gonna use "\"  -> escape char
Crse = "programming \"pro"
print(Crse)

# \"
# \'
# \\ -> this is if we need to print \
# \n -> this is for new line


# -----------------------------------------------------------------------------------------------------------------------------------
# using concatination to build a string

first = "Jana"
last = "Abdallah"
full = first + " " + last
print(full)

# so we can use another better and new approach
FirstN = "Jana"
LastN = "Abdallah"
# it will be executed at run time so we can replace the value it doesn't have to be a constant value
FullN = f"{FirstN} {LastN}"
print(FullN)


# -----------------------------------------------------------------------------------------------------------------------------------
# String Methods
# Everything in python is an object and objects have methods

CRS = " Programming Lang "
print(CRS.upper())  # this print a new string so the old string will not be affected
print(CRS.title())  # captilize the 1st char of each word
print(CRS.strip())  # remove the space from the beginning and end of the string
print(CRS.lstrip())  # this remove the white space from the left of the string
print(CRS.rstrip())  # this remove the white space from the right of the string

# this will return the index of where we can find this substring inside the string
# if it returns -1 so this mean that this substring not found inside the string
print(CRS.find("Pro"))

# Python is a capital case sensitive language

print(CRS.replace("P", "J"))  # this will replace all P capital with J capital

# this check if this is inside the string or not , do we have Pro in CRS ?
print("Pro" in CRS)
print("Swift" not in CRS)  # this check if this is not in the CRS


# -----------------------------------------------------------------------------------------------------------------------------------
# in python we have 3 types of nums , int, float, complex nums
l = 1
g = 1.1
z = 1+2j

# we have 2 types of division ' / '  or ' // '
# / -> this if we made 3/4 it will print the float number as it
# // -> this is will print only the whole num part
print(10 / 3)
print(10 // 3)

# we use ** to make power operation
print(2 ** 4)

# we have spacial operator called  augmented assignment operator
v = 10
# we can make
v = v+2
print(v)
# or we can use this operator
v += 2
print(v)


# Useful functions to work with numbers
print(round(2.9))
print(abs(-2.9))

# we can use math module if we need to handle complex math operations and module is like a separate file with some python code
# so in python we have this math module which include lots of mathematical functions or working with nums
# import math -> so math in this program will be an object so we can use the . operator with it to use all methods it has
print(math.ceil(2.2))

# -----------------------------------------------------------------------------------------------------------------------------------
# Types Conversion
# we use input() func to get an input from the user
r = int(input("r:"))
h = r+1
# if we run this only the above code we will get an error
# bec when the user will input the num it will be string not and int so we have to convert it into int so we can use math operations on it
# without using int(input("r:")) it will still a string

# we can also make this
f = input("f:")
n = int(f)+1
print(n)
print(f"r: {r} , f: {n}")
# we have int(), float(), bool(), str()
# we can use type() func to know the var type
print(type(r))

# these are the false values meaning in python
# "", 0, None

# -----------------------------------------------------------------------------------------------------------------------------------
# Comparison operators (>, <, ==, <=, >=, !=)
# we have a built in func called -> ord() -> this will return the numeric representation of each char Ascii of each thing we use
print(ord('b'))

# -----------------------------------------------------------------------------------------------------------------------------------
# Conditions and Statements
temp = 35
if temp > 30:
    print("It's Warm")
elif temp > 20:
    print("It's nice ")
else:
    print("NONE")
print("DONE")

# we can make if and else using another quick way
mess = "Yes Sure" if temp > 30 else "No"   # ternary operator
print(mess)

# logical operators (and, or, not)
high_income = True
good_credit = True
student = True

if (high_income and good_credit):
    print("ELgible")
else:
    print("NotElgible")


if not student:
    print("NOt ELigible")
else:
    print("Eleee")


age = 22
if 18 <= age <= 40:
    print("Ppp")
# -----------------------------------------------------------------------------------------------------------------------------------
