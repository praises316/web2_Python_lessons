# Arithmetic Operators
# Plus +
# Minus -
# Multiplication *
# Division /
# Exponential **
# Modulus

'''first_number = 4
second_number = 5
sum = first_number + second_number
print(sum)

sub = first_number * second_number + second_number - first_number
print(sub)'''

firstNumber = 3
firstNumber += 5
print(f"Addition: {firstNumber}")

secondNumber = 10
secondNumber -= 3
print(f"Subtraction: {secondNumber}")

thirdNumber = 2 
thirdNumber *= 27
print(f"Multiplication: {thirdNumber}")

fourthNumber = 20 
fourthNumber /= 4
print(f"Division: {fourthNumber}")

fifthNumber = 12
fifthNumber //= 3
print(f"Floor Division: {fifthNumber}")

sixthNumber = 7
sixthNumber ** 4
print(f"Exponential: {sixthNumber}")

seventhNumber = 24
seventhNumber %= 5
print(f"Modulus: {seventhNumber}")



weekly_allowance = 2000
# money spent
money_spent = weekly_allowance - 400
print(money_spent)

# money found under bed

money_found = 100
money_under_bed = money_spent + money_found
print(money_under_bed)

# bought snacks

buy_snacks = money_under_bed - 250
print(buy_snacks)

# gave 25% to younger sibling

# twenty_five_percent = 25 / 100
# print(twenty_five_percent)
balance_remaining = buy_snacks * 0.75
print(balance_remaining)

# buy data
one_third_left = balance_remaining / 3
print(one_third_left)

# split into 2 savings and tithing
savings_tithing = one_third_left / 2
print(savings_tithing)

# final balance
final_balance = savings_tithing % 100
print(final_balance)
