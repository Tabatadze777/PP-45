import sys
from inspect import getgeneratorstate


# ==============================================================================
# იტერატორი - iter() და next()
# iter() ქმნის სიის იტერატორს, next() კი ყოველ გამოძახებაზე შემდეგ ელემენტს აბრუნებს.
# როცა ელემენტები ამოიწურება, next() იწვევს StopIteration-ს
# (აქ ის try/except-ით დავიჭირეთ, რომ პროგრამა არ გაჩერდეს)
# ==============================================================================
lst = [10, 2, 15, 4, 6, 11]

iterator_lst = iter(lst)

print(next(iterator_lst))
print(next(iterator_lst))
print(next(iterator_lst))
print(next(iterator_lst))
print(next(iterator_lst))
print(next(iterator_lst))

try:
    print(next(iterator_lst))
except StopIteration:
    print('StopIteration - ელემენტები ამოიწურა')


# ==============================================================================
# იტერაცია ხელით - while True + StopIteration
# ასე მუშაობს for ციკლი "კულისებში": next() გამოიძახება მანამ,
# სანამ StopIteration არ დაფიქსირდება
# ==============================================================================
iterator_lst = iter(lst)

while True:
    try:
        print(next(iterator_lst))
    except StopIteration:
        break


# ==============================================================================
# გენერატორი - yield და return-ის განსხვავება
# yield-ის შემცველი ფუნქცია გენერატორია: ის არ სრულდება ერთბაშად, არამედ
# ყოველ next()-ზე აბრუნებს ერთ მნიშვნელობას და ჩერდება.
# return კი ფუნქციას პირველივე გამოძახებაზე ამთავრებს
# ==============================================================================
def countdown1(n):
    while n > 0:
        yield n
        n -= 1


def countdown2(n):
    while n > 0:
        return n
    n -= 1


print(countdown2(1))
count_down = countdown1(10)

print(next(count_down))
print(next(count_down))
print(next(count_down))
print(next(count_down))
print(next(count_down))
print(next(count_down))
print(next(count_down))
print(next(count_down))
print(next(count_down))
print(next(count_down))


# ==============================================================================
# გენერატორის ამოწურვა
# გენერატორი ერთჯერადია: ყველა მნიშვნელობის ამოღების შემდეგ ის ცარიელია,
# ამიტომ ციკლი და list() მასზე აღარაფერს აბრუნებს
# ==============================================================================
for i in count_down:
    print(i)

lst_count_down = list(count_down)
print(lst_count_down)
lst_2 = list(count_down)
print(lst_2)


# ==============================================================================
# გენერატორის შესრულების პაუზა
# yield-ზე ფუნქცია ჩერდება და next()-ის შემდეგ გამოძახებაზე გრძელდება იმავე
# ადგილიდან. გენერატორის შექმნისას კოდი ჯერ არ სრულდება (print(demo_gen)
# მხოლოდ გენერატორის ობიექტს გვიჩვენებს). როცა yield-ები მთავრდება,
# ფუნქცია სრულდება და next() იწვევს StopIteration-ს
# ==============================================================================
def demo():
    print(" -> დაიწყო")
    yield "A"
    print(" -> გაგრძელდა A-ს შემდეგ")
    yield "B"
    print(" -> გაგრძელდა B-ს შემდეგ")
    print(" -> ემზადება დასრულებისთვის")


demo_gen = demo()
print(demo_gen)
print(next(demo_gen))
print(next(demo_gen))

try:
    print(next(demo_gen))
except StopIteration:
    print('StopIteration - გენერატორი დასრულდა')


# ==============================================================================
# return გენერატორში
# გენერატორში return ამთავრებს გენერატორს.
# აქ ვაბრუნებთ მხოლოდ პირველ უარყოფით რიცხვს და ვჩერდებით
# ==============================================================================
def first_negative(numbers):
    for n in numbers:
        if n < 0:
            yield n
            return


print(list(first_negative([4, -1, 7, -9])))


# ==============================================================================
# გენერატორის მდგომარეობები - getgeneratorstate()
# გენერატორი გადის მდგომარეობებს: GEN_CREATED (შექმნილია), GEN_SUSPENDED
# (yield-ზე შეჩერებულია) და GEN_CLOSED (დასრულებულია)
# ==============================================================================
def countdown(n):
    while n > 0:
        yield n
        n -= 1


generator = countdown(5)
try:
    print(getgeneratorstate(generator))
    print(next(generator))
    print(getgeneratorstate(generator))
    print(next(generator))
    print(getgeneratorstate(generator))
    print(next(generator))
    print(getgeneratorstate(generator))
    print(next(generator))
    print(getgeneratorstate(generator))
    print(next(generator))
    print(getgeneratorstate(generator))
    print(next(generator))

except StopIteration:
    print(getgeneratorstate(generator))


# ==============================================================================
# მეხსიერება - სია vs გენერატორი
# სია ყველა ელემენტს ერთბაშად მეხსიერებაში ინახავს, გენერატორი კი მხოლოდ
# მიმდინარე მდგომარეობას და ელემენტებს საჭიროებისას აგენერირებს.
# sys.getsizeof() აჩვენებს, რომ გენერატორი მილიონი ელემენტისთვისაც კი
# ძალიან მცირე მეხსიერებას იკავებს
# ==============================================================================
def generate_list(n):
    lst = [i for i in range(n)]
    return lst


def generator(n):
    count = 0
    while count <= n:
        yield count
        count += 1


lst = generate_list(1_000_000)
gen = generator(1_000_000)

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))


# ==============================================================================
# Comprehension-ები და გენერატორ-გამოსახულება
# კვადრატულ ფრჩხილებში [ ] - სია, ფიგურულში { } - ლექსიკონი ან სიმრავლე.
# ჩვეულებრივ ფრჩხილებში ( ) კი tuple-ი არ იქმნება, არამედ გენერატორი,
# რომელიც ელემენტებს ზარმაცად (lazy) აგენერირებს.
# გენერატორი შეგვიძლია პირდაპირ ფუნქციას გადავცეთ (მაგ. max)
# ==============================================================================
lst = [i for i in range(10)]
print(lst)

dct = {i: i * i for i in range(10)}
print(dct)

st = {i for i in range(10)}
print(st)

tpl = (i for i in range(10) if i % 2 == 0)
print(tpl)
for i in tpl:
    print(i)

print(max(i for i in range(10) if i % 2 == 0))


# ==============================================================================
# map() და filter() - ზარმაცი (lazy) იტერატორები
# map და filter სიას კი არა, იტერატორის ობიექტს აბრუნებენ.
# მნიშვნელობები გამოითვლება მხოლოდ მაშინ, როცა მათ ციკლით ან list()-ით ვიღებთ
# ==============================================================================
nums = [5, 10, 15]

mapped_nums = map(lambda x: x * 2, nums)
print(mapped_nums)
for num in mapped_nums:
    print(num)

nums = [1, 2, 3, 4, 5, 6, 7, 8]

filtered_nums = filter(lambda num: num % 2 == 0, nums)
print(filtered_nums)


# ==============================================================================
# გენერატორების ჯაჭვი (Pipeline)
# რამდენიმე მარტივი გენერატორი ერთმანეთს უერთდება: ერთის გამოსავალი მეორის
# შესავალია. მონაცემები ელემენტ-ელემენტად გადის მთელ ჯაჭვში.
# აქ: ხაზების გასუფთავება -> ცარიელი ხაზების გამოტოვება -> CSV-ის დაშლა
# ==============================================================================
def read_lines(source):
    for line in source:
        yield line.strip()


def non_empty(lines):
    for line in lines:
        if line:
            yield line


def parse_csv(lines):
    for line in lines:
        yield line.split(",")


raw = ["alice,30,120.50", "", "bob,25,80.00", " ", "carol,41,200.25"]
rows = parse_csv(non_empty(read_lines(raw)))
for row in rows:
    print(row)


# ==============================================================================
# yield from - ჩადგმული სიის გაშლა (flatten)
# ჯერ ვხსნით ჩადგმული ციკლებით, შემდეგ იგივეს ვაკეთებთ yield from-ით,
# რომელიც მოცემული იტერაბელის ყველა ელემენტს თავად აბრუნებს
# ==============================================================================
def flatten_with_loops(lst):
    for sublist in lst:
        for i in sublist:
            yield i


def flatten(lst):
    for sublist in lst:
        yield from sublist


lst1 = [[1, 2, 3], [4, 5], [6, 7, 8]]
lst2 = [[1, 2, 3], [4, 5], [6, 7, 8]]
lst3 = [[1, 2, 3], [4, 5], [6, 7, 8]]

gen1 = flatten_with_loops(lst1)
for i in gen1:
    print(i, end=' ')
print()

gen2 = flatten(lst2)
for i in gen2:
    print(i, end=' ')
print()

gen3 = flatten(lst3)
for i in gen3:
    print(i, end=' ')
print()
