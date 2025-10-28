# # LOOPS IN PYTHON
# # Loops repeat a block of code until they hit a limit or condition.
# # They exist to save us from typing the same line 500 times.
# # Python gives us for-loops and while-loops.
# # 
print()
print("--- Loops in Python ---")

# The for-loop.
# A for-loop repeats for each element in a sequence (like a list or string).
import time 

animals = ["lamb", "sheep", "cow", "goose", "donkey" ]

print("\nOur animals:", animals)
print("\n--- For Loop: visiting each animal ---")

for animal in animals:
    print("Now petting a", animal)
    time.sleep(1.5)

    if animal == "sheep":
        print("Hi Shep!")

print("\nNow I have petted all the animals.")


for i in range(10):
    print("Counting:", i)

# range(start, stop, step)
print()
print("--- range() with start, stop, step ---")

for num in range(2, 11, 2):
    print("Even number:", num)
print("Loop ended. Evens appreciated.")

print("--- Iterating over strings ---\n")

fav_word = "Shenanigan"
letter_list = []

for letter in fav_word:
    print(letter, end="")
    letter_list.append(letter)
    print(letter_list)

print()

# ---------------------------------------------------------
# WHILE LOOPS
# ---------------------------------------------------------
# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 
# import time
# count = 0


#Challenge 1

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
number = input("Pick how many fruits:")
for fruit in fruits[number]:
    print("You picked:", fruit)