import re
fhandle = open(input('File? '))

seq = ''
prev_name = ''
sequences = dict()

for x in fhandle:
    x = x.rstrip()
    if x.startswith('>') == True:
        x = x[1::]
        if prev_name == '':
            prev_name == x
        if seq != '':
            sequences[prev_name] = seq
        sequences[x] = ''
        prev_name = x
        seq = ''
    else:
        seq = seq + x
sequences[prev_name] = seq


highestGC = 0
highestName = ''
for name,code in sequences.items():
    amount = 0
    length = 0
    for letter in code:
        if letter == 'C' or letter == 'G':
            amount += 1
            length += 1
            continue
        length += 1
    gc_content = (amount / length) * 100
    if gc_content > highestGC:
        highestGC = gc_content
        highestName = name

print(highestName)
print(highestGC)