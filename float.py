PI = 3.1415
print(f"The initial value of PI is {PI}")
print(f"The value of PI in one decimal place is {PI:.1f}")
print(f"The value of PI in two decimal places is {PI:.2f}")
print(f"The value of PI in three decimal places is {PI:.3f}")

height = int(input("Enter your height >>>>"))
print(f"Your height is: {height:.2f}")


Chelsea = 25 / 5
print(f"Chelsea odd: {Chelsea}")
Psg = 5 / 3
print(f"Psg odd: {Psg}")

acct_balance = 200000
print(f"Your account balance is #{acct_balance:.2f}")
account_bal = 120
print(f"Your account balance is #{account_bal:.3f}")

bio = "My name is Praise"
print(not "name" in bio)
print("name" not in bio , "Praise" in bio)
print("name" in bio)
print("Praise" not in bio)

# bio1 = "I am a "Programmer""

print("id|\t Name | \t Gender")
print("1.\t Praise | \t Female")
print("\a")


'''isMarried = input("")
print(isMarried.startswith("true"))'''

'''
bio2 = "Praise is a Programmer"
print(bio2.startswith("Praise"))'''

record = "James Abuja 150000.5 NGN0921"

print("Salary Slip")
print("---------------")
name = record[0:5]
#print(name) 
print("Name:",name[0].capitalize() + record[1:5])
initial = record[0:1]
print("Initial:",initial[0:1].capitalize())
ID = record[21:27]
print("ID:",ID)
valid_id = "YES"
print("Valid ID:",valid_id.startswith("YES"))
ValidId = "YES"
print("Valid ID:",ValidId)
monthly_salary = float(record[12:21])
print (f"Monthly Salary: {monthly_salary:,.2f}")

# Question 2
message  = "GhostNet#X44CR#98.654#TRC8821"
print("ALERT REPORT")
print("--------------")

code_name = message[0:8]
print("Code Name:",code_name)
message_code = message[9:14]
print("Message Code:",message_code)
last_letter = message[23:24]
print("Last Letter:",last_letter)
trace_ID = message[22:]
print("Trace ID:",trace_ID)
traceable = "Yes"
print("Traceable:",traceable)
security_level = message[15:20]
print("Security Level:",security_level)

print("Using Split Method")
print("****************")
decode_message = message.split("#")
print(decode_message)
name = decode_message[0]
print(f"Code Name: {name}")
code = decode_message[1]
print(f"Message Code: {code}")
last_character = decode_message[1][-1]
print(f"Last Letter: {last_character}")
trace_id = decode_message[3]
print(f"Trace Id: {trace_id}")
Traceable = decode_message[1]
print(f"Traceable: {Traceable}")
security = float(decode_message[2])
print(f"Security Level: {security}")


celebrities = "Davido-Wizkid-Rema-Runtown-Buju-Burna"
print(celebrities)
names_of_celebrities = celebrities.split("-")
print(names_of_celebrities)

name1 = names_of_celebrities[0][-3]
print(name1)

