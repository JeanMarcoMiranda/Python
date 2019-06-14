nums = []
npar = 0
nimp = 0
for i in range(0, 8):
    num = int(input("Ingresar un número: "))
    nums.append(num)

for i in nums:
    
    if i % 2 == 0:
        npar += 1
    else:
        nimp += 1

print("Números pares: ",npar,"\n"+
      "Números impares: ",nimp)