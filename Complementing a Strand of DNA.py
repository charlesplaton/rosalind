fhandle = open(input())
text = fhandle.read()
fhandle.close()

seq = ""

for x in text:
    if x == "A":
        seq = "T" + seq
    elif x == "T":
        seq = "A" + seq
    elif x == "C":
        seq = "G" + seq
    elif x == "G":
        seq = "C" + seq

print(seq)