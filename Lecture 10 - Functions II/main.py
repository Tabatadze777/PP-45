# ეს პროგრამა ალაგებს ადამიანების სიას (ლექსიკონების სია) lambda ფუნქციის დახმარებით:
# ჯერ ასაკის, შემდეგ კი ქულის მიხედვით, კლებადობით (reverse=True), და ბეჭდავს შედეგს.

people = [
     {"name": "Ana", "age": 20, 'score': 10},
     {"name": "Nino", "age": 20, 'score': 9},
     {"name": "Luka", "age": 20, 'score': 8},
]


sorted_age = sorted(people, key=lambda x: (x['age'], x['score']), reverse=True)
print(sorted_age)
