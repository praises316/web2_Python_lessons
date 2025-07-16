# Question 1: Area and Perimeter

length_of_rectangle = int(input("enter length of a triangle>>>>\n"))
width_of_rectangle = int(input("enter width of a triangle>>>>\n"))

calculate_area = length_of_rectangle *  width_of_rectangle
calculate_perimeter = length_of_rectangle + width_of_rectangle

print(f"Area = {calculate_area:,.2f}")
print(f"Perimeter = {calculate_perimeter:,.2f}")


# Question 2: Magic Number

my_age = 25
pi = 3.14159

result = ((my_age * 2 + pi) % 5) ** 2

print(result)
print(type(result))

# Question 3: String Slicing Challenge

code = "PythonIsAmazing"

code1 = code[0:6]
code2 = code[6:]
code3 = code[-1::-1]
code4 = code[::3]

print(code)
print(code1)
print(code2)
print(code3)
print(code4)

# Question 4: Secret Message Parser

message = "GhostNet#X44CR#98.654#TRC8821"

code_name = message[0:8]
message_code = message[9:14]
security_level = message[15:20]
trace_id = message[22:]
print(code_name)
print(message_code)
print(security_level)
print(trace_id)

# Question 5: Salary Slip Formatter

record = "Grace Lagos 175000.75 NGN7722"
name = record[0:5]
print(f"Name: {name}")
city = record[6:11]
print(f"City: {city}")
salary = float(record[12:21])
print(f"Salary: {salary:,.2f}")
ID = record[22:]
print(f"ID: {ID}")

# Question 6: String Membership and Boolean

bio = "My name is Dapal"

name = "name" in bio, "Dapal" in bio
print(name)

# Startswith Practice

isMarried = input("Are you married? (true/false): ")

print(isMarried.startswith("t"))

# Question 8: Odd or Even Checker

number = input("enter a number to check whether it's 
