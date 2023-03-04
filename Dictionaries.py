fhandle = open(input("What file?"))
output = open("output.txt", "w")
text = fhandle.read()
ls = text.split()
dic = dict()
for k in ls:
    dic[k] = dic.get(k, 0) + 1
for v,k in dic.items():
    output.write(v+" "+str(k)+"\n")