nums = []
diag1 = 0
diag2 = 0

for fill in range(0,3):
    nums.append([])
    for col in range(0,3):
        num = int(input("Introduzca un numero: "))
        nums[fill].append(num)
print(nums)

for fil in range(0,3):
    for col in range(0,3):
        if (nums[fil][col] == nums[0][0]) or (nums[fil][col] == nums[len(nums)-1][len(nums[0])-1]):
            diag1 += nums[fil][col]
        elif (nums[fil][col] == nums[0][len(nums[0])-1]) or (nums[fil][col] == nums[len(nums)-1][0]):
            diag2 += nums[fil][col]

print("La suma de la primera diagonal es: ",diag1,"\n"+
      "La suma de la segunda diagonal es: ",diag2,"\n"+
      "La suma de ambas diagonales es: ",diag1+diag2)