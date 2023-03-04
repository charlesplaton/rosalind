fhandle = open(input("file name?"))
output = open("output.txt", "w")
counter = 2
for line in fhandle:
    if counter % 2 == 0:
        counter = counter + 1
        continue
    counter = counter + 1
    output.write(line)
fhandle.close()
output.close()