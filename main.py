import random
array1 = [] 
for x in range(9):
  array1.append(random.randint(0, 100))
random.shuffle(array1)
print(array1[0])
print(array1[4])
print(array1[8])
array1[5] = 34
print(array1[7])
print(len(array1))
print(min(array1))
print(max(array1))
array2 = [12, 25, 47, 58, 69, 72] 
array_sum = array1 + array2
print(array_sum)
print(array2[1] + array2[5])
random.shuffle(array2)
