# 集合 (set)
# 一般的には、集合は、順序を持たない、重複しない、変更可能なデータ型である。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# fast membership testing
print('orange' in basket)
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

# unique letters in a
print(a)
# unique letters in b
print(b)
# letters in a that are not in b
print(a - b)
# letters in b that are not in a
print(b - a)
# letters in both a and b
print(a & b)
# letters in either a or b
print(a | b)
# letters in a or b but not both
print(a ^ b)


# ===========================================
# Manipulation of sets
# ===========================================
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# 和集合
print(s1.union(s2))  # {1, 2, 3, 4}

# 積集合
print(s1.intersection(s2))  # {2, 3}

# 差集合
print(s1.difference(s2))  # {1}
