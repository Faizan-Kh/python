# creating a set
fruits = {"apple", "banana", "cherry"}
print("before adding orange: ", fruits)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 1. Adding an element to the set
fruits.add("orange")
print("After adding orange:", fruits)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 2. Removing an element from the set
fruits.remove("banana")
print("After removing banana: ", fruits)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 3. Discarding an element from the set (won't raise an error if the element does not exist)
fruits.discard("pineapple")
print("After discarding 'pineapple' (not in set):", fruits)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 4. Checking for membership
is_cherry_in_set = "cherry" in fruits
print("Is 'cherry' in the set?", is_cherry_in_set)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 5. Finding the length of the set
set_length = len(fruits)
print("Length of the set:", set_length)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 6. Clearing all elements from the set
fruits.clear()
print("After clearing the set:", fruits)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 7. Union of two sets
fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"mango", "pineapple"}
union_set = fruits1.union(fruits2)
print("Union of fruits1 and fruits2:", union_set)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 8. Intersection of two sets
fruits3 = {"apple", "banana", "grape"}
intersection_set = fruits1.intersection(fruits3)
print("Intersection of fruits1 and fruits3:", intersection_set)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 9. Difference of two sets
difference_set = fruits1.difference(fruits3)
print("Difference of fruits1 and fruits3:", difference_set)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 10. Symmetric difference of two sets
symmetric_difference_set = fruits1.symmetric_difference(fruits3)
print("Symmetric difference of fruits1 and fruits3:", symmetric_difference_set)
