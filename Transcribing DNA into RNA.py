fhandle = open(input())
text = fhandle.read()
fhandle.close()

seq = ""

for x in text:
    if x == "T":
        seq = seq + "U"
    else:
        seq = seq + x

print(seq)