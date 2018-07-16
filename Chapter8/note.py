#Python文字列からファイルを作って呼び出す
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way
And returned on the previous night.
'''
print(len(poem))

#writeで保存
fout = open('relativity', 'wt')
print(fout.write(poem))
fout.close()

#printで保存
fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()

#printの機能を制限する
fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

#ソース文字列が大きい場合チャンクを分けて書き込む
fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(poem[offset:offset+chunk]))
    offset += chunk

fout.close()

#'x'を使うことで大切なファイルを壊さず上書きできる
#使い方は例外ハンドラ
try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')

#read()は大きなファイルを扱うときに注意が必要（メモリを必要分用意するため）
poem = '' #read()のため初期化
fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print('read', len(poem))

#read()による字数上限を設定しメモリを守る
poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
    print('fragment', len(fragment))

fin.close()
print('read,fragments', len(poem))

#readlene()を使った一行ずつの呼び出し
poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line: #lineが空文字列('')の時Falseが返される
        break
    poem += line

fin.close()
print('read,line', len(poem))

#lineはイテラブルなオブジェクトなためイテレータを用いてfor文で取り出せる
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

fin.close()
print('read,イテラブル', len(poem))

#readlines()で読み出し1行文字列のリストで返す
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')

#バイナリファイルの書き込み
bdata = bytes(range(0, 256))
print(len(bdata))
fout = open('bfile', 'wb')
print(fout.write(bdata))
fout.close()

#バイナリデータをチャンク単位で書き込み
fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
    print('offset', offset)

fout.close()

#read()でバイナリファイルの読み出し
bdata = '' #初期化
fin = open('bfile', 'rb')
bdata = fin.read()
print('read', len(bdata))
fin.close()

#withによる自動クローズ機能(コンテキストマネージャー機能)
with open('relativity', 'wt') as fout:
    print('end write', fout.write(poem))

#seek()による読み書き開始位置の変更
fin = open('bfile', 'rb')
print(fin.tell())
print(fin.seek(255))
bdata = fin.read()
print(len(bdata))
print(bdata[0])

#seekの第二引数について
import os
print('seek_set', os.SEEK_SET)
print('seek_cur', os.SEEK_CUR)
print('seek_end', os.SEEK_END)

fin = open('bfile', 'rb')
print(fin.seek(-1, 2))
print(fin.tell())
bdata = fin.read()
print(len(bdata))
print(bdata[0])

#seekの移動練習(一番使用効率が高いのがバイナリデータの処理)
fin = open('bfile', 'rb')

print(fin.seek(254, 0))
print(fin.seek(1, 1))
bdata = fin.read()
print('bdata', len(bdata))
print(bdata[0])

#CSV(Comma Separated Values)データーベース
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
]

with open('villains', 'wt') as fout: #コンテキストマネージャー
    csvout = csv.writer(fout)
    csvout.writerows(villains)

# villainsを呼び出して元のデータ構造を作成
with open('villains', 'rt') as fin:
    cin = csv.reader(fin) # イテレラブルな値
    villains = [row for row in cin] # リスト内包表記を使っている

print(villains)

# 辞書の形式で呼び出し
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)

# 辞書形式で書き込み
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
]

with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

# ファイルをデータから読み直す
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print('dict villains', villains)

# XML
import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
print(root.tag)
for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

print('menuセクション数',len(root))
print('朝食の項目の数', len(root[0]))

# JSON(JavaScript Object Notation)
#サンプルデータの作成
menu = \
    {
        "breakfast": {
                "hours": "7-11",
                "items": {
                    "breakfast burritos": "$6.00",
                    "pancakes": "$4.00"
                }
            },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
        }
    }
}

# dumpsを使ったエンコード
import json
menu_json = json.dumps(menu)
print(type(menu_json))
print('json', menu_json)

# loadsを使ってPythonデータ構造に変更
menu2 = json.loads(menu_json)
print(type(menu2))
print('python struct', menu2)

# datetimeのエンコードとデコード（例外が起こる）
import datetime
now = datetime.datetime.utcnow()
print(now)
# json.dumps(now) ここで起こる
now_str = str(now)
print(json.dumps(now_str))

from time import mktime
now_epoch = int(mktime(now.timetuple()))
print(json.dumps(now_epoch))

# ちょっと変換が面倒かな・・・
# JSONのエンコード方式を継承して変えて見ましょ
class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance()はobjの型をチェックする
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        else:
            return json.JSONEncoder.default(self, obj)

json.dumps(now, cls=DTEncoder)

#YAML
import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()

data = yaml.load(text)
print(data['details'])
print('poems', len(data['poems']))

# 参照方法が[辞書][リスト][辞書]
print(data['poems'][1]['title'])

# セキュリティでの問題点

# 危険
from xml.etree.ElementTree import parse
# et = parse(xmlfile)

# 対策済み
from defusedxml.ElementTree import parse
# et = parse(xmlfile)


# 設定ファイル
import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
print(cfg)
print(cfg['french'])
print(cfg['french']['greeting'])
print(cfg['files']['bin'])

# pickleを使ったシリアライズ(直列化)
import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled) # リストで表示
print(now1)
print(now2)

# pickleを用いて独自のクラスやオブジェクトを処理する
import pickle
class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1)
print(str(obj1))
pickled = pickle.dumps(obj1) # JSON文字列にエンコード = dumps()
print('pickled:', pickled)
obj2 = pickle.loads(pickled) # JSON文字列にデコード = loads()
print(obj2)
print(str(obj2))

# SQLite
import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
if curs is None:
    curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')

# 動物のデータを追加
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

# プレースホルダーを使った方法（こっちのほうが安全）
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))

# すべての動物の情報を引き出す
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

# 個体数順にソートして取り出す(昇順)
curs.execute('SELECT * from zoo ORDER BY count')
print('昇順', curs.fetchall())

# 降順でソートする
curs.execute('SELECT * from zoo ORDER BY count DESC')
print('降順', curs.fetchall())

# 最も損失の大きい動物は？
curs.execute('''SELECT * FROM zoo WHERE
damages = (SELECT MAX (damages) FROM zoo)''')
print('損失', curs.fetchall())

# 開いたものはちゃんと閉じよう
curs.close()
conn.close()

