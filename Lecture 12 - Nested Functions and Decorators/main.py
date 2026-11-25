from functools import reduce, wraps


# ==============================================================================
# map() - ფუნქციის გამოყენება სიის ყველა ელემენტზე
# lambda-თი თითოეული რიცხვი მრავლდება 2-ზე, შედეგი list()-ად გადაგვყავს
# ==============================================================================
nums = [5, 10, 15]

mapped_nums = list(map(lambda x: x * 2, nums))
print(mapped_nums)

for num in mapped_nums:
    print(num)


# ==============================================================================
# map() + ჩაშენებული ფუნქცია
# map-ს შეგვიძლია გადავცეთ არა მხოლოდ lambda, არამედ ჩაშენებული ფუნქციაც
# (მაგ. int), რომ სტრიქონების სია რიცხვების სიად გადავაქციოთ
# ==============================================================================
texts = ["1", "2", "3", "4"]
print(texts)

numbers = list(map(int, texts))
print(numbers)


# ==============================================================================
# filter() - ელემენტების გაფილტვრა პირობით
# რჩება მხოლოდ ის ელემენტები, რომლისთვისაც ფუნქცია აბრუნებს True-ს
# (აქ: მხოლოდ ლუწი რიცხვები)
# ==============================================================================
nums = [1, 2, 3, 4, 5, 6, 7, 8]

filtered_nums = filter(lambda num: num % 2 == 0, nums)
print(list(filtered_nums))


# ==============================================================================
# reduce() - სიის ერთ მნიშვნელობამდე დაყვანა
# acc ინახავს დაგროვილ შედეგს, x კი მიმდინარე ელემენტია
# (აქ: ყველა რიცხვის ნამრავლი)
# ==============================================================================
nums = [1, 2, 3, 4, 5]

reduced_nums = reduce(lambda acc, x: acc * x, nums)
print(reduced_nums)


# ==============================================================================
# ფუნქცია, როგორც ობიექტი (First-Class Function)
# ფუნქცია შეგვიძლია ჩავწეროთ ცვლადში და არგუმენტად გადავცეთ სხვა ფუნქციას
# ==============================================================================
def square(x):
    return x ** 2


new_name = square
print(square(10))
print(new_name(5))


def test(func):
    print(func(10))


test(square)


# ==============================================================================
# ჩადგმული ფუნქცია (Nested Function)
# ფუნქციის შიგნით სხვა ფუნქციის შექმნა და მისი დაბრუნება (გამოძახების გარეშე),
# შემდეგ დაბრუნებული ფუნქციის გამოძახება გარედან
# ==============================================================================
def outer():
    def inner():
        return 'Inner Function'

    return inner


outer_result = outer()
print(outer_result())


# ==============================================================================
# ხედვის არეები - LEGB წესი (Local, Enclosing, Global, Built-in)
# ერთი და იგივე სახელის ცვლადი სხვადასხვა არეში: global, enclosing და local.
# inner-ში `count = 200` ქმნის ახალ ლოკალურ ცვლადს და გარე count-ებს არ ცვლის.
# გარე ცვლადის შესაცვლელად inner-ში საჭიროა `global count` (გლობალური)
# ან `nonlocal count` (enclosing არეს ცვლადი)
# ==============================================================================
count = 10  # Global


def outer():
    count = 125  # Enclosing
    print(f'Outer Function: {count}')

    def inner():
        count = 200  # Local
        print(f'Inner Function: {count}')

    inner()


outer()
print(f'Global Scope: {count}')


# ==============================================================================
# დეკორატორი - საბაზისო მაგალითი
# დეკორატორი იღებს ფუნქციას და აბრუნებს wrapper-ს, რომელიც ორიგინალ ფუნქციას
# გამოძახების წინ და შემდეგ დამატებით ქცევას ამატებს.
# *args და **kwargs wrapper-ს ნებისმიერი არგუმენტის მიღების საშუალებას აძლევს.
# `@my_decorator` სინტაქსი იგივეა, რაც say_hello = my_decorator(say_hello)
# ==============================================================================
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Args: {args}, Kwargs: {kwargs}')
        print('Before calling function')
        result = func(args[0])
        print('After calling function')
        return result

    return wrapper


@my_decorator
def say_hello(name):
    return f'Hello {name}!'


decorator = my_decorator(say_hello)
print(decorator('John'))

returned_info = say_hello('Irakli')
print(returned_info)


# ==============================================================================
# დეკორატორი functools.wraps-ით
# @wraps(func) ინახავს ორიგინალი ფუნქციის მეტამონაცემებს (__name__, __doc__,
# __annotations__), რომლებიც wrapper-ით ჩანაცვლებისას სხვა შემთხვევაში დაიკარგებოდა.
# log_calls ბეჭდავს გამოძახებულ ფუნქციას, მის არგუმენტებს და დაბრუნებულ შედეგს
# ==============================================================================
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} "f"args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result

    return wrapper


@log_calls
def say_hello(name: str):
    """Returns a hello message"""
    return f'Hello {name}!'


print(say_hello.__name__)
print(say_hello.__doc__)
print(say_hello.__annotations__)


# ==============================================================================
# ერთი დეკორატორის გამოყენება რამდენიმე ფუნქციაზე
# იგივე log_calls დეკორატორი ნებისმიერ ფუნქციას შეგვიძლია დავადოთ
# ==============================================================================
@log_calls
def say_goodbye(name):
    return f'Goodbye {name}!'


@log_calls
def square(number):
    return number ** 2


say_hello('John')
say_goodbye('John')
square(3)


# ==============================================================================
# დეკორატორი პარამეტრით (Decorator Factory) და დეკორატორების გაერთიანება
# repeat(count) აბრუნებს დეკორატორს, რომელიც ფუნქციას count-ჯერ იძახებს.
# სამი ჩადგმული დონე: repeat -> decorator -> wrapper.
# რამდენიმე დეკორატორი ქვემოდან ზემოთ გამოიყენება:
# ჯერ log_calls, შემდეგ repeat(10)
# ==============================================================================
def repeat(count):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(10)
@log_calls
def say_hello(name: str):
    """Returns a hello message"""
    print(f'Hello {name}!')


say_hello('Irakli')
