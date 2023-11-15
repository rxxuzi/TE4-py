var = (1, 2, 3) < (1, 2, 4)
print(var)
var = [1, 2, 3] < [1, 2, 4]
print(var)
var = 'ABC' < 'C' < 'Pascal' < 'Python'
print(var)
var = (1, 2, 3, 4) < (1, 2, 4)
print(var)
var = (1, 2) < (1, 2, -1)

print(var)
var = (1, 2, 3) == (1.0, 2.0, 3.0)
print(var)
var = (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
print(var)
