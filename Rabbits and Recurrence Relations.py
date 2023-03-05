
young = 1
adult_old = 0
adult_new = 0

n = int(input('n? '))
k = int(input('k? '))

for x in range(n-1):
    adult_new = young
    young = 0
    young += adult_old * k
    adult_old += adult_new

print(adult_old+young)
