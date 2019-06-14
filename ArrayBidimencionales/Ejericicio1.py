alumnos = []

for fil in range(0,1):
    alumnos.append([])
    for col in range(0,4):
        if col == 0:
           nom = input("Ingresar nombre de alumno: ")
           alumnos[fil].append(nom)
        else:
            nota = float(input("Ingrese una nota del alumno: "))
            alumnos[fil].append(nota)
print(alumnos)

print("\n"+"Ingrese el número 1 si quiere buscar la nota del alumno"+"\n"
      "Ingrese el número 2 para modificar la nota de un alumno"+"\n"
      "Ingrese el número 3 para calcular el promedio de las notas de un alumno"+"\n")

opcion = int(input("Ingrese la opcion que desea ejecutar: "))

if opcion == 1:
    alum = input("Ingrese el nombre del alumno que desea buscar: ")
    for i in range(0, len(alumnos)):
        if alumnos[i][0] == alum:
            for col in range (1,len(alumnos[0])):
                print(alumnos[i][col])
elif opcion == 2:
    alum = input("Ingrese el nombre del alumno que desea buscar: ")
    nota = int(input("Ingrese el numero de la nota que desea modificar: "))
    for fil in range(0,len(alumnos)):
        if alumnos[fil][0] == alum:
            alumnos[fil][nota] = float(input("Ingrese la nueva nota: "))
            print(alumnos[fil])
            break         
elif opcion == 3:
    alum = input("Ingrese el nombre del alumno que desea buscar: ")
    promedio = 0
    for fil in range(0,len(alumnos)):
        if alumnos[fil][0] == alum:
            for col in range (1,len(alumnos[0])):
                promedio += alumnos[fil][col]
            break
    print("Su promedio es de: ",promedio/3)
else:
    print("Introdujo una opcion errornea")