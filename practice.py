import random
import math

a = 0
b = 5
c= 2

print(a + c)

print("Colin " + "Cirian") #CONCATENATION 

print(b/c)

print(abs(-20))
print(math.sqrt(64))
print(pow(9, 8))
print(random.random())
print(random.randrange(1, 10))

def abs_diff(num1, num2):
    return abs(num1 - num2)

result = abs_diff(-14, -9)
print(f"The absolute difference between -14 and -9 is: {result}")

print("Hello\nWorld")

print("Py" in "Python")

print("Python"[2])

print("Python"[2:5])

word = "python"

print(word.upper())

print(ord("Q"))
print(chr(20))

print("Hello, ", end="")
print("World!")

print("Hello", "World!", sep="-")

print("Hello, {}".format("World!") )

word = "Hello"
new_word = word.replace("H", "J")
print(new_word)

print(len("Colin " + "Cirian"))

empty_string = ""
print(type(empty_string))

print("He said, \"Hello, World!\"")

print("Colin" + " " + "Cirian")

print("Python-" *5 + "Python")

print("hello world my name is colin drake cirian".title())

list = [1, 2, 3, "Apple", "Banana", "Civic"]
print(list)

list[0] = "one"
print(list)

list.append("Hello person")
print(list)

tuple = ("civic", "m3 comp", "gt3rs", "typer")
print(tuple)

favorite_fruits = ["grapes", "strawberry", "pears"]

favorite_fruits.append("banana")
favorite_fruits.append("kiwi")

favorite_fruits.pop()

print(favorite_fruits)

my_empty_dict = {}

person = {'name': "colin", "age": "22", "lastname": "cirian"}

print(person["age"])

person["age"] = "23"
print(person["age"])

print(person.get("height"))

my_dict2 = {"name": "Jimmy", "favorite color": "blue"}
del my_dict2["favorite color"]
print(my_dict2)

my_empty_set = ()

my_set = {1, 2, 3, 4, 5}
my_set.add("hello")
my_set.remove(3)
print(my_set)

book_dict = {
    "title": "Python Programming",
      "author": "codeprowess",
        "year": 2023}

book_dict["year"] = 2024
print(book_dict)

my_movie_set = {"Godfather", "Spider-man", "Django", "Iron Claw", "Inception"} #SETS
my_movie_set.add("Inception")
print(my_movie_set)

colors = {"blue", "green", "red", "yellow", "purple", "pink"}
colors.add("green")
print(colors)

my_tuple = (1, 2, 3, 4, 5)
new_element = 6

new_tuple = my_tuple + (new_element,)
print(new_tuple)


#LIST NESTED INSIDE A LIST
my_nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_nested_list[0][1])
