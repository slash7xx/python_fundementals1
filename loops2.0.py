while count < 5: 
    print(f"Loopin'. We are on loop # {count}.")
    count += 1
    time.sleep(0.5)

print("We have escaped the loop!")

user_input = ""

while user_input != "exit":
    user_input = input("Type 'exit' to escape:")