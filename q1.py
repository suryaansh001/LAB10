import string

h = str(input())
l = ["A", "E", "I", "O", "U", "a", "u", "i", "e", "o"]
d = {}
c = 0

for i in h:
    for p in l:
        if i == p:
            c += 1
            if p in d:
                d[p] += 1
            else:
                d[p] = 1

print(d)
