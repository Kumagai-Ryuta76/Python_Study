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

"""
データ構造
コンテナ
→リスト・ディクショナリ・タプル・セトの4つが代表的

リストは[]で右辺の要素を囲い、カンマ区切りで値を並べる
変数 = [要素2, 要素2, 要素3, ・・・]
複数のデータを単にまとめて管理する場合や、順序を持つ複数のデータを管理したい場合
"""
members = ['熊谷', '鈴木', '佐藤']
# リスト全体の参照
print(members)
# リストの添字をしていして特定の要素を返す
print(members[1])

num = [10, 20, 30]
# sum(リスト)でリストの合計値を返す
total = sum(num)
# len(リスト)でリストの要素数を返す
ave = total / len(num)
print(f'合計{num}、平均{ave}')
# リスト.append(リストに追加したい値)
members.append('田中')
print(members)
# リスト.remove(リストから削除したい値)
members.remove('鈴木')
print(members)
# リスト[変更要素の添字] = 変更後の値
members[1] = '中村'
print(members)
"""
スライスによる範囲指定
リスト変数[A:B]
"""
a = [10, 20, 30, 40, 50]
# 添字1以上3未満の要素
print(a[1:3])
# 添字が2以上の全ての要素
print(a[2:])
# 添字が3未満の全ての要素
print(a[:3])
"""
負の数による指定
リスト変数[-1]
負の要素になることで末尾から数えれる
"""
# 末尾の要素を参照
print(a[-1])
# 末尾から2番目の要素を参照
print(a[-2])
"""
ディクショナリ
変数 = {キー:値1, キー:値2, キー:値3}
順序を持たない、複数のデータを見出しをつけて管理したい場合
"""
scores = {'network': 80, 'database': 90, 'security': 80}
print(scores)
# 変数名[キー]とすることでキーに付いた要素を呼び出せる
print(scores['database'])
# 要素の追加　ディクショナリ[新しいキー] = 新しい値
scores['programing'] = 90
# 要素の変更　ディクショナリ[変更したい要素のキー] = 変更後の値
scores['network'] = 95
# 要素の削除　del　ディクショナリ[削除したい要素のキー]
del scores['security']
print(scores)
# ディクショナリ.values()でキーをのぞいた値のみを取り出すことができる
total = sum(scores.values())
print(total)
"""
タプル
変数 = (値1, 値2, 値3, ....)
置き換えの可能性がない複数のデータを単にまとめて管理したい場合
※要素の追加・変更・削除不可
"""
scores = (90, 80, 60)
print(scores)
print(scores[2])
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')
# タプル内で要素が1つのみの場合は、要素の後に,をつける
b = ('a',)
print(type(b))
"""
セット
変数 = {値1, 値2, 値3,...}
重複した値の格納不可
添字の概念がないため順番がない
append関数ではなくadd関数で追加を行う
"""
scores = {90, 70, 60, 50}
scores.add(50)
print(scores)
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')
"""
コンテナの応用
list関数：渡された物をリストに変換する
tuple関数：渡された物をタプルに変換する
set関数：渡された物をセットに変換する
"""
scores = {'network': 60, 'database': 80, 'security': 60}
members = ['マツダ', 'アサギ', 'クドウ']
# リストmembersをタプルに変換して表示
print(tuple(members))
# scoresのキーをリストに変換して表示
print(list(scores))
# scoresの値をセットに変換して表示
print(set(scores.values()))
"""
コンテナのネスト
"""
# ディクショナリの中にディクショナリをネスト
kumagai_scores = {'network': 90, 'database': 85, 'programing': 95}
suzuki_scores = {'network': 95, 'database': 75, 'programing': 80}
members_scores = {
    '熊谷': kumagai_scores,
    '鈴木': suzuki_scores
}
# ディクショナリの中にセットをネスト
members_hobbies = {
    '熊谷': {'映画', 'ゲーム', 'キャンプ'},
    '鈴木': {'お酒', '筋トレ', 'クラブ', 'ゲーム'}
}
print(members_hobbies)
print(members_hobbies['熊谷'])
print(members_hobbies['鈴木'])
"""
2次元リスト：リストの中にリストを入れたもの
"""
a = [1, 2, 3]
b = [2, 3, 4]
c = [a, b]
# リストc斬隊を参照
print(c)
# リストのcの0番目（リストa）だけを参照
print(c[0])
# リストcの1番目（リストb）の2番目だけ参照
print(c[1][2])
"""
集合演算
セットのみで使える機能
セット1 | セット2　和集合
セット1 & セット2　積集合
セット1 - セット2　差集合
セット1 ^ セット2　対象差
"""
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)
"""
if文
if 条件式:
    条件が成立した時の処理（1ブロック)
else:
    条件が成り立たなかった時の処理（elseブロック）
"""
score = input('点数を入力してください')
if int(score) > 60:
    print('合格です！')
else:
    print('不合格です。')
    print('追試を受けてください。')
"""
比較演算子
== 右辺左辺は等しい
!=　右辺左辺は等しくない
<　右辺は左辺より大きい
>　右辺は左辺より小さい
<=　右辺は左辺以上
>=　右辺は左辺以下
in 右辺に左辺は含まれているか
"""
name = input('あなたの名前は？')
print(f'{name}さん、こんにちは')
food = input(f'{name}さんの好きな食べ物は？')
if 'カレー' in food:
    print('素敵です。カレーは最高です。')
else:
    print(f'私も{food}が好きです。')
