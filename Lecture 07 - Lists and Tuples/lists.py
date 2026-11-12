
# -----------------------------------------------------------------------------
# 1. Creating lists
# -----------------------------------------------------------------------------

# Empty lists
empty_lst_1 = []
empty_lst_2 = list()

print(empty_lst_1)
print(empty_lst_2)

# List with numbers
lst = [1, 2, 3, 4, 5]
print(lst)

# List with mixed types
lst = ['Hello', 'World', 1, 2]
print(lst)

# Nested list
nested = [[1, 2], [3, 4], [5, 6]]
print(len(nested))


# -----------------------------------------------------------------------------
# 2. Indexing
# -----------------------------------------------------------------------------

colors = ["red", "green", "blue"]
print(colors[3])    # IndexError: list index out of range
print(colors[-2])   # negative index counts from the end

# Indexing nested lists
nested = [
    [1, 2, 3],
    [3, 4],
    [5, 6],
]
print(len(nested[0]))
print(nested[1][1])


# -----------------------------------------------------------------------------
# 3. Slicing  ->  lst[start:stop:step]
# -----------------------------------------------------------------------------

lst = [10, 7, 9, 10.5, 3, 2, 8]
print(lst[1:4:2])
print(lst[:5])
print(lst[2:])
print(lst[::-1])


# -----------------------------------------------------------------------------
# 4. Mutability (lists can change, strings cannot)
# -----------------------------------------------------------------------------

# Strings are immutable: upper() returns a NEW object
name = 'irakli'
name_upper = name.upper()

print(id(name))
print(id(name_upper))

# Lists are mutable: item assignment changes the list in place
lst = [10, 7, 9, 10.5, 3, 2, 8]
lst[-1] = 125
print(lst)


# -----------------------------------------------------------------------------
# 5. Adding elements: append / insert / extend
# -----------------------------------------------------------------------------

lst.append('Hello')
lst.append('World')
print(lst)
print(lst[2])

lst.insert(0, 'Hello')
print(lst[3])

lst_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst.extend(lst_2)
print(lst)


# -----------------------------------------------------------------------------
# 6. Removing elements: remove / pop / del / clear
# -----------------------------------------------------------------------------

lst = [10, 7, 9, 10.5, 3, 2, 8]
lst.remove('Hello')
last_element = lst.pop(2)
print(last_element)
print(lst)

# del lst[2]
lst.clear()
print(lst)


# -----------------------------------------------------------------------------
# 7. Searching and sorting: count / index / reverse / sort
# -----------------------------------------------------------------------------

lst = [10, 7, 9, 10.5, 3, 2, 8]
lst = ['Irakli', 'Nika', 'Levani', 'Ana', 'Nutsa']

print(lst.count(10))
print(lst.index(10.5))

lst.reverse()
# lst.sort(reverse=True)
lst.sort()
print(lst)


# -----------------------------------------------------------------------------
# 8. Copying lists
# -----------------------------------------------------------------------------

lst = [10, 7, 9, 10.5, 3, 2, 8]
# copied_lst = lst[:]
copied_lst = lst.copy()
# copied_lst = list(lst)

print(id(lst))
print(id(copied_lst))

copied_lst[0] = 'Hello'
print(lst)
print(copied_lst)
