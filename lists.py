# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.
print()
print("--- Lists in Python ---")

#initialize a list with brackets:
empty_list = []
empty_list.append("Thing")
print(empty_list)

animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print()
print()
print()

print("--- Indexing: how to access the elements of a list ---")
print("First Element:", animals[0])
print("Second element:", animals[1])
print("Last element:", animals[-1])

print()
print("--- Modifying Lists ---")
animals[0] = "babirusa"
print(animals)

animal_to_replace = animals.index("pangolin")
print(animal_to_replace)
animals[animal_to_replace] = "seamonkey"

# add element at end of list:
animals.append("glass frog")
print(animals)

# insert element at specific index
animals.insert(3, "aye-aye")
print("Inserted one animal:", animals)
animals.insert(1, "camel")
print("Inserted another animal:", animals)

animals.remove("babirusa")
print(animals)

last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)

print()
print("--- Useful List Functions ---")

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Original Numbers:", nums)

print("Length of list:", len(nums))
print("Max number:", max(nums))
print("Min number:", min(nums))
print("Sum of numbers:", sum(nums))

nums.sort()
print(nums)
animals.sort()
print(animals)

nums.reverse()
print(nums)

print()
print("--- Checking Membership ---")

if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list.")

print()
print("--- Copying Lists ---")

original_list = [1, 2, 3]
copied_list = original_list
copied_list = original_list.copy()
copied_list.append(4)
print(original_list)
print(copied_list)

print()
print("--- Nested Lists/The Matrix ---")

matrix = [  
    [1,2,3], 
    [4,5,6], 
    [7,8,9]  
    ] 

print(matrix[2][2])


print("\n--- Challenges ---\n")
#Challenge 1
numbers = [1, 2, 3, 4, 5, 6,]
usernumber = int(input("Gimme a number:"))
numbers[2] = usernumber
print(numbers)

#Challenge 2
shopping = []
shopping.append("milk")
shopping.append("eggs")
shopping.append("bread")
mychoice = ("PS Giftcard")
shopping[1] = mychoice
shopping.remove("eggs")