Vi = []
Vr = []
for i in range(0,6):
    num = int(input("Introduzca un numero: "))
    Vi.append(num)

for i in range(len(Vi),0,-1):
    num = Vi[i-1]
    Vr.append(num)

print("\n"+"El vector inicial es: ",Vi,"\n"+
      "El vector resultante es: ",Vr)