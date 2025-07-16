# Question 1
print('''
Question 1:
Five main modes in Vim:
1. Normal mode – Allows navigation using ESC key
2. Insert mode – Allows editing (i, a, s, o, Insert key)
3. Command-line mode – Used to save, quit, etc. (e.g. :w, :q)
4. Visual mode – Used to highlight text for copy/paste
5. Ex mode – Advanced scripting/recording in Vim
''')

# Question 2
print('''
Question 2:
:set number – Shows line numbers
:20 – Goes to line 20
dd – Deletes current line
''')

# Question 3
print('''
Question 3:
To record a macro: Press 'qa' (record into register a)
To stop recording: Press 'q'
To replay macro: Use '@a' in normal mode
''')

# Question 4
print('''
Question 4:
'o' opens a new line below the current one and enters Insert mode.
'O' opens a new line above the current one and enters Insert mode.
''')

# Question 5
print('''
Question 5:
Use :! followed by the command
Example: :!ls
''')

# Question 6
print('''
Question 6:
Invalid: 2name (cannot start with number)
Valid: _userAge
Invalid: print (reserved keyword)
''')

# Question 7
state = "Plateau"
print("Question 7:")
print(state)
print(type(state))

# Question 8
print('''
Question 8:
camelCase: myFirstName
snake_case: last_name
PascalCase: MiddleName
''')

# Question 9
number = 12.4
numbers = 23.5
total = number + numbers
product = number * numbers
print("Question 9:")
print(total)
print(product)
print(type(product))

# Question 10
a = 5
b = 2
print("Question 10:")
print(a / b)
print(type(a / b))

# Question 11
first_name = "Praise"
last_name = "Dapal"
print("Question 11:")
print("My name is {} {}".format(first_name, last_name))
print(f"My name is {first_name} {last_name}")
print("My name is " + first_name + " " + last_name)

# Question 12
print("Question 12:")
print("Name:\tPraise\nLocation:\tPlateau")

# Question 13
print("Question 13:")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")
print(type(name))
print(type(age))
print(type(hobby))

# Question 14
print("Question 14:")
age = int("20")
price = float("505.5")
print(age, type(age))
print(price, type(price))

# Question 15
print("Question 15:")
is_married = input("Are you married? ") == "yes"
print(is_married)

# Question 16
print("Question 16:")
side = float(input("Enter side of the square: "))
area = side * side
print(f"Area: {area}")

# Question 17
print("Question 17:")
name = input("Enter full name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
hobbies = input("Enter your hobbies: ")
print("Summary of Inputs")
print("-----------------------")
print(f"Your name is {name}, you are {age} years old, your height is {height}, and your hobbies are: {hobbies}")

# Question 18
import time
print("Question 18:")
print("1. Open the microwave")
print("2. Put the rice")
print("3. Set the time")

customer = {}
username = input("Enter your name: ")
customer["username"] = username

duration = int(input("Duration (in minutes): "))
customer["duration"] = duration

amount = duration * 1200
customer["amount"] = amount

print(f"You will be charged #{amount:,.2f}")
print(f"{username}, your food will be ready in {duration} minutes.")
print("4. I will let you know when it is ready...")

minutes_in_seconds = 60
time.sleep(duration * minutes_in_seconds)

print("5. Your food is ready.")

