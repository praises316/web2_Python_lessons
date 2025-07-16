weekly_allowance = 2000
print("money spent")
print("*******")
money_spent = 400
weekly_allowance -= money_spent
print(money_spent)

print("money found under bed")
print("*********")
money_found = 100
weekly_allowance += money_found
print(weekly_allowance)

print("bought snacks")
print("************")
buy_snacks = 250
weekly_allowance -= buy_snacks
print(weekly_allowance)

print("gave 25% to younger sibling")
print("************")
give_sibling = (weekly_allowance * 0.25)
weekly_allowance -= give_sibling
print(weekly_allowance)

print("buy data")
print("************")
buy_data = 0.3333 * weekly_allowance
weekly_allowance -= buy_data
print(weekly_allowance)

print(" split into 2 savings and tithing")
print("*************")
savings_tithing =  2
weekly_allowance //= savings_tithing
print(weekly_allowance)

print(" final balance")
print("**************")
final_balance = 100
weekly_allowance %= final_balance
print(weekly_allowance)
