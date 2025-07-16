# Initial allowance
allowance = 2000
print("Starting allowance: ₦", allowance)

# 1. Spent ₦400 on books
allowance -= 400
print("After buying books (₦400): ₦", allowance)

# 2. Found ₦100 under bed
allowance += 100
print("After finding ₦100: ₦", allowance)

# 3. Bought snacks worth ₦250
allowance -= 250
print("After buying snacks (₦250): ₦", allowance)

# 4. Gave 25% to sibling
allowance *= 0.75  # Keeping 75% means giving out 25%
print("After giving 25% to sibling: ₦", allowance)

# 5. Used one-third to buy data
allowance *= (2/3)  # Keeping 2/3 means using 1/3
print("After using one-third for data: ₦", allowance)

# 6. Split remaining between savings and tithing
savings = allowance / 2
tithing = allowance / 2
allowance -= (savings + tithing)
print("After splitting between savings and tithing: ₦", allowance)

# 7. Remove all complete ₦100 notes
allowance %= 100
print("Remaining after removing all ₦100 notes (₦100 %=): ₦", allowance)

