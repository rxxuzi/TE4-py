# 辞書 (Dictionary) とは

辞書（Dictionary）、しばしば "dict" としても参照される、はPythonの基本的なデータ型の一つであり、キーと値のペアのコレクションを表す。
辞書は順序付けられたデータ構造であり、Python 3.7以降、要素の挿入の順序が保持される。

辞書は、キー(`key`): 値(`value`) のペアの集合であり、キーが (辞書の中で)一意でなければならない

## 辞書の生成

Pythonの辞書は、波括弧 `{}` を使ってキーと値のペアを定義することで作成できる。

```python
d = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red"
}
```

また、`dict()` コンストラクタも使用できる。

```python
d = dict(apple="red", banana="yellow", cherry="red")
```

## 主な操作

- `keys()`: 辞書のすべてのキーを返す。
- `values()`: 辞書のすべての値を返す。
- `items()`: キーと値のペアを返す。
- `get()`: 指定したキーに関連付けられている値を取得する。
- `setdefault()`: キーが存在しない場合にデフォルト値を設定する。
- `update()`: 他の辞書のキーと値を追加または上書きする。
- `pop()`: 指定したキーを持つ要素を削除し、その値を返す。

## 例

```python
d = {"apple": "red", "banana": "yellow"}
print(d["apple"])  # "red"

# キーが存在しない場合のデフォルト値の取得
print(d.get("orange", "Not Found"))  # "Not Found"

# キーと値のペアの追加
d["cherry"] = "red"

# キーと値のペアの削除
color = d.pop("banana")
```

## 特性

1. **キーの一意性**: 各キーは一意でなければならない。
2. **変更可能**: 一度作成された後も、キーと値の追加や削除が可能。
3. **様々なデータ型**: キーは変更不可能なデータ型であれば何でも良く、文字列や整数、タプルなどが使える。値には任意のデータ型が使用できる。

## まとめ

辞書は、キーと値のペアを格納するための強力で柔軟なデータ構造である。Pythonプログラムの中で頻繁に使用され、データの検索、保存、操作に非常に便利である。