a = int(input("A?"))
b = int(input("B?"))
sum = 0
if a % 2 == 0:
    while a < b:
        if sum == 0:
            a = a + 1
            sum = a
            continue
        a = a + 2
        if a > b:
            break
        sum = sum + a
else:
    while a < b:
        if sum == 0:
            sum = a
            continue
        a = a + 2
        if a > b:
            break
        sum = sum + a
print(sum)