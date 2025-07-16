#Get user input

('''
1. full_name variable stores the value of a users fullname

2. user_age variable stores the value of a users age 

3. user_height variable stores the value of a users height

4. user_hobbies variable stores the value of a users hobbies

5. isMarried stores the value of a users marital status

''')


#get user Full name
print("Hello,What is your name?")
print("Please enter your full name")
full_name = input("")
print(f"Full name : {full_name} (type: {type(full_name)})")

#get user Age
print("How old are you?")
print("Please enter your age here")
user_age = int(input(""))
print(f"Age: {user_age} (type:  {type(user_age)})")


#get user Height
print("Enter your height here")
user_height = float(input(""))
print(f"Height: {user_height} (type: {type(user_height)})") 


#get user Hobbies
print("What are your hobbies?")
print("enter your hobbies here")
user_hobbies = input("")


#get user marital status

marital_status = input("Are you married? Enter yes OR no \n")
is_married = marital_status == "yes"
print(f"Marital_Status: {is_married} (type: {type(is_married)})")



#User Detail Collected in summary

print("\n User details entered")

print(f"Name: {full_name}")
print(f"Age: {user_age}")
print(f"Height: {user_height}")
print(f"Hobbies: {user_hobbies}")
print(f"Married: {is_married}")





