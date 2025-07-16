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
print(f"The sum of the addition from the two numbers is equal to {sum}")
print(f"{firstNumber} + {secondNumber} = {sum}")

print("***************")
print("Subtraction")
print("Enter two numbers to subtract")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
sub = float(firstNumber) - float(secondNumber)
print(f"The sum of the addition from the two numbers is equal to {sum}")
print(f"{firstNumber} - {secondNumber} = {sub}")

print("*******************")
print("Multiplication")
print("Enter two numbers to multiply")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
Multiplication = float(firstNumber) * float(secondNumber)
print(f"The sum of the addition from the two numbers is equal to {sum}")
print(f"{firstNumber} * {secondNumber} = {Multiplication}")

print("*******************")
print("Multiplication")
print("Enter two numbers to divide")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
Division = float(firstNumber) / float(secondNumber)
print(f"The sum of the addition from the two numbers is equal to {sum}")
print(f"{firstNumber} / {secondNumber} = {Division}")

print("*******************")
print("Exponential")
print("Enter two numbers to get the exponintial")
firstNumber = input("First Number:")
secondNumber = input("Second Number:")
Exponential = float(firstNumber) ** float(secondNumber)
print(f"The sum of the addition from the two numbers is equal to {sum}")
print(f"{firstNumber} ** {secondNumber} = {Exponential}")

