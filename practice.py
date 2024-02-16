import math
import random

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