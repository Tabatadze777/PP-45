# ==================================================
# ASCII -  7-BIT დიაპაზონი
# ==================================================
# 1111111 - 7 BIT
# 0000000 - MIN - 0
# 1111111 - MAX - 127


# ==================================================
# UTF-8
# ==================================================
# 11111111 1111111 1111111 11111111


# ==================================================
# სტრინგზე ინდექსებით წვდომა
# ==================================================
txt = 'Python'
print(txt[0])
print(txt[1])
print(txt[-1])


# ==================================================
# სტრინგის დაჭრა (Slicing)
# ==================================================
text = 'Hello World'
first_part = text[0:5]
second_part = text[6:11]

print(first_part)
print(second_part)
print(text[:5])
print(text[6:])
print(text[:])

print(text[0:11:2])

num = '1221'
print(num[::-1])
print(num)


# ==================================================
# სტრინგის მეთოდები: upper, lower, capitalize, title
# ==================================================
user_input = input('Enter yes/no: ')

print(user_input.upper())
print(user_input.lower())
print(user_input.lower() == 'yes')

print(user_input.capitalize())
print(user_input.title())


# ==================================================
# ელფოსტიდან დომენის ამოღება
# ==================================================
email1 = 'irakli@gmail.com'
email2 = 'irakli@yahoo.com'

print(email1.find('@'))
print(email1.index('@'))

domain1 = email1[email1.index('@') + 1:]
domain2 = email2[email2.index('@') + 1:]

print(domain1)
print(domain2)


# ==================================================
# strip() - ზედმეტი სივრცეების მოშორება
# ==================================================
answer = input('Type yes or no: ')
# მაგალითები: 'Yes', 'yEs', '  yes', 'yes  ', '  yes  '
print(answer.strip().lower())


# ==================================================
# replace() - ჩანაცვლება
# ==================================================
text = 'I  love  Java'
print(text.replace('Java', 'Python'))
print(text.replace('  ', ' '))


# ==================================================
# split() და join()
# ==================================================
text = 'one,two,three'
split_text = text.split(',')
print(split_text)

joined_text = ' '.join(split_text)
print(joined_text)


# ==================================================
# სტრინგის ფორმატირება
# ==================================================
print("Hello, I'm John Doe, I'm", 30, "years old")

name = input('Enter your name: ')
age = input('Enter your age: ')

text = f"Hello, I'm {name}, I'm {age} years old"
print(text)


# ==================================================
# რეგულარული გამოსახულებები (Regular Expressions)
# ==================================================
import re

text = "My contact is 555-123-4567."
pattern = r"\d{3}-\d{3}-\d{4}"

match = re.search(pattern, text)
print(match.group(0))