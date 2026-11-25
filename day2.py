#ask user for their name and greet them 
name = input("What's your name? ").strip().title()

#split the name into first and last name
first, last = name.split(" ")

#say hello to the user
print(f"Hello, {first}!")

#alot smaller than before 
