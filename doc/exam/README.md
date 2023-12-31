# Python 3のテスト対策用まとめシート

## 制御フロー（Control Flow）

### 条件文（if, elif, else）

- if, elif, elseを使って条件に基づいて異なるコードブロックを実行。
- Pythonはインデントを使ってコードブロックを区別する。インデントが不適切だとエラーが発生する。

### ループ（for, while）

- forループは、リストやタプルなどの反復可能オブジェクトを通して反復する。
- whileループは、条件が真である限り繰り返す。
- breakはループを途中で終了し、continueは次のイテレーションに進む。

### 例外処理（try, except, finally）

- tryブロックで例外が発生する可能性のあるコードを囲む。
- exceptブロックで特定の例外をキャッチして処理する。
- finallyブロックは例外の有無にかかわらず実行される。

## データ構造（Data Structures）

### リスト（List）

- 可変、順序付けられた要素のコレクション。
- リスト内包表記は強力で、簡潔なコードを書くのに役立つ。

### タプル（Tuple）

- 不変で、順序付けられた要素のコレクション。
- 変更できない（immutable）ため、リストより安全で、高速。

### 辞書（Dictionary）

- キーと値のペアのコレクション。
- キーはユニークで、データを迅速に検索するのに役立つ。

### セット（Set）

- 重複しない要素のコレクション。
- 集合演算（和集合、積集合、差集合）が可能。

## モジュール（Modules）

### モジュールのインポート

- モジュールは関連する関数やクラスをグループ化したもの。
- importステートメントを使用してモジュールをインポートする。
- from ... import ... を使用して特定の関数やクラスのみをインポートする。

### 標準ライブラリ

- Pythonには多くの有用な標準ライブラリが含まれている（例：math, datetime, os）。
- 標準ライブラリを利用することで、多くの一般的なタスクを簡単に実行できる。

### パッケージの利用

- 外部パッケージを利用することで、Pythonの機能を拡張する。
- pipはPythonのパッケージ管理ツール。

## 入出力（Input/Output）

### 標準入力（Standard Input）

- `input()`関数を使ってユーザーからの入力を受け取る。
- `input()`は入力を文字列として返すため、数値を扱う場合は適切に型変換が必要。

### ファイル入出力（File Input/Output）

- `open()`関数でファイルを開く。モード（読み取り、書き込み、追加など）を指定する。
- ファイル操作後は`close()`を呼び出してファイルを閉じる。`with`ステートメントを使うと自動的に閉じる。

### 注意点

- ファイルパスは正確に指定する必要がある。間違ったパスを指定するとエラーが発生する。
- ファイルを開く際には常に例外処理（try-except）を考慮する。
- テキストファイルとバイナリファイルは異なるモードで開く必要がある（'t'と'b'）。

## クラス（Classes）

### クラスの定義

- `class`キーワードを使ってクラスを定義する。
- クラスは属性（変数）とメソッド（関数）を持つ。

### インスタンスの作成

- クラスからオブジェクト（インスタンス）を作成するには、クラス名に括弧をつけて呼び出す。
- コンストラクタ（`__init__`メソッド）はインスタンス作成時に自動的に呼び出される。

### 継承

- クラスは他のクラスから継承できる。
- 継承されたクラス（サブクラス）は親クラス（スーパークラス）の属性とメソッドを引き継ぐ。

### 注意点

- クラスメソッドの第一引数は常に`self`である。これはインスタンス自身を指す。
- クラス変数とインスタンス変数を混同しない。クラス変数はクラスのすべてのインスタンス間で共有される。
- 継承は適切に使用する。無闇に継承を多用するとコードの複雑性が増す。
- メソッドオーバーライディングをする際、親クラスのメソッドを適切に呼び出す（`super().method_name()`）。

## 躓きやすい点

1. **インデントの重要性**: インデントはPythonの構文において非常に重要。不適切なインデントは構文エラーにつながる。
2. **タプルの要素が一つの場合のカンマ**: 例：`a = (1,)`。カンマを忘れるとタプルではなく整数として扱われる。
3. **辞書のキーのユニーク性**: 辞書のキーはユニークでなければならない。重複するキーを設定すると、最後の値が保持される。
4. **モジュールの名前衝突**: インポートするモジュールの名前が既存の変数や別のモジュールと衝突すると、予期せぬエラーが発生することがある。
5. **ループと変数スコープ**: forやwhileループ内で宣言された変数は、ループの外でもアクセス可能。これが意図しない結果を引き起こすことがある。
6. **変更可能なデフォルト引数**: 関数のデフォルト引数に変更可能なオブジェクト（例：リストや辞書）を使うと、予期しない挙動を引き起こすことがある。
7. **グローバル変数とローカル変数の混乱**: グローバル変数と同じ名前のローカル変数を定義すると、スコープに関連する問題が発生することがある。
8. **型の自動変換**: Pythonは柔軟な型変換を行うが、時には予期せぬ型変換が発生し、バグの原因になることがある。
9. **文字列とバイト列の区別**: Python 3では、文字列（str）とバイト列（bytes）は明確に区別される。互換性の問題が発生することがある。
10. **リストのスライスと範囲**: リストのスライスや範囲操作は、しばしばオフバイワン（off-by-one）エラーの原因となる。
11. **クラス変数とインスタンス変数の混同**: クラス内で定義された変数は、クラス変数（全インスタンスで共有）とインスタンス変数（各インスタンスごとに異なる）がある。これらを間違えると予期せぬ挙動が発生する。
12. **継承とメソッドオーバーライドの誤解**: 継承されたメソッドをオーバーライドする際、親クラスのメソッドを適切に呼び出す必要がある（`super()`の使用）。これを怠ると、親クラスの振る舞いが失われる。
13. **例外の過度な使用**: 例外処理はエラー処理には有効だが、プログラムの通常の制御フローに使うべきではない。
14. **ファイルのクローズ漏れ**: `open()`でファイルを開いた後、適切に`close()`することが重要。`with`ステートメントを使うと自動的に閉じるため推奨される。
15. **標準入出力の誤解**: `input()`は常に文字列を返すため、数値入力の場合は適切に型変換する必要がある。また、`print()`はデフォルトで改行を行うが、これを変更することができる（`end`パラメータの使用）。
