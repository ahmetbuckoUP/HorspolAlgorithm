
text = ""
pattern = ""

while len(text) <= 0:
    text = input("Enter text: ")

while len(pattern) <= 0:
    pattern = input("Enter pattern: ")

# Init Data for Horspool
found = 0
i = 0
m = len(pattern)
n = len(text)

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

print('Found', found, 'matches')