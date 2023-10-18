matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
]

# =====================================
# matrixの行と列を入れ替える
# =====================================
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


# ===========================================
# matrixの行と列を入れ替える
# ===========================================
p = [[row[i]for row in matrix] for i in range(4)]
print(p)

# ===========================================
# matrixの行と列を入れ替える(タプル)
# ===========================================
m = list(zip(*matrix))
print(m)