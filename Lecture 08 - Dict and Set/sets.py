# ტუპლის unpacking (ელემენტების ცალკე ცვლადებში გაშლა)
person = ("Ana", 21, "Tbilisi")

name, age, city = person
print(name)
print(age)
print(city)


# მრავალი ცვლადისთვის მნიშვნელობის ერთ ხაზში მინიჭება
name, age = 'ana', 21
print(name)
print(age)


# სიის ელემენტებზე გადაყოლა, pop-ი და enumerate
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
    fruits.pop(0)
print("banana" in fruits)

for i, fruit in enumerate(fruits):
    if fruit == 'banana':
        print(f'index: {i}, fruit: {fruit}')


# სეტის შექმნა და დუბლიკატების ავტომატური მოშორება
tags = {'python', 'java', 'ai', 'python'}
print(tags)
for tag in tags:
    print(tag)


# ცარიელი სეტის შექმნა და ელემენტის დამატება
empty_set = set()
print(type(empty_set))

empty_set.add(10)
print(empty_set)


# სიიდან დუბლიკატების მოშორება სეტის გამოყენებით
programming_lst = ['python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python','python', 'java', 'ai', 'python']
programming_set = set(programming_lst)

set_to_lst = list(programming_set)
print(set_to_lst)


# სეტებზე მათემატიკური ოპერაციები: გაერთიანება
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a.union(b))


# სეტებზე მათემატიკური ოპერაციები: თანაკვეთა
print(a & b)
print(a.intersection(b))


# სეტებზე მათემატიკური ოპერაციები: სხვაობა
print(a - b)
print(a.difference(b))


# სეტებზე მათემატიკური ოპერაციები: სიმეტრიული სხვაობა
print(a ^ b)
print(a.symmetric_difference(b))


# სიის შევსება ციკლით და list comprehension
lst = []

for i in range(5):
    lst.append(i)

print(lst)


lst_comprehension = [i for i in range(5)]
print(lst_comprehension)


# ლექსიკონის comprehension
dct_comprehension = {i:i**2 for i in range(5)}
print(dct_comprehension)


# სეტის comprehension
set_comprehension = {i for i in range(5)}
print(set_comprehension)
