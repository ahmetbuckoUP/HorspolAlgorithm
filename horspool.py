from itertools import product
from string import ascii_lowercase

letter = [''.join(i) for i in product(ascii_lowercase, repeat=1)]

def horspool(text,pattern):
    n = len(text)
    m = len(pattern)
    print('Texti : "{}" Paterni: "{}"'.format(text,pattern))
    letterDict = {}
    for i in letter:
        x = {'{}'.format(i):m}
        letterDict.update(x)
    count = 0
    for l in pattern:
        x={'{}'.format(l):letterDict[l]- count}
        letterDict.update(x)
        count = count + 1
    print('Tabela e inicializuar: {}'.format(letterDict))
    found = 0
    i = 0


    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j = j - 1

        if j < 0:
            found = found + 1

        i = i + m - 1

        occ = m - 2

        while occ >= 0:
            if pattern[occ] == text[i]:
                # print(pattern[occ])
                # print(text[i])
                break
            occ = occ - 1

        i = i - occ

    print('Patterni u gjet {} here'.format(found))

data = {
    'asfsafasaahmetasdadasd':'ahmet',
    'saahmetas':'ahmet',
    'asdasmetasahmetdasdahmet':'ahmet',
    'Ne shikojme filma bashke me ahmetin':'ahmet',
    'datastring':'ahmet',
}


for x in data:
    horspool(x,data[x])

