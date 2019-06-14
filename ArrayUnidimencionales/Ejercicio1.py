
nums = []
mrepite = 0
moda = []

for i in range(0,10):
    num=int(input("Ingrese un numero: "))
    nums.append(num)

for i in nums:
    nrepite = 0
    for f in nums:
        if i == f:
            nrepite += 1
    if nrepite > mrepite:
        mrepite = nrepite

for i  in nums:
    nrepite = 0
    for f in nums:
        if i == f:
            nrepite += 1
    if nrepite == mrepite:
        existe = False
        for exst in range(0,len(moda)):
            if i == moda[exst]:
                existe = True
        if existe == False:
            moda.append(i)
        continue

if moda == nums:
    print("No existe moda")
else:
    print(moda)
