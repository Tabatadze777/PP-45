# ==================================================
# try/except
# ==================================================

# Try
try:
    num = int(input('Enter a number: '))

except ValueError as e:
    print(f'ERROR: {e}')
except Exception as e:
    print(f'ERROR: {e}')

print('after user input')


# ==================================================
# infinite loop
# ==================================================

# Break
while True:
    inp = input('Please enter something: ')

    if inp == 'q':
        break
    if inp == '-1':
        break
    if inp == 'quit':
        break

    print(f'User Input: {inp}')

print('While finished')


# Continue
total = 1

while True:
    num = input('Enter a number: ')

    if num == 'q':
        break

    if int(num) == 0:
        print('Zero must not be used')
        continue

    print('Calculating')
    total *= int(num)

print(total)


# ==================================================
# for loop
# ==================================================

# While
i = 0
while i < 5:
    print(f'i = {i}')
    i += 1


# Range
for i in range(1, 5):
    print(f'i = {i}')


# String
for ch in 'Python':
    print(ch)


# Reverse
for i in range(10, 0, -1):
    print(f'i = {i}')


# ==================================================
# nested loops
# ==================================================

# Stars
row = 0

while row < 5:
    column = 0

    while column < 5:
        print('*', end='  ')
        column += 1

    print()
    row += 1


# Table
row = 1

while row < 11:
    column = 1

    while column < 11:
        print(f'{row} * {column} = {row * column}', end='    ')
        column += 1

    print()
    row += 1


# Square
for i in range(5):
    for j in range(5):
        print('*', end='  ')
    print()


# Multiplication
for i in range(5):
    for j in range(5):
        print(f'{i} * {j} = {i * j}', end='    ')
    print()
