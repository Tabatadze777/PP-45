# DRY (Don't Repeat Yourself) - პრინციპი: კოდი არ უნდა მეორდებოდეს.
# აქ ერთსა და იმავე პირობას ვამოწმებთ ორჯერ, ამიტომ ასეთი კოდი სჯობს ფუნქციად გავიტანოთ.
age = 18
if age <= 18:
    name = ''
elif age >= 18:
    name = ''


# იგივე კოდის განმეორება: მომხმარებელს ორჯერ ვეკითხებით სახელსა და ასაკს.
# ეს არის DRY პრინციპის დარღვევის მაგალითი.
name = input('Enter your name: ')
age = input('Enter your age: ')

print(f'Your name is {name} and your age is {age}')

name = input('Enter your name: ')
age = input('Enter your age: ')

print(f'Your name is {name} and your age is {age}')


# ფუნქციის შექმნა და გამოძახება: განმეორებადი კოდი ერთ ფუნქციაშია გაერთიანებული
# და საჭიროების შემთხვევაში რამდენჯერაც გვინდა, იმდენჯერ შეგვიძლია გამოვიძახოთ.
def greeting():
    name = input('What is your name? ')
    age = input('What is your age? ')
    print(f'Your name is {name} and your age is {age}')


greeting()
print('finished first function')
greeting()


# პარამეტრებიანი ფუნქცია default მნიშვნელობით: city არ არის სავალდებულო,
# თუ არ გადავცემთ, მისი მნიშვნელობა იქნება 'Tbilisi'.
# გადაცემა შეიძლება პოზიციით ან სახელით (keyword argument).
def greeting(first_name, last_name, city='Tbilisi'):
    print(f'first_name is {first_name}, last_name is {last_name} from {city}')


# პოზიციური არგუმენტები + city სახელით
greeting('John', 'Doe', city='Batumi')

# მხოლოდ keyword არგუმენტები: რიგითობას მნიშვნელობა არ აქვს
greeting(last_name='Ola', first_name='Ana')

# პოზიციური და keyword არგუმენტების შერევა (პოზიციურები ყოველთვის პირველია)
greeting('John', last_name='Doe')

# print-იც ფუნქციაა და შეუძლია რამდენიმე არგუმენტის მიღება
print('Hello', 'World', '!!!')


# ცვალებადი ტიპის (list) default მნიშვნელობა: ვიყენებთ None-ს და ფუნქციის შიგნით
# ვქმნით ახალ სიას, რომ გამოძახებებს შორის სია საერთო არ გახდეს.
def append_in_list(num, lst=None):
    if lst is None:
        lst = []

    lst.append(num)
    print(lst)


append_in_list(5)
append_in_list(2)
append_in_list(10, [1, 2, 3])


# print ფუნქცია ეკრანზე ბეჭდავს და აბრუნებს None-ს,
# ამიტომ something-ის მნიშვნელობა იქნება None.
print('Hello')
type_of_hello = type('Hello')
something = print(type_of_hello)


# return: ფუნქცია ტექსტს ბეჭდვის ნაცვლად აბრუნებს,
# შედეგი კი ცვლადში შეგვიძლია შევინახოთ და მოგვიანებით გამოვიყენოთ.
def greeting(first_name, last_name, city='Tbilisi'):
    return f'first_name is {first_name}, last_name is {last_name} from {city}'


greeting_text = greeting('Ana', 'Doe')
print(greeting_text)


# რამდენიმე მნიშვნელობის დაბრუნება: ფუნქცია აბრუნებს tuple-ს,
# რომელსაც გამოძახებისას რამდენიმე ცვლადში "ვხსნით" (unpacking).
def math_operation(num1, num2):
    multiply = num1 * num2
    division = num1 / num2
    return multiply, division


multiply_result, division_result = math_operation(10, 2)
print(multiply_result)
print(division_result)


# რამდენიმე return: ფუნქცია მუშაობას პირველივე შესრულებულ return-ზე ამთავრებს,
# ამიტომ else-ის გარეშეც სწორად გამოიცნობს ასაკობრივ კატეგორიას.
def check_age(age):
    if age < 0:
        print('age < 0')
        return "Invalid age"
    if age < 18:
        print('age < 18')
        return "Minor"

    print('else')
    return "Adult"


print(check_age(25))
