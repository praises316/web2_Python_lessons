# Question 1

# my_age variable stores the value of my actual age an integer
my_age = 22

# pi variable stores the value of the constant number(value) of piand it is a float number.

pi = 3.14159
# magic_number stores the value of the sum of my_age and pi with some values added seperately.
magic_number = my_age * 3 + pi % 7
magic_number1 = (my_age * 3 + pi) % 7

print(magic_number)
print(magic_number1)
print(type(magic_number))
print(type(magic_number1))


# Question 2

# secret_word variable stores the value of a string "PythonIsAmazing"
'''
0    1    2    3    4    5    6   7  8  9  10 11  12  13  14
P    y    t    h    o    n    I   s  A  m  a  z   i   n   g
-15 -14  -13  -12  -11  -10  -9  -8 -7 -6 -5 -4  -3  -2  -1
'''

secret_word = "PythonIsAmazing"
# This line prints only the first word "Python"
secret_word1 = (secret_word[0:6])
print(secret_word1)

# This line prints the last 7 charaters of the string "isAmazing"
secret_word2 = (secret_word[-7:])
print(secret_word2)

# This line prints the middle word "Is"
secret_word3 = (secret_word[6:8])
print(secret_word3)

# This line prints the whole string in a reversed manner "gnizamAsInothtyP"
secret_word4 = (secret_word[-1::-1])
print(secret_word4)

secret_word10 = (secret_word[::-1])
print(secret_word10)

# This line prints every second character in the string "yhnsmzn"
secret_word5 = (secret_word[::-5])
print(secret_word5)

secret_word9 = (secret_word[-15::2])
print(secret_word9)

# Question 3

secret_word6 = "Python"
first_word = secret_word6.upper()
print(first_word)


secret_word7 = "IsAmazing"
second_word = secret_word7.lower()
print(second_word)


secret_word8 = first_word + second_word
print(secret_word8)

