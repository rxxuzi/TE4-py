prime = []

for n in range(2 , 100):
    for x in range(2 , n):
        if(n % x == 0):
            break
    else:
        prime.append(n)


print(prime)