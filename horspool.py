def horspool(text,pattern):
    found = 0
    i = 0
    m = len(pattern)
    n = len(text)
    print('Texti : "{}" Paterni: "{}"'.format(text,pattern))

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

