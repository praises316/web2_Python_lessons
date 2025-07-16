print ("Sting data type")

name = "Tom"
print(type(name))

names = ("1111")
print(type(names))

name  = "My name is Praise"
age = "Fifteen"
favoriteColor = "Red"

print(name)
print(age)
print(favoriteColor)

nationality = str(True)
localGovernment = str(False)
religion = str(None)


print(nationality)
print(localGovernment)
print(religion)


Bio = '''
1. Praise
2. Fifteen
3. Red
4. Nigerian
5. Mangu
6. Christianity
'''

print(Bio)


myBio = "Programmer"
print(len("Programmer"))
print(myBio[4])

print("Blockfuse index")
companyName = "Blockfuse"
print(len("Blockfuse"))
print(companyName[0])
print(companyName[1])
print(companyName[2])
print(companyName[3])
print(companyName[4])
print(companyName[5])
print(companyName[6])
print(companyName[7])
print(companyName[8])

print("Slicing in python")

greeting = "Hello, world"

print(greeting[0:3])
print(greeting[1:5])
print(greeting[6:])
print(greeting[1:9])

fullName = "Praise Dauda Dapal"

firstName = fullName[0:6]
middleName = fullName[7:12]
lastName = fullName[13:18]

print(fullName)
print(firstName)
print(middleName)
print(lastName)

quote = "Five slice of bread"
chain = "blockchain"
number = 50
total = 1

firstSlice = quote[0:4]
secondSlice = quote[5:10]
thirdSlice = quote[11:14]
fourthSlice = quote[14:]


print(firstSlice)
print(secondSlice)
print(thirdSlice)
print(fourthSlice)



total = len(chain) + number + total
print(total)

technology = "Blockchain"

chain1= technology[-3:-1]
chain2 = technology[-10:]

print(chain1)
print(chain2)

bio = "Programmer"

pro = bio[-10:-7]
grammer = bio[-7:]
print(pro)

upperCase = (pro.upper())
print(upperCase)

lowerCase = (pro.lower())
print(lowerCase)


upperCase2 = (grammer.upper())
print(upperCase2)

lowerCase2 = (grammer.lower())
print(lowerCase2)

# This line of capitalizes the first letter of the first word
word = "python"
print(word)
print(word.capitalize())


word3 = "python"
word4 = "python"
word3 = word3[0].upper() + word3[1:]
print(word3[0:1].upper() + word3[1:])
print(f"{word4[0].upper()}{word4[1:]}")
print("{}{}".format(word4[0].upper(),word4[1:]))
print(word3)
print(word4)


'''
 0   1   2   3   4   5   6   7  8  9 10 11 12  13  14
 u   s   e   r   @   d   o   m  a  i  n  .  c   o   m
-15  -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3  -2  -1
'''
email = "user@domain.com"
email1 = (email[0:5])
email2 = (email[5:])
print("{}{}".format(email1,email2))

status = "single"
word_length = len(status) // 2
first_half = status[:word_length]
second_half = status[word_length:]
status1 = (status[0:3])
status2 = (status[3:])
print(status1,status2)
print(first_half,second_half)
