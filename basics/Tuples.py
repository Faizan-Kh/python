exampleTuple = ("avocado", "banana", "kiwi", "peach", "mango", "orange")

# Accessing a tuple
print(exampleTuple[1])
print(exampleTuple[:4])
print(exampleTuple[2:4])
print(exampleTuple[1:])
print(exampleTuple[-2])

print("---------------------------------------------------")
print("---------------------------------------------------")

# if condition for tuple
if "avocado" in exampleTuple:
    print("yes, there is an avocado in the tuple")
else:
    print("oops, there is no avocado here")

print("---------------------------------------------------")
print("---------------------------------------------------")

# converting a tuple to list
thisTuple = ("apple", "banana", "mango")
y = list(thisTuple)
y[1] = "kiwi"
thisTuple = tuple(y)
print(thisTuple)

print("---------------------------------------------------")
print("---------------------------------------------------")

# del thisTuple
# print(thisTuple)

print("---------------------------------------------------")
print("---------------------------------------------------")

newTuple = exampleTuple + thisTuple
multipliedTuple = newTuple * 2
print("New Tuple", newTuple)
print("Multiplied Tuple", multipliedTuple)
