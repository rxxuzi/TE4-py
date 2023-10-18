# マップ (`map`) とは

`map` は、Pythonの組み込み関数であり、ある関数をイテラブルのすべての要素に適用して新しいイテラブルを生成するために使用される。

## 基本的な使用方法

`map`関数は、主に2つの引数を取る：

1. 関数： イテラブルの各要素に適用する関数。
2. イテラブル： 適用される関数の対象となる要素のコレクション。

## 例

```python
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared_numbers = map(square, numbers)

print(list(squared_numbers))  # [1, 4, 9, 16]
```

上記の例では、`square`関数がリスト`numbers`の各要素に適用され、新しいイテラブル`map`オブジェクトが生成される。
この結果を見るためには、`list`や他のイテラブルの型に変換する必要がある。

また、`lambda`関数と組み合わせて、コードをよりコンパクトにすることもできる：

```python
numbers = [1, 2, 3, 4]
squared_numbers = map(lambda x: x * x, numbers)
```

## 複数のイテラブルに適用

`map`関数は、複数のイテラブルにも適用することができる。
この場合、指定した関数は、それぞれのイテラブルから取得された要素のタプルに適用される。

```python
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = map(add, list1, list2)

print(list(result))  # [5, 7, 9]
```
