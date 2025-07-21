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
# For Loops
# we have a built in func called range() it loops according to the number we pass to it so here we wrote 3 so it gonna loop 3 times
for num in range(3):
    print("Attempt")

for number in range(3):  # number is here is like the i "iterator" so we can print it
    print(f"Attempt : {number}")

# we can also do this
for numb in range(1, 4):  # here instead of looping starting from  0 , here we gave it a range from 1 till 4 means it will stop at 3 it will loop till numb is = 4 then it will end the loop
    # this going to print (.) numb+1 times
    print("Attempt", numb, (numb+1) * ".")

# we can do this
for i in range(1, 10, 2):  # here instead of looping starting from  0 , here we gave it a range from 1 till 10 , and we've paased antoher value as the 3rd argument and this is the step value , means each iteration it will add 2 not 1
    print("Attempt", i)

# Break
successful = False
for c in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")


# -----------------------------------------------------------------------------------------------------------------------------------
# Nested Loops

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")


# -----------------------------------------------------------------------------------------------------------------------------------
# range is a complex type
print(type(range(5)))  # it's type is range

# we can do this
for x in "Python":  # x is gonna be each char in python , here we iterate over python
    print(x)

# we can do this
for x in [1, 2, 3, 4]:  # we can iterate over each number in the list
    print(x)


# -----------------------------------------------------------------------------------------------------------------------------------
# while loops
# We've learned that we use for loops to iterate over iterable objects
# in python we have while loop and we use that to repeat smth as long as the condition is true

NUM = 100
while NUM > 0:
    print("YESSS")
    NUM = NUM//2


command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

# -----------------------------------------------------------------------------------------------------------------------------------
# Functions


def greet(firstname, lastname):  # def -> define
    print("Hi there")
    print(f"Welcome on board,{firstname}")


greet("Jana", "Abdallah")

# Types of Functions
# we have 2 types of functions -> function that perform a tas and func that calculates and return a value
# 1- Perform a task
# 2- Return a value


def get_greeting(name_):
    return f"Hi {name_}"


message = get_greeting("jana")
# we can write this message inside a file using open func
file = open("content.txt", "w")  # w -> opened for writing
file.write(message)
print(message)

# -----------------------------------------------------------------------------------------------------------------------------------
# Default Arguments
# we can make a specific argument as an optional argument, by making it have a default value


def increment(number, by=1):  # here we make the default value of by=1 , if the user doesn't change it
    return number+by


print(increment(6))

# -----------------------------------------------------------------------------------------------------------------------------------
# sometimes we need to create a function that takes a variable number of arguments


def multiply(x, y):
    return x*y

# but if we want pass mutliply(.,.,.,.) we will not able to do this bec it takes 2 args
# but if we make this multiply(*numbers)


def mult(*numbers):
    print(numbers)


mult(2, 3, 4, 5, 6, 7)

# using ** -> when we use ** we can pass to the func multiple key value pairs or multiple keyword args to a func and python will store them into a dictionary


def save_user(**user):
    print(user)


save_user(id=1, name="Jana", age=22)  # this will print a dictionary

# -----------------------------------------------------------------------------------------------------------------------------------
# Fizz-Buzz Problem
# if the input we got is divisible by 3, return "Fizz"
# if the input is divisible by 5, return "Buzz"
# if the input is divisible by both 3 and 5, return "FizzBuzz"
# otherwise, return the input number itself
# this is a common interview question to test the basic understanding of control flow and logic in programming


def fizz_buzz(input):
    input = int(input)  # ensure input is an integer
    input_str = "Fizz" if input % 3 == 0 else "Buzz" if input % 5 == 0 else str(
        input)
    return input_str


# testing the fizz_buzz function
print(fizz_buzz(15))  # should return "FizzBuzz"
print(fizz_buzz(9))   # should return "Fizz"
print(fizz_buzz(10))  # should return "Buzz"
print(fizz_buzz(7))   # should return "7"

# -----------------------------------------------------------------------------------------------------------------------------------


def multiplyyy(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
# this will print the multiplication of all numbers
print(multiplyyy(2, 3, 4, 5, 6, 7))
