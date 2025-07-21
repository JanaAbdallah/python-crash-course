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
