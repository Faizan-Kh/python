list1 = ["apple", "banana", "cherry"]
# print(thisList)
list2 = [1, 4, 6, 7, 5]
list3 = [True, False, True]

print("---------------------------------------------------")
print("---------------------------------------------------")

# sorting a list
thisList = ["dragon fruit", "apple", "banana", "cherry", "mango", "papaya"]
thisList.sort()
print("Sorter List: ", thisList)

print("---------------------------------------------------")
print("---------------------------------------------------")

# joining 2 lists
list4 = list1 + list2
print("Joined List: ", list4)

print("---------------------------------------------------")
print("---------------------------------------------------")

# appending list2 in list1
for x in list2:
    list1.append(x)
print("Appending List 2 in List 1: ", list1)

print("---------------------------------------------------")
print("---------------------------------------------------")

# adding list2 to the beginning of list3
list3.extend(list2)
print("Extend function: ", list3)

print("---------------------------------------------------")
print("---------------------------------------------------")

list1.copy()


