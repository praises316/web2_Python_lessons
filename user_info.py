# Prompt for full name
print("Enter your full name:")
full_name = input()
print(f"Full name: {full_name} (type: {type(full_name)})")

# Prompt for age
print("Enter your age:")
user_age = int(input())
print(f"Age: {user_age} (type: {type(user_age)})")

# Prompt for height
print("Enter your height (in meters):")
user_height = float(input())
print(f"Height: {user_height} (type: {type(user_height)})")

# Prompt for marital status
print("Are you married? (yes/no):")
marital_input = input().strip().lower()
is_married = True if marital_input == "yes" else False
print(f"Married: {is_married} (type: {type(is_married)})")

# Prompt for hobbies
print("What are your hobbies?")
user_hobbies = input()
print(f"Hobbies: {user_hobbies} (type: {type(user_hobbies)})")

# Final summary
print("\n----- SUMMARY -----")
print(f"Name: {full_name}")
print(f"Age: {user_age}")
print(f"Height: {user_height} meters")
print(f"Married: {is_married}")
print(f"Hobbies: {user_hobbies}")

