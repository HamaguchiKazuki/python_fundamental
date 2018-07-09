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

