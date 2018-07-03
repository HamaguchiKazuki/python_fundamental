"""名前付きタプル：タプルの子クラスで位置および名前でもアクセスできる"""
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

#辞書からも作れる
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)# duck2 = Duck(bill = 'wide orange', tail = 'long'　と同じ意味
print(duck2)

#別の名前付きタプルなら値を変えれる

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

#名前付きタプルは辞書と似たような動きができるが値を追加することはできない

duck_dict = {'bill': 'wide orage', 'tail': 'long'}
print(duck_dict)

#辞書にフィールドは追加できる

duck_dict['color'] ='green'
print(duck_dict)

#これはできない

try:
    duck_dict.color = 'green'
except:
    print('これが表示されてなかったらおたくやばいね')
