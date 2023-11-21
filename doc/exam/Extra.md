# Python 3上級者向けテクニックとサンプルコード

目次

- [制御フロー](#制御フロー)
- [データ構造](#データ構造)
- [例外処理](#例外処理)
- [入出力](#入出力)
- [クラス](#クラス)
- [ラムダ](#ラムダ式)
- [json](#jsonの操作)
- [ジェネレータとイテレータ](#ジェネレータとイテレータ)
- [デコレータ](#デコレータ)
- [コンプリヘンション](#コンプリヘンションを使った辞書とセット)
- [コンテキストマネージャ](#コンテキストマネージャとwithステートメント)

---

## 制御フロー

### リスト内包表記の応用

#### テクニック
- リスト内包表記はループよりも効率的で読みやすいリスト操作を可能にする。
- 複数のリストから新しいリストを作成する際に特に便利。

#### サンプルコード
```python
# 2次元配列の転置
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```
このコードは、与えられた行列の転置を行っている。各列を行に変換している。

---

## データ構造

### 辞書内包表記

#### テクニック
- 辞書内包表記を使うと、キーと値のペアから辞書を簡単に作成できる。
- リストや他の辞書から辞書を生成する場合に有用。

#### サンプルコード
```python
# リストから辞書を生成
keys = ['name', 'age', 'gender']
values = ['Alice', 25, 'Female']

dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary)  # {'name': 'Alice', 'age': 25, 'gender': 'Female'}
```
ここでは、2つのリストから辞書を生成している。リストのインデックスを使ってキーと値のペアを作成している。

---

## 例外処理

### 例外チェーンの利用

#### テクニック
- Pythonでは、一つの例外を処理中に別の例外が発生した場合、最初の例外を第二の例外に「チェーン」することができる。
- これにより、エラーの原因をより明確に追跡できる。

#### サンプルコード
```python
# 例外チェーンの例
try:
    file = open('non_existent_file.txt')
except FileNotFoundError as e:
    raise RuntimeError("ファイルの読み込みに失敗") from e

# RuntimeError: ファイルの読み込みに失敗
# The above exception was the direct cause of the following exception:
# FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file.txt'
```
このコードは、ファイルが存在しない場合の`FileNotFoundError`をキャッチし、それを`RuntimeError`に「チェーン」している。

---

## 入出力

### コンテキストマネージャの応用

#### テクニック
- `with`ステートメントはファイル操作だけでなく、リソースの確保と解放にも使える。
- これにより、リソースリークを防ぐことができる。

#### サンプルコード
```python
# ファイル操作以外でのwithステートメントの使用
class ManagedResource:
    def __enter__(self):
        print("リソース確保")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("リソース解放")

with ManagedResource() as resource:
    print("リソース使用中")

# リソース確保
# リソース使用中
# リソース解放
```
このクラスはコンテキストマネージャとして機能し、`with`ブロックに入るときにリソースを確保し、ブロックを抜けるときに解放する。

## クラス

### メタクラスの使用

#### テクニック
- メタクラスはクラスの動作をカスタマイズするのに使える。
- クラスの作成時に特定の属性やメソッドを強制するのに便利。

#### サンプルコード
```python
# メタクラスの例
class Meta(type):
    def __new__(cls, name, bases, dct):
        if 'class_id' not in dct:
            dct['class_id'] = name.lower()
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    x = 5

print(MyClass.class_id)  # myclass
```
このメタクラスは、新しいクラスが`class_id`属性を持っていない場合、クラス名の小文字版を自動的に`class_id`として追加する。

了解しました。ラムダ式（自作関数）、リスト内包表記、そしてJSONの操作に関するテクニックを追加します。

---

## ラムダ式

### ラムダ式の利用

#### テクニック
- ラムダ式は無名関数を作成するために使われ、小さな関数を一時的に必要とする場合に便利。
- ソートやフィルタリングのカスタム関数としてよく用いられる。

#### サンプルコード
```python
# リストの要素を2倍にするラムダ式
doubler = lambda x: x * 2
print(doubler(5))  # 10

# リストを特定の条件でフィルタリング
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
```
---

## JSONの操作

### JSONデータの扱い

#### テクニック
- Python標準ライブラリの`json`モジュールを使用して、JSONデータの読み書きができる。
- 辞書型とリスト型をJSON形式の文字列に変換したり、その逆の操作が可能。

#### サンプルコード
```python
import json

# 辞書をJSON文字列に変換
data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)  # {"name": "Alice", "age": 25, "city": "New York"}

# JSON文字列を辞書に変換
decoded_data = json.loads(json_string)
print(decoded_data['age']) # 25
```
---

## ジェネレータとイテレータ

### ジェネレータの利用

#### テクニック
- ジェネレータは一度に一つの値を生成する反復可能オブジェクトで、メモリ効率が良い。
- `yield`キーワードを使用して、関数の実行を一時停止し、値を返す。

#### サンプルコード
```python
# 範囲内の奇数を生成するジェネレータ
def odd_numbers(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

for num in odd_numbers(10):
    print(num)  # 1, 3, 5, 7, 9
```

---

## デコレータ

### デコレータの応用

#### テクニック
- デコレータは関数やメソッドを変更せずに、その振る舞いを拡張するために使用される。
- ログ出力、パフォーマンス測定、アクセス制御などに有用。

#### サンプルコード
```python
# 実行時間を測定するデコレータ
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result
    return wrapper

@timer
def long_running_function():
    time.sleep(2)

long_running_function()  # long_running_function took 2.0 seconds
```

---

## コンプリヘンションを使った辞書とセット

### 辞書とセットのコンプリヘンション

#### テクニック
- 辞書とセットもリスト同様にコンプリヘンションを使用できる。
- 複雑な構造の辞書やセットを簡潔に作成するのに役立つ。

#### サンプルコード
```python
# 二つのリストから辞書を作成
keys = ['name', 'age', 'gender']
values = ['Alice', 30, 'Female']
dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary)  # {'name': 'Alice', 'age': 30, 'gender': 'Female'}

# リストからセットを作成
numbers = [1, 2, 2, 3, 3, 3]
unique_squares = {x**2 for x in numbers}
print(unique_squares)  # {1, 4, 9}
```

---

## コンテキストマネージャと`with`ステートメント

### コンテキストマネージャのカスタム実装

#### テクニック
- コンテキストマネージャは、リソースの確保と解放を自動化するために使用される。
- `__enter__` と `__exit__` メソッドを持つクラスを作成することで、カスタムコンテキストマネージャを実装できる。

#### サンプル

コード
```python
# カスタムコンテキストマネージャ
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    f.write('hello, world!')

# hello.txtに 'hello, world!' が書き込まれる
```
