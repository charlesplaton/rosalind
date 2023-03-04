fhandle = open(input())
text = fhandle.read()
fhandle.close()

a = 0
c = 0
g = 0
t = 0

for x in text:
    if x == "A":
        a += 1
    elif x == "C":
        c += 1
    elif x == "G":
        g += 1
    elif x == "T":
        t += 1

print(a, c, g, t)