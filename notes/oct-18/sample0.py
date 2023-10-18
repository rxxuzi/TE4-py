# ===========================================
# basic list comprehension
# ===========================================
squares = []
for x in range(1, 11):
    squares.append(x ** 2)
print(squares)

# ===========================================
# list comprehension
# ===========================================
squares = [x ** 2 for x in range(1, 11)]
print(squares)
print(type(squares))

# ===========================================
# list comprehension with if
# ===========================================
s = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(s)
