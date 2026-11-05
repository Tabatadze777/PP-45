# ==================================================
# if/elif/else
# ==================================================

# Grades
grade = 61

if grade > 50 and grade < 60:
    print('E')
elif grade >= 60 and grade < 70:
    print('D')
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 80 and grade < 90:
    print('B')
elif grade >= 90 and grade < 100:
    print('A')
else:
    print('F')


# And
age = 25
has_id = True

if age >= 18 and has_id:
    print('Yes')
else:
    print('No')


# Truthiness
name = input('Enter a name: ')

if name:
    print(f'Hello, {name}!')
else:
    print('Please enter a name!')


# Or
role = 'moderator'

if role == 'admin' or role == 'moderator':
    print('You can add new product')


# Not
has_id = True

if not has_id:
    print('You have no ID')


# Nested
age = 20
has_ticket = True
has_id = True

if age >= 18 and (has_ticket or has_id):
    print('User is old enough')

    if has_ticket and has_id:
        print('You can play')
    else:
        print('You lack of documents')

else:
    print('Sorry, you are not old enough to play')


# ==================================================
# Error/Exception Handling
# ==================================================

try:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a number: '))
    print(num1 / num2)

except ValueError as e:
    print('invalid input')

except ZeroDivisionError as e:
    print('cannot divide by zero')

except Exception as e:
    print(e)
