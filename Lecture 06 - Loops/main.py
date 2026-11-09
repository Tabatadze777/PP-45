# ==================================================
# String Homework #4
# ==================================================
title = '  My First Python   Program '


split_title = title.lower().split()
slug = '-'.join(split_title)
print(slug)


# ==================================================
# try/except/else/finally
# ==================================================
try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a / b)
except ValueError:
    print("შეყვანილი მნიშვნელობები უნდა იყოს მთელი რიცხვები.")
except ZeroDivisionError:
    print("ნულზე გაყოფა შეუძლებელია.")
else:
    print('ყველაფერი დასრულდა წარმატებით')
finally:
    print('ყველა მოქმედება დასრულდა')


# ==================================================
# while loop: counting from 1 to 10
# ==================================================
count = 1

while count <= 10:
    print(f'Count: {count}')
    count += 1

print('After While Loop')


# ==================================================
# while loop: password check (3 attempts)
# ==================================================
password = ''
count = 1

while password != 'Python123' and count <= 3:
    password = input('Enter your password: ')

    if password != 'Python123':
        print('Wrong password')
        count += 1
    else:
        print('Password is correct')


# ==================================================
# while loop: countdown from 10 to 1
# ==================================================
number = 10
while number > 0:
    print(number)
    number -= 1


# ==================================================
# while loop: counting up from 1 to 10
# ==================================================
number = 1
while number <= 10:
    print(number)
    number += 1


# ==================================================
# while loop: sum of numbers until -1 is entered
# ==================================================
total = 0
number = 0


while number != -1:
    number = int(input("Enter a number: "))

    if number != -1:
        total += number


print(total)


# ==================================================
# while loop: menu (q to quit)
# ==================================================
inp = ''
while inp != 'q':
    print('1. Home')
    print('2. Calculator')
    print('3. File Handler')

    inp = input('Enter your choice: ')

    if inp == '1':
        print('You are on home page')
    elif inp == '2':
        print('You are on calculator')
    elif inp == '3':
        print('You are on file handler')
    elif inp == 'q':
        print('Goodbye')


# ==================================================
# while loop: age validation (0-120)
# ==================================================
age = -1
while age < 0 or age > 120:
    age = int(input("Enter valid age (0-120): "))
print("Accepted age:", age)
