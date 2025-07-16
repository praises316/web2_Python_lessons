# Step 1: Weekly allowance
weekly_allowance = 2000
print("Weekly allowance:", weekly_allowance)

# Step 2: Money spent
weekly_allowance -= 400
money_spent = weekly_allowance
print("After spending 400, money left:", money_spent)

# Step 3: Money found under bed
money_found = 100
money_spent += money_found
money_under_bed = money_spent
print("After finding 100 under bed, total money:", money_under_bed)

# Step 4: Bought snacks
money_under_bed -= 250
buy_snacks = money_under_bed
print("After buying snacks for 250, money left:", buy_snacks)

# Step 5: Gave 25% to sibling (kept 75%)
balance_remaining = buy_snacks * 0.25
print("After giving 25% to sibling, remaining balance:", balance_remaining)

# Step 6: Bought data (1/3 of what's left)
data_cost = balance_remaining / 3
balance_after_data = balance_remaining - data_cost
print("Data cost (1/3 of balance):", data_cost)
print("After buying data, money left:", balance_after_data)

# Step 7: Split into 2 equal parts (savings and tithing)
savings_tithing = 38.0
print("Each of savings and tithing share:", savings_tithing)

# Step 8: Final balance using modulus
final_balance = 100 % savings_tithing
print("Final balance (100 % 38.0):", final_balance)

