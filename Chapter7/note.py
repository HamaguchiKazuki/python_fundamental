import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))

unicode_test('B')
unicode_test('$')
unicode_test('\u00a2')
unicode_test('\u20ac')
unicode_test('\u2603')
place = 'café'
print(place)
unicode_test('\u00e9')

print( unicodedata.name('\u00e9') )
print( unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') )

#コードか名前で'é'を呼んでみる
place = 'caf\u00e9'
print(place)
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place)

#先に特殊文字を組み立ててみる！
u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
print(u_umlaut)

drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)

#Unicodeの文字数を数えよう！
print( len('$') )
print( len('\U0001f47b') ) #両方文字数は1だよ

snowman = '\u2603'
print( len(snowman) )
#バイトシーケンスにエンコード

ds = snowman.encode('utf-8')
print(ds, 'len=%s'%len(ds))

#例外処理
print(snowman.encode('ascii', 'ignore'))  # エンコードできないものを捨てる
print(snowman.encode('ascii', 'replace')) # エンコードできないものを'?'に置き換える
print(snowman.encode('ascii', 'backslashreplace'))  # unicode-escape形式のPython Unicode文字列を生成
print(snowman.encode('ascii', 'xmlcharrefreplace')) # Webページで利用可能なエンティティの文字列を生成

print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
#utf-8
place2 = place_bytes.decode('utf-8')
print(place2)
#ascii
#place3 = place_bytes.decode('ascii')
#print(place3)
#latin-1
place4 = place_bytes.decode('latin-1')
print(place4)
#windows-1252
place5 = place_bytes.decode('windows-1252')
print(place5)

print('%s' % 42)
print('%d' % 42)
print('%x' % 42)
print('%o' % 52)

print('%s' % 7.03)
print('%f' % 7.03)
print('%e' % 7.03)
print('%e' % 7.03)
print('%g' % 7.03)
print('%d%%' % 100)

actor = 'Richard Gere'
cat = 'Chester'
weight = 28
print("My wife's favorite actor is %s" % actor)
print("Our cat %s weighs %s pounds" % (cat, weight) )

n = 42
f = 7.03
s = 'string cheese'

#文字の表記の仕方（古いスタイル）
#ふつー
print('%d %f %s' % (n, f, s))
#最小の幅を10とし右揃え
print('%10d %10f %10s' % (n, f, s))
#最小の幅を10とし左揃え(42xxxxxxxx7.030000xxstring cheese
print('%-10d %-10f %-10s' % (n, f, s))
#最小の幅を10とし表示文字を制限
print('%10.4d %10.4f %10.4s' % (n, f, s))
#表示文字の制限
print('%.4d %.4f %.4s' % (n, f, s))
#引数を後に指定
print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))

#新しいスタイル
#ふつー
print('{} {} {}'.format(n, f, s))
#引数の順番を入れたやつ
print('{2} {0} {1}'.format(f, s, n))
#書式指定キーに名前を入れた書式
print('{n} {f} {s}'.format(n=42, f=7.03, s='string cheese'))
#辞書形式で表示する
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other')) #{0}は辞書をさす、{1}は'other'をさす
#型指定子を用いた表示
print('{0:d} {0:f} {2:s}'.format(n, f, s))
#キーワード引数で指定
print('{n:d} {f:f} {s:s}'.format(n=42, f=7.33, s='string cheese'))
#幅10で右揃え
print('{0:10d} {1:10f} {2:10s}'.format(n, f, s))
#わかりやすいバージョン右揃え
print('{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s))
#わかりやすいバージョン左揃え
print('{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s))
#中央揃え
print('{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s))
#文字数上限＊整数では使えないので注意！＊
print('{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s))
#パディング（出力フィールドのスペースを他の文字で埋める）
print('{0:!^20s}'.format('BIG SALE'))

#正規表現
print('{0:-^50s}'.format('正規表現'))
#単純なマッチング
import re
result = re.match('You', 'Young Frankenstein')
print(result.group())

#より複雑な時は先にコンパイル
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
print(result.group())

#match()はどこまでできるのか見てみる！
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())

#パターンの先頭に^を付けても同じ意味になる
m = re.match('^You', source)
if m:
    print(m.group())

#'Frank'はいけるか？
m = re.match('Frank', source)
if m:
    print(m.group())
else:
    print('no pattern')

#matchはソースが先頭にないといけないsearchは？
m = re.search('Frank', source)
if m:
    print(m.group())

#matchでもパターン検索したい！
m = re.match('.*Frank', source) # '.'は任意の一文字 '*'は任意の個数の直前のもの
if m:
    print(m.group())

# nという一文字を文章中から何個あるか探し出す
m = re.findall('n', source)
print(m)
print('Found', len(m), 'matches')

#nの後ろに任意の１文字が続く
m = re.findall('n.', source)
if m:
    print(m)

#文字の最後にあるnもマッチさせる
m = re.findall('n.?', source)
if m:
    print(m)

#splitの分割機能
print(source)
m = re.split('n', source)
print(m)

#subによるマッチした部分の置換
m = re.sub('n', '?', source)
print(m)

#stringモジュールを使ってみよう
import string
printable = string.printable
print(len(printable) )
print(printable[0:50])
print(printable[50:])

#printableの中の数字はどれか
print(re.findall('\d', printable))

#printableの中で数字、英字、アンスコを表示
print(re.findall('\w', printable))

#空白文字を表示
print(re.findall('\s', printable))

#ASCII以外も検索一致は使えるの？
x = 'abc' + '-/*' + '\u00ea' + '\u0115'
print(re.findall('\w', x))

#メタ文字
source = '''I wish I may, I wish I might Have a dish of fish tonight.'''
print(source)

#任意の位置にあるwishを探索
print(re.findall('wish', source))

#任意の位置にあるwishかfishを探索
print(re.findall('wish|fish', source))

#先頭でwishを探索
print(re.findall('^wish', source)) # ^はサーチ文字列を先頭に固定

#先頭でI wishを探索
print(re.findall('I wish', source))

#末尾でfishを探す
print(re.findall('fish', source))

#末尾でfish tonight.を探索
print(re.findall('fish tonight.$', source)) # $はサーチ文字列を末尾に固定 .$は行末のピリオドを含んだ文字にマッチする

#より正確にマッチさせるためにエスケープ文字'\'を使う
print(re.findall('fish tonight\.$', source))

# wかfの後にishが続いている単語を探索
print(re.findall('[wf]ish', source))

# w, s, hのどれかが１個以上続いているところを探索
print(re.findall('[wsh]+', source))

#ghtの後ろに英数文字以外の単語が続いているところを探索
print(re.findall('ght\W', source))

# I （Iとスペース）の後ろにwishが続くところを探索
print(re.findall('I (?=wish)', source))

# wishの前にI (Iとスペース）があるところを探索
print(re.findall('(?<=I) wish', source))

#正規表現の中でもPythonと矛盾を引き起こすところがある
print(re.findall('\bfish', source))
#[]となる

#\bはバックスペースの意味を持つエスケープ文だよね！
#そうゆう時は'r'を追加してエスケープを無効化しましょ
print(re.findall(r'\bfish', source))

#マッチした文字列の出力指定

m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
#タプルで表示
print(m.groups())

#グループ別に保存していく
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))

#バイナリデータ

#bytes変数とbytearrayの作成
blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)
the_bytes_array = bytearray(blist)
print(the_bytes_array)

#bytesを文字で表示
print(b'\x61')
print(b'\x01abc\xff')

#bytearrayはミュータブルだから変更できるよ！（bytesはイミュータブルです）
the_bytes_array[1] = 127
print(the_bytes_array)

#0~255までの256個のオブジェクトを作る
the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))
print(the_bytes)

#structを用いたバイナリデータの変換
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

print(len(valid_png_header))

#dataの長さと各値に置けるデータの増え方
for x in range(1, len(data)):
    print(x-1, ":", data[x-1:x])

print(struct.pack('>L', 154))
print(struct.pack('>L', 141))

print(struct.unpack('>2L', data[16:24]))

# 16x 16バイトを読み飛ばす 2L 2個の符号なし調整数を読み出す 6x最後の6バイトを読み飛ばす
print(struct.unpack('>16x2L6x', data))

#外部パッケージのconstructをインストール
#最新バージョンconstruct(v2.9.45)では使えない
# from construct import *
# fmt = Struct('png',
#              Magic(b'\x89PNG\r\n\x1a\n'),
#              UBInt32('length'),
#              Const(String('type', 4), b'IHDR'),
#              UBInt32('width'),
#              UBInt32('height')
#              )
# result = fmt.parse(data)
# print(result)
# print(result.width, result.height)

#binasciiの利用
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))

#逆方向の変換
print(binascii.unhexlify(b'89504e470d0a1a0a'))

#ビット演算子
a = 0b0101
b = 0b0001
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)
