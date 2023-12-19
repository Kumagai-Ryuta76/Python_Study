"""
print関数　→　画面に出力する関数
"""
print('Hello, World!!')
print('熊谷の学習スタート！')
print('28歳')
print('Web開発エンジニア目指して勉強中！')

# 数値の場合は''は不要
print(10)
print(-100)

# print()の中で計算することも可能
# 加算
print(1 + 2)
# 減算
print(100 - 50)
# 乗算
print(10 * 5)
# 除算
print(7 / 4)
# 割り算の章
print(7 // 4)
# 割り算の余り
print(7 % 4)
# 累乗
print(2 ** 3)

"""
数値リテラル　＝　1 10 20
文字列リテラル　＝　'Hello' "World"
"""
# 文字列の結合になる
print('1' + '1')
# 文字列の反復
print('やあ' * 3)
print('Python' + 'の世界へようこそ')
print('Pythonは' + 'とっても' * 3 + '楽しいですよ')

"""
エスケープシーケンス
\n = 改行
\\ = バックスラッシュ
\' = シングルクォーテーション
\" = ダブルクォーテーション
"""
# 改行なし
print('はじめまして熊谷です体を動かすのが好きです')
# 改行あり
print('はじめまして\n熊谷です\n体を動かすのが好きです')
# エスケープシーケンスで'と"を表示
print('引用符には\'と\"があります')
# ヒアドキュメントは'''で囲む構文でprint()を使うと画面に表示される
print('''初めまして
熊谷です
体を動かすのが好きです''')
# ヒアドキュメントの前後の改行を取り除く
print('''
初めまして
熊谷です
体を動かすのが好きです
'''.strip())

"""
オペランドを演算子の左右に記述する
周囲を巻き添えにして化ける
優先順位順で評価される
高= **
中= * / %
低= + -
"""
print(1 + 2 - 2 * 1 / 2 % 2 ** 5)

"""
変数の利用
値を入れておく箱のイメージ
変数の代入　変数名:XXX = 値:YYY
参照　　　　変数名
※変数名のルール
予約後禁止
先頭文字に数字不可
先頭にアンスコをつけた名前は原則使用しない
大文字小文字全角半角は区別される
小文字で始まるわかりやすいものが望ましい
"""
name = '熊谷'
age = 28
print(name)
print(age)

print('半径が3cmの円の直径は、')
dia = 3 * 2
print(dia)
print('その円の円周の長さは')
print(dia * 3.14)

# 変数は上書き可能　原則として変数は再利用しない
name = '隆太'
print(name)
"""
複数単語を繋げる変数名にはいくつか方法がある
アッパーキャメル : MyAge
ロワーキャメル : myAge
⭐︎スネークケース : my_age
チェインケース : my-age
スネークケースがpythonでは推奨されている
"""

"""
アンパック代入
まとめて変数に代入することが可能
XXX, YYY = XXX, YYY
"""
name, age = '隆太', 28
print(name)
print(age)

"""
自身への代入
num = 1
num = num + 1
num = num + 1
num = num + 1
numに追加され続け最終的にnumは4となる
"""
num = 1
num = num + 1
num = num + 1
num = num + 1
print(num)

"""
算術演算子と代入演算子を合わせてものが複合代入演算子
+=　右辺の値と左辺の変数を足し算して代入
-=　右辺の値と左辺の変数を引き算して代入
*=　右辺の値と左辺の変数をかけ算して代入
/=　右辺の値と左辺の変数を割り算して代入
"""
age = 24
age += 1
print(age)

num = 2600
num *= 1.5
print(num)

"""
input関数
変数名 = input(文字列)
変数名を画面に表示しキーボード入力をもって値を代入する
"""
name = input('あなたの名前は？')
print('おお' + name + 'よ、よくぞ参られた')

"""
データ型
int　整数
float　少数
str　文字列
bool　真偽値
type関数　type()でデータ型を確認できる
"""
# 文字列型
x = '熊谷'
print(type(x))
print(x)
# int型
x = 23
print(type(x))
print(x)
# float型
x = 175.6
print(type(x))
print(x)

"""
データ型の変換
int関数　int(x)
float関数　float(x)
str関数　str(x)
bool関数　bool(x)
"""
# int関数で整数型を変換
x = 3.14
y = int(x)
print(y)
print(type(y))
# str型で文字列型へ変換
z = str(x)
print(z)
print(type(z))

"""
format関数 '{}を含む文字列'.format(埋め込む値1,埋め込む値2...)
埋め込む値の順は{}の順番
"""
name = '熊谷隆太'
age = 28
height = 186.5
print('私の名前は{}で、年齢は{}歳で、身長は{}cmです。'.format(name, age, height))

"""
関数には2タイプある
関数名()~で呼び出すもの(print関数,input関数)
値.関数名()~で呼び出すもの(format関数)
"""
price = input('お会計は')
# 入力値を整数型に変換
price = int(price)
number = input('人数を入力')
# 入力値を整数型に変換
number = int(number)
payment = price / number
# 計算結果を整数型に変換
payment = int(payment)
# 同じ型にしなければ演算ができないために文字列型へ変換する
print('お会計は{}円です'.format(payment))

"""
f-string
f'{}を含む文字列'
fをつけるとpythonがf-stringとして認識し、{}の中に変数や式、関数を記述できる
"""
name = '熊谷隆太'
age = 28
height = 186.5
print(f'私の名前は{name}で、年齢は{age}歳で、身長は{height/100}mです。')

height = input('身長を入力')
height = int(height)
weight = input('体重を入力')
weight = int(weight)
bmi = weight / height / height
bmi = int(bmi * 10000)
print(f'BMIは{bmi}です。')
