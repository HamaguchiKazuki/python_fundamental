#7-1
import unicodedata
mystery = '\U0001f4a9'
print(mystery)
print(unicodedata.name(mystery))

#7-2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

#7-3

