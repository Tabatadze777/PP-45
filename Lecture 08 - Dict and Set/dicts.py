# ცარიელი ლექსიკონის შექმნა
empty_dict = {}
print(empty_dict)


# ლექსიკონის შექმნა ორი გზით: {} სინტაქსით და dict() ფუნქციით
student = {'name': 'Ana', 'age': 21, 'city': 'Tbilisi'}
print(student)

student_2 = dict(name='Ana', age=22, city='Tbilisi')
print(student_2)


# ლექსიკონის ელემენტებზე წვდომა: გასაღებით, get-ით, keys-ით და values-ით
print(student['city'])
print(student.get('city', 'Unknown Key'))
print(student.keys())
print(student.values())


# ლექსიკონში ელემენტის დამატება, შეცვლა და setdefault
student['birth_date'] = '10 January'
student['name'] = 'Irakli'
print(student)

student.setdefault('birth_date', '10 January')
print(student)


# ლექსიკონიდან ელემენტის წაშლა (pop, clear), items-ით გადაყოლა, len და in
student = {'name': 'Ana', 'age': 21, 'city': 'Tbilisi'}

removed_element = student.pop('city')
print(removed_element)
print(student)

student.clear()
print(student)

print(student.items())
for key, value in student.items():
    print(f'Key: {key}, Value: {value}')

print(len(student))
print("age" in student)


# ჩადგმული (nested) ლექსიკონი
student = {
    'name': 'Ana',
    'age': 21,
    'city': 'Tbilisi',
    'grades': {'python': 90, 'java': 91, 'c': 100}
}

print(student['grades']['c'])
