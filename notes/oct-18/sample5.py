# 辞書型(directory)
# 各要素の値は変更できない
# 各要素のキーは変更できない
# 各要素のキーは文字列でなければならない

fruits = {
    'orange': 'orange',
    'apple': 'red',
    'banana': 'yellow',
    'kiwi': 'green',
    'grape': 'purple',
    'peach': 'pink'
}

# ========================================
# 要素を取得
# ========================================
print(fruits['orange'])
print(fruits['apple'])

# ========================================
# 要素を追加
# ========================================
fruits['pear'] = 'green'
print(fruits['pear'])
print(fruits)

# ========================================
# 要素を削除
# ========================================
del fruits['pear']
print(fruits)

# ========================================
# 要素の存在確認
# ========================================
print('cherry' in fruits)
print('orange' in fruits)

# ========================================
# ループを使ってキーとバリューを同時に取り出す
# ========================================
for key, value in fruits.items():
    print(key, value)




