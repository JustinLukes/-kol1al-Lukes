import random  # Importujte modul random

array1 = []  # udělá nový prázdný seznam s názvem array1
for x in range(9):
    array1.append(random.randint(0, 100))  # Udělá náhodná čísla mezi 0 a 100 do array1

random.shuffle(array1)  # Náhodně promíchejte prvky v array1

print(array1[0])  # Vypíše první variable array1
print(array1[4])  # Vypíše pátý variable array1
print(array1[8])  # Vypíše devátý variable array1

array1[5] = 34  # Nastavte šestý variable array1 na hodnotu 34

print(array1[7])  # Vypíše osmý variable array1

print(len(array1))  # Vypíše délku array1 (mělo by to být 9)
print(min(array1))  # Vypíše nejmenší hodnotu v array1
print(max(array1))  # Vypíše největší hodnotu v array1

array2 = []  # udělá nový prázdný seznam s názvem array2
for x in range(9):
    array2.append(random.randint(0, 100))  # Udělá náhodná čísla mezi 0 a 100 do array1

array_sum = array1 + array2  # Spojte array1 a array2 do nového seznamu array_sum
print(array_sum)  # Vypíše spojený seznam

print(array2[1] + array2[5])  # Vypíše součet druhého a šestého prvku array2

random.shuffle(array2)  # Náhodně promíchejte prvky v array2
