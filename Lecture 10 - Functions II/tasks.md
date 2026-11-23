# Lecture 10 - Functions II: ამოცანები

## ამოცანა 1: პიცერიის შეკვეთა 🍕

დაწერეთ ფუნქცია `make_order(customer, size, *toppings, **extras)`, რომელიც აყალიბებს პიცის შეკვეთას:

- `customer`: მომხმარებლის სახელი;
- `size`: პიცის ზომა (`'small'`, `'medium'` ან `'large'`);
- `*toppings`: ნებისმიერი რაოდენობის დანამატი (მაგ. `'cheese'`, `'mushrooms'`, `'olives'`);
- `**extras`: დამატებითი პარამეტრები (მაგ. `delivery=True`, `drink='Cola'`, `note='No onions'`).

ფასები:

- ზომის ფასი: small = 10, medium = 15, large = 20;
- თითო დანამატი = 2;
- `delivery=True` ამატებს 5-ს.

ფუნქციამ უნდა დაბეჭდოს ლამაზად ფორმატირებული ჩეკი (ყველა დანამატი და დამატებითი პარამეტრი ცალკე ხაზზე) და დააბრუნოს საბოლოო ფასი.

გამოიძახეთ ორი გზით:

```python
make_order('Nino', 'large', 'cheese', 'olives', delivery=True, drink='Cola')

toppings = ['cheese', 'mushrooms', 'ham']
extras = {'delivery': False, 'note': 'No onions'}
make_order('Luka', 'medium', *toppings, **extras)
```

> **მინიშნება:** `**extras`-ში ნებისმიერი სახელის მქონე არგუმენტი მოხვდება და Python შეცდომას არ ამოაგდებს. ამიტომ ქივორდების (keyword) სახელები სწორად უნდა შეამოწმოთ `get` მეთოდით. მაგალითად, თუ დაწერეთ `delivary=True` და არა `delivery=True`, პროგრამა შეცდომის გარეშე იმუშავებს, მაგრამ მიტანის ფასს ვერ დაამატებს. `extras.get('delivery')` დააბრუნებს `None`-ს, თუ ასეთი გასაღები არ არსებობს (ან მეორე არგუმენტად მითითებულ მნიშვნელობას: `extras.get('delivery', False)`), ამიტომ `KeyError` არ მოხდება. იგივე ეხება `extras` ლექსიკონის გასაღებებს.

## ამოცანა 2: თამაშის ლიდერბორდი 🎮

მოცემულია მოთამაშეების სია:

```python
players = [
    {"nick": "ShadowWolf", "level": 42, "wins": 120, "losses": 30},
    {"nick": "PixelQueen", "level": 42, "wins": 95, "losses": 10},
    {"nick": "NoobMaster", "level": 7, "wins": 3, "losses": 40},
    {"nick": "DragonFly", "level": 58, "wins": 200, "losses": 100},
    {"nick": "CatLord", "level": 58, "wins": 150, "losses": 25},
]
```

`sorted`-ისა და `lambda`-ს გამოყენებით დაბეჭდეთ:

1. **ლიდერბორდი**: ჯერ დონის (`level`) მიხედვით კლებადობით, თანაბარი დონის შემთხვევაში გამარჯვებების (`wins`) მიხედვით კლებადობით;
2. **ყველაზე სტაბილური მოთამაშეები**: დალაგებული win rate-ის მიხედვით კლებადობით, სადაც `win rate = wins / (wins + losses)`;
3. **ნიკების ტოპი**: ნიკები დალაგებული სიგრძის მიხედვით, ერთნაირი სიგრძის შემთხვევაში კი ანბანით.

## ამოცანა 3: მუსიკალური პლეილისტი 🎵

მოცემულია სიმღერების სია. თითოეული სიმღერა არის ლექსიკონი, სადაც ხანგრძლივობა (`duration`) წამებშია მითითებული:

```python
songs = [
    {"title": "Sunrise", "artist": "Luna", "duration": 215, "plays": 5400},
    {"title": "Midnight Drive", "artist": "Neon Pulse", "duration": 187, "plays": 12800},
    {"title": "Ocean Eyes", "artist": "Luna", "duration": 243, "plays": 9100},
    {"title": "Thunder", "artist": "Neon Pulse", "duration": 201, "plays": 7600},
    {"title": "Quiet Rain", "artist": "Mira", "duration": 156, "plays": 3200},
]
```

**ნაბიჯი 1.** დაწერეთ ფუნქცია `show_playlist(name, *songs)`, რომელიც დაბეჭდავს პლეილისტის სახელს და სიმღერებს ნუმერაციით, მაგალითად:

```
Top Hits
1. Sunrise - Luna (215 წმ)
2. Midnight Drive - Neon Pulse (187 წმ)
...
```

ნუმერაციისთვის გამოიყენეთ ცვლადი, რომელსაც ციკლში ყოველ ჯერზე 1-ით გაზრდით.

გამოიძახეთ ფუნქცია სიის დაშლით:

```python
show_playlist('My Playlist', *songs)
```

**ნაბიჯი 2.** `sorted`-ისა და `lambda`-ს გამოყენებით დაალაგეთ სიმღერები ხანგრძლივობის მიხედვით ზრდადობით და გადაეცით `show_playlist`-ს (`Short First`).

**ნაბიჯი 3.** დაალაგეთ სიმღერები მოსმენების (`plays`) მიხედვით კლებადობით (`reverse=True`), აიღეთ პირველი 3 სიმღერა (slice: `[:3]`) და გადაეცით `show_playlist`-ს (`Top 3`).

> **მინიშნება:** `lambda` ასე დაიწყეთ: `key=lambda song: song["duration"]`.

