
print()
print("--- Conditionals in Python ---")
# Boolean refresher:
print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4)
print(4 > 5)

print()
print()
print()
print()

# if
num1 = 10 
if num1 == 10: 
    print("Your number is equal to 10")

num2 = 13
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")
else: 
    print("Your number is greater than 12")

#if elif else

temperature = 93
if temperature >= 80: 
    print("It's hot!")
elif temperature >= 60:
    print("It's nice.")
else:
    print("It's cold!")

print()
print("--- Comparing Values with if/elif/else ---")

x = 20
y = 20

if x == y: 
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y: 
    print("x is less than y")
else: 
    print("error")

# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 
print()
print()
print()

age = 17
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

# Using 'or' and 'not'
print("--- Using 'or' --- ")

day = "Saturday"

if day is "Saturday" or  day is "Sunday":
    print("It's the weekend!")
elif day is "Monday" or day is "Tuesday" or day is "Wednesday":
    print("It's Monday or Tuesday or Wednesday")
else:
    print("It's Wed,Thur, or Fri")

if day is not "Monday":
    print("It's not Monday")

    #Challenge 1:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

    Password = 290835
    Entry = int(input("Enter your password: "))
print(type(Entry))
if Entry == Password:
    print("Access Granted")
else:
    print("Access Denied")