# *args და **kwargs ერთად: ნებისმიერი რაოდენობის პოზიციური და ქივორდ არგუმენტები
def show_args(first_name: str, last_name: str, *scores: int, **kwargs) -> str:
    print(first_name)
    print(last_name)
    print(scores)
    print(kwargs)
    return first_name + " " + last_name


var = show_args('John', 'Smith', 90, 92, 100, scores=[10, 25, 30])


# *args: სიის დაშლა (unpacking) ფუნქციის არგუმენტებად
def add(x, y, *args):
    if len(args) > 0:
        print('There is too much arguments')
    print(f'X = {x}, Y = {y}')
    return x + y


lst = [10, 15, 25]
add(*lst)


# **kwargs: ლექსიკონის დაშლა (unpacking) ქივორდ არგუმენტებად
def profile(first_name, last_name, **kwargs):
    print(first_name)
    print(last_name)
    print(f'Additional Information: {kwargs}')


additional_info = {'last_name': 'Doe', 'phone_number': '+995123412341234', 'passport_id': '1351325123'}
profile('John', **additional_info)


# რეკურსია: ფიბონაჩის მიმდევრობა (1, 1, 2, 3, 5, 8, 13)
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


# ფუნქცია როგორც ობიექტი: ფუნქციის სახელის დაბეჭდვა ფუნქციის ობიექტს აჩვენებს
def square(x):
    return x * x

def power(x, y):
    return x ** y

def square_var3(x):
    return x ** 3

print(square)
print(power)
print(square_var3)


# lambda ფუნქცია და მისი ექვივალენტი def-ით (პირობით გამოსახულებასთან ერთად)
def lambda_to_def(x):
    if x > 0:
        return x / x
    else:
        return 'x = 0'

square_var1 = lambda x: x / x if x > 0 else 'x = 0'
square_var2 = lambda x: x / x
square_var3 = lambda x: x / x
# print(square_var(10))
print(square_var1)
print(square_var2)
print(square_var3)

print(lambda_to_def(0))
print(square_var1(0))


# lambda ფუნქცია რამდენიმე პარამეტრით და ნაგულისხმევი მნიშვნელობით
lambda x, y: x / x
square_var1 = lambda x, y=10: x * y
print(square_var1(y=5, x=3))


# sorted() და lambda: ტუპლების სიის დალაგება რამდენიმე კრიტერიუმით
students = [("Charlie", 85, 25, 92), ("Alice", 78, 25, 53), ("Bob", 92, 8, 15)]

sorted_students = sorted(students, key=lambda student: (student[2], student[1]) )
print(sorted_students)


# sorted() და lambda: ლექსიკონების სიის დალაგება (ასაკისა და ქულის მიხედვით, კლებადობით)
people = [
     {"name": "Ana", "age": 20, 'score': 10},
     {"name": "Nino", "age": 20, 'score': 9},
     {"name": "Luka", "age": 20, 'score': 8},
]


sorted_age = sorted(people, key=lambda x: (x['age'], x['score']), reverse=True)
print(sorted_age)
