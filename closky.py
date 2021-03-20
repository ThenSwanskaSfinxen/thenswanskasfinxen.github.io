"""
def int_to_se(num):
    d = { 0 : 'noll', 1 : 'ett', 2 : 'två', 3 : 'tre', 4 : 'fyra', 5 : 'fem',
          6 : 'sex', 7 : 'sju', 8 : 'åtta', 9 : 'nio', 10 : 'tio',
          11 : 'elva', 12 : 'tolv', 13 : 'tretton', 14 : 'fjorton',
          15 : 'femton', 16 : 'sexton', 17 : 'sjutton', 18 : 'arton',
          19 : 'nitton', 20 : 'tjugo',
          30 : 'trettio', 40 : 'fyrtio', 50 : 'femtio', 60 : 'sextio',
          70 : 'sjuttio', 80 : 'åttio', 90 : 'nittio' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + 'hundra'
        else: return d[num // 100] + 'hundra' + int_to_se(num % 100)

    if (num < m):
        if num % k == 0: return int_to_se(num // k) + 'tusen'
        else: return int_to_se(num // k) + 'tusen,' + int_to_se(num % k)
numbers = []
for i in range(1, 11):
    numbers.append(int_to_se(i))

numbers = ["hundra" if x == "etthundra" else x for x in numbers]
numbers = ["tusen" if x == "etttusen" else x for x in numbers] 
for n in sorted(numbers):
    print(n + ", ", end="")
"""
"""
from num2words import num2words

numbers = []
for i in range(1, 1001):
    numbers.append(num2words(i, lang="fr"))
for n in sorted(numbers):
    print(n + ", ", end="")
"""

numbers = []
with open("engelska") as words:
    word = ""
    for line in words:
        for c in line:
            if c == ",":
                numbers.append(word)
                word = ""
            word += c
new = []
for i in numbers:
    k = i.replace(" ", "")
    k =  i.replace(",", "")
    new.append(k)

from word2number import w2n

numbers = []
for w in new:
    numbers.append(w2n.word_to_num(w))
print(len(set(numbers)))