# List
letters = ["a", "b", "c", "d", "e"  "f", "g", "h", "i", "j"]

# We can have a list of lists
nested_list = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j"]
]

matrix = [
    [0, 1],
    [2, 3]
]

# we can make a matrix of 100
zeros = [0]*100
print(zeros)  # this will print a list of 100 zeros

# we can use range in list
numbers = list(range(11))  # this will create a list of numbers from 0 to 10

# we can use the len func to know the lenght of a list
print(len(numbers))  # this will print the length of the list

# We can also have a list of dictionaries
nested_dict = [
    {"name": "Jana", "age": 22},
    {"name": "John", "age": 30},
    {"name": "Doe", "age": 25}
]

# we can also have a list of tuples
nested_tuple = [
    ("a", "b", "c"),
    ("d", "e", "f"),
    ("g", "h", "i"),
    ("j",)
]

# We can also have a list of sets
nested_set = [
    {"a", "b", "c"},
    {"d", "e", "f"},
    {"g", "h", "i"},
    {"j"}
]

# -----------------------------------------------------------------------------------------------------------------------------------
# Accessing items in a list

Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
Letters[0]  # this will print "a"

# Slicing in a list is like in a string
print(Letters[0:3])  # this will print ["a", "b", "c)

# we can pass the step , like if you need to go over the list but by every 2 items for an example
Letters[::2]  # this will print ["a", "c", "e", "g", "i"]

# if we do this
# this will print the list in reverse order ["j", "i", "h", "g", "f", "e", "d", "c", "b", "a"]
Letters[::-1]

# -----------------------------------------------------------------------------------------------------------------------------------
# Unpacking Lists
# if we hvae
Numbers = [1, 2, 3, 4, 5]

# and we want to add vars to it so how we can do it?
a, b, c, d, e = Numbers  # this will unpack the list into
# a = 1, b = 2, c = 3, d = 4, e = 5
# but the numbers of the list should be equal to the number of variables we have
# if we have more variables than the list, we will get an error
# if we have less variables than the list, we will get an error too

# what if we want to unpack specific items from the list like the first and the second items , we dont need the rest , so what we can do?
a, b, *rest = Numbers  # this will unpack the first two items into a
# a = 1, b = 2, rest = [3, 4, 5]

# this will unpack the first item into a, the last item into last, and the rest into other
a, *other, last = Numbers
# a = 1, other = [2, 3, 4], last = 5


# -----------------------------------------------------------------------------------------------------------------------------------
# Looping over lists
Num = [1, 2, 3, 4, 5]

for num in Num:
    print(num)  # this will print each number in the list

# -----------------------------------------------------------------------------------------------------------------------------------
# If we want to add items to a list
# Add
Nums = [1, 2, 3, 4, 5]
Nums.append(6)  # this will add 6 to the end of the list

# If we want to add an item in a specific index we use insert
Nums.insert(2, 7)  # at index 2 it will add 7
Nums.insert(0, "Jana")  # this will add 0 at the start of the list
print(Nums)  # this will print [Jana, 1, 2, 7, 3, 4, 5, 6]
# List or any other DS can hold different types of data at once

# Remove
Nums.pop()  # this will remove the last item in the list
Nums.pop(2)  # this will remove the item in index = 2 in the list
Nums.remove(7)  # this will remove the first occurrence of 7 in the list

# we can also delete an item using del statement
del Nums[0]  # this will delete the first item in the list
# del Nums  # this will delete the whole list
# we can use clear to remove all items in the list
# Nums.clear()  # this will remove all items in the list

# -----------------------------------------------------------------------------------------------------------------------------------

# Finding items in a list
Nums = [1, 2, 3, 4, 5]
# this will print the index of the first occurrence of 3 in the list
print(Nums.index(3))
# if we want to find the index of the last occurrence of an item in the list, we can use rindex
# this will print the index of the first occurrence of 3 in the list from index 0 to index 3
print(Nums.index(3, 0, 3))

if "d" in Nums:  # this will check if "d" is in the list
    print("d is in the list")

Nums.count(3)  # this will count the number of occurrences of 3 in the list

# -----------------------------------------------------------------------------------------------------------------------------------
# Sorting a list

Nums = [5, 2, 3, 1, 4]
Nums.sort()  # this will sort the list in ascending order
print(Nums)  # this will print [1, 2, 3, 4, 5]
Nums.sort(reverse=True)  # this will sort the list in descending order
print(Nums)  # this will print [5, 4, 3, 2, 1]

# we have a built in function called sorted that can sort any iterable
# this will sort the list in ascending order , but this will not change the original list
sorted_nums = sorted(Nums)
print(sorted_nums)  # this will print [1, 2, 3, 4, 5]

# -----------------------------------------------------------------------------------------------------------------------------------
# Map Function
items = [
    ("Jana", 22),
    ("John", 30),
    ("Doe", 25),
]

# currently each item in this list is a tuple

ages = []

for item in items:
    # this will append the age of each item to the ages list
    ages.append(item[1])
print(ages)  # this will print [22, 30, 25]

# By this way we mapped our list into a new list of ages
# but we have anther way to do this using the map function
age_list = map(lambda item: item[1], items)  # this will return a map object
print(list(age_list))  # this will print [22, 30, 25]

# -----------------------------------------------------------------------------------------------------------------------------------
# Filter Function
# if we want to filter the items in the list based on a condition
filter(lambda item: item[1] > 25, items)  # this will return a filter object
# -----------------------------------------------------------------------------------------------------------------------------------
# We have in python a comprehension syntax that allows us to create lists, sets, and dictionaries in a more concise way
# List Comprehension

Items = [
    ("Jana", 22),
    ("John", 30),
    ("Doe", 25),
]
# [expression for item in Items ]  # this is the syntax of list comprehension
# this will create a list of ages from the items list
Ages = [item[1] for item in Items]
# instead of using the map function we can use list comprehension
print(Ages)  # this will print [22, 30, 25]


# We can achieve filter using comprehension as well
# this will create a list of items where the age is greater than 25
filtered = [item for item in items if item[1] > 25]
# this will print [('John', 30)]
print(filtered)
