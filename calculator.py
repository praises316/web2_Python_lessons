# A simple calculator app
print('''
1. Addition
2. Subtraction
3. Multiplication
4. Division
************************
''')
print("Enter two numbers to add")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
sum = float(firstNumber) + float(secondNumber)
print(f"The sum of the addition from the two numbers is equal to {sum:.2f}")
print(f"{firstNumber} + {secondNumber} = {sum:.2f}")

print("***************")
print("Subtraction")
print("Enter two numbers to subtract")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
sub = float(firstNumber) - float(secondNumber)
print(f"The result of the subtraction from the two numbers is equal to {sub:.2f}")
print(f"{firstNumber} - {secondNumber} = {sub:.2f}")


print("*******************")
print("Multiplication")
print("Enter two numbers to multiply")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
Multiplication = float(firstNumber) * float(secondNumber)
print(f"The result of the multiplication from the two numbers is equal to {Multiplication:.2f}")
print(f"{firstNumber} * {secondNumber} = {Multiplication:.2f}")

print("*******************")
print("Multiplication")
print("Enter two numbers to divide")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
Division = float(firstNumber) / float(secondNumber)
print(f"The result of the division from the two numbers is equal to {Division:.2f}")
print(f"{firstNumber} / {secondNumber} = {Division:.2f}")

print("*******************")
print("Exponential")
print("Enter two numbers to get the exponintial")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
Exponential = float(firstNumber) ** float(secondNumber)
print(f"The result of the exponential from the two numbers is equal to {Exponential:2f}")
print(f"{firstNumber} ** {secondNumber} = {Exponential:.2f}")

print("*******************")
print("Floor Division")
print("Enter two numbers to divide with floor division")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
floor_division = float(firstNumber) // float(secondNumber)
print(f"The result of the exponential from the two numbers is equal to {Exponential:2f}")
print(f"{firstNumber} // {secondNumber} = {floor_division}")

