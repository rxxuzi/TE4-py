# ListとTuple

## リスト (List) とは

リストは、Pythonの基本的なデータ型の一つであり、順序付けられた要素のコレクションを表す。リストは変更可能であり、異なるデータ型の要素を含むことができる。

### リストの生成

リストは、角括弧 `[]` を使用して要素を定義することで作成できる。

```python
list1 = [1, 2, 3, 4]
list2 = ["apple", "banana", "cherry"]
```

### 主な操作

- `append()`: 要素をリストの末尾に追加する。
- `extend()`: 他のリストやイテラブルから要素を追加する。
- `remove()`: 指定した要素をリストから削除する。
- `pop()`: 指定した位置の要素をリストから削除し、その要素を返す。
- `index()`: 指定した要素の位置を返す。
- `sort()`: リストをソートする。

## タプル (Tuple) とは

タプルは、リストと似ているが、一度作成すると変更ができない不変の順序付けられた要素のコレクションである。

### タプルの生成

タプルは、丸括弧 `()` を使用して要素を定義することで作成できる。

```python
tuple1 = (1, 2, 3, 4)
tuple2 = ("apple", "banana", "cherry")
```

シンプルなアサインメントでも作成できる:

```python
tuple3 = 1, 2, 3
```

### 主な操作

タプルは不変であるため、要素を追加したり、削除したりすることはできない。しかし、以下のような基本的な操作は可能である:

- インデックスを使って要素にアクセスする。
- `index()`: 指定した要素の位置を返す。
- `count()`: 指定した要素の数をカウントする。

## 両者の違い

1. **変更の可否**: リストは変更可能（ミュータブル）で、タプルは変更不可能（イミュータブル）である。
2. **記法**: リストは `[]` で、タプルは `()` で定義される。
3. **用途**: タプルは変更されるべきでないデータを保持するのに適している。リストはデータが動的に変わる場合や操作が頻繁に行われる場合に適している。

### まとめ

リストとタプルは、Pythonでの順序付けられたデータの表現に非常に便利である。リストは変更が頻繁に行われるデータを扱うのに適しており、タプルは不変のデータを保持するのに適している。