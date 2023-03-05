fhandle = open('rosalind_hamm.txt', 'r')
seq_list = list()
for seq in fhandle:
    seq_list.append(seq.rstrip())

hamming_dist = 0
for x in range(len(seq_list[0])):
    if seq_list[0][x] != seq_list[1][x]:
        hamming_dist += 1

fhandle.close()
print(hamming_dist)