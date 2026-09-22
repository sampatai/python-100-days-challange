import random
# fruits=["Apple","Peach","Orange"]
# for fruit in fruits:
#     print(fruit)

# scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
# total_exam_score=sum(scores)
# print(total_exam_score)
# total=0
# for number in range(1,101):
#     total +=number
#     print(total)

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '+', '=', '[', ']', '{', '}', ';', ':',
    ',', '.', '/', '<', '>', '?'
]
print("Welcome to the password generator!")

nr_letter=int(input("How many letters would you like in your password ?\n"))
nr_symbol=int(input("How many symbols would you like  ?\n "))
nr_number=int(input("How many numbers would you like ?\n"))
#Easy Level

# password=""
#
# for char in range(0,nr_letter):
#     random_char=random.choice(letters)
#     password += random_char
#
# for char in range(0,nr_symbol):
#     random_char=random.choice(symbols)
#     password += random_char
#
# for char in range(0,nr_number):
#     random_char=random.choice(numbers)
#     password += random_char

    # print("Your password is: ", password)


password_list=[]

for char in range(0,nr_letter):
    password_list.append(random.choice(letters))

for char in range(0,nr_symbol):
    password_list.append(random.choice(symbols))
for char in range(0,nr_number):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)


password = "".join(password_list)
print(password)

