# print "This python script acts as a micro-wave"
import time
print('''("*************")
 ("Cohort III MIcro-wave")
("*************")
("1. Open The Micro-wave")
("2. Put the Rice")
("3. Set the Time")
''')
customer = {}
username = input("Enter your name: \n>>>")
customer["username"] = username
time_to_micro_wave = int(input("Duration: \n>>>"))
convert_to_int= float(time_to_micro_wave)
customer["duration"] = convert_to_int
price_to_pay = convert_to_int * 1000
customer["amount"] = price_to_pay
print("You are charge: #", price_to_pay, "only")
print(" Your rice will be ready in {} mins(s) {}".format(convert_to_int,username))
print(f"Your Rice wil be ready in {convert_to_int} min(s) {username}")
print("4 I will let you know when it is ready...")
minutes_in_seconds =60
time.sleep(time_to_micro_wave * minutes_in_seconds)
print("5 Your food is ready.")
