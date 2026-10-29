# ==============================
# Integer Data Type
# ==============================
print(-10)
print(11)
print(12)
print(13)
print(14)


# ==============================
# Float Data Type
# ==============================
print(-10.5)
print(11.5)
print(12.5)
print(13.5)


# ==============================
# String Data Type
# ==============================
print('Hello World')
print("Hello World")
print("What's your name")
print('What\'s your name')


# ==============================
# Bool Data Type
# ==============================
print(True)   # true
print(False)  # false


# ==============================
# Type Function
# ==============================
print(type('Hello World'))
print(type(10))
print(type(10.5))
print(type(True))


# ==============================
# Math Operations
# ==============================
print(5 + 5)
print(8 - 5)
print(2 * 5)
print(10 / 5)
print(5 ** 2)
print(10 // 5)
print(9 % 2)

print(5.1 + 5.8)
print(8 - 5.0)
print(2 * 5)
print(10 / 5)
print(5 ** 2)
print(10 // 5)
print(9 % 2)


# ==============================
# PEMDAS
# ==============================
10 * (5 / 2) + 3 - 2


# ==============================
# String Manipulation
# ==============================
print('Hello' + ' ' + 'World' + '!')

print('hello world'.upper())
print('HELLO WORLD'.lower())
print('hello world'.capitalize())


# ==============================
# print() - sep / end
# ==============================
print('Hello', 'World', '!', '!', 5)
print('Hello', 'World', '!', '!', 5, sep='@')
print('Hello', 'World', '!', '!', 5, sep='\t')
print('Hello World', end='-')
print('Hello World')


# ==============================
# Comparison Operators
# ==============================
print(1 == 5)
print('5' != '5')
print(5 > 6)
print(5 < 6)
print(6 >= 6)
print(6 <= 6)


# ==============================
# Logical Operators
# ==============================
# OR
print(False or False)
print(6 < 6 or 5 > 6)

# AND
print(True and False)
print(5 < 6 and 10 > 6)

# NOT
print(not False)
print(not (5 < 6 and 10 > 6))

print(18 <= 5 <= 65)  # 25 >= 18 and 25 <= 65


# ==============================
# Variables
# ==============================
age = 30
print(age + age + age + age)
print(age)
print(age)
print(age)
print(age)

# import keyword
# print(keyword.kwlist)

age_of_academy = 10   # snake_case
ageOfAcademy = 10     # camelCase

first_name, last_name = 'Irakli', 'Tabatadze'
print(first_name)
print(last_name)
print(first_name + ' ' + last_name)

first_name = 'John'
print(first_name)

first_name = first_name + last_name
first_name += last_name
print(first_name)


# ==============================
# Input & Type Conversion
# ==============================
name = input('Please input your name: ')
print('Hello', name)

int('50')
str()
float()
bool()

first_number = float(input('Please input the first number: '))
second_number = float(input('Please input the second number: '))
print(type(first_number))
print(type(second_number))
print(first_number + second_number)

print(bool(0))
print(bool(''))