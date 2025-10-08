# Basic string creation and indexes:
greeting = "Hello"
first_name = "Ada"
print(greeting, first_name)

# 0 1 2 3 4 
# H e l l o
second_letter = greeting[1]
print(second_letter)

#Concatenation: 
message = greeting + " " + first_name + "!!!!"
print("Concatenated message:", message)

print()
#Splicing
word = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Range of letters (non-inclusive):", word[-7:-2])
print(word[:5])
print("Last seven letters:", word[-7:])
print("Step through every second character:", word[::2])
print("Reversed, stepping every third letter:", word[::-3])

## Built-in string functions

last_name = "Lovelace"
length = len(last_name)
print("Length of name:", length)

character = "spOngEBOB SQuarePaNts"
print("\nUppercase:", character.upper())
print("Lowercase:", character.lower())
print("Capitalized first letter:", character.capitalize())
print("Title Format:", character.title())

print()

#Find and replace text
sentence = "I'm a goofy goober"
new_sentence = sentence.replace("I'm", "You're")
print(sentence)
print(new_sentence)

# FORMATTED STRINGS IN PYTHON
# f-strings allow variables and expressions inside strings

print("\n--- Formatted Strings ---")

name = "Elijah"
age = 14
city = "Annandale"

print(f"Hello, my name is {name}. I'm {age} years old and live in {city}. ")

# f-strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

quote = input("Favorite quote ")
length_of_quote = len(quote)
print(f"Your quote is {length_of_quote} characters long")


# Challenge 2: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Output formatted name: Lovelace, Ada

print(f"{input("Enter your last name: ")}," + f" {input("Enter your first name: ")}")

#or

first = input("First?") 
last = input("Last?")
print(last + "," + first)





# Challenge 3: Word Mutation
# Ask for a word and print it backwards, in uppercase, and lowercase.
# Example output
# Enter a word: Python
# Uppercase: PYTHON
# Lowercase: python
# Backwards: nohtyP


#Challenge 3 Answer:
word = input("Chosen Word:")
print("My chosen word is" ,word)
print("Caps:" , word.upper())
print("Lowercase:" , word.lower())
print("Reverse:" , word[::-1])