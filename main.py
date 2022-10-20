def bubble_sort(mas):
    length = len(mas)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if mas[j] > mas[j + 1]:
                temp = mas[j]
                mas[j] = mas[j + 1]
                mas[j + 1] = temp

m = []

n = int(input("Array length: "))
for i in range(0, n):
    element = int(input("arr[" + str(i + 1) + "] = "))
    m.append(element)

bubble_sort(m)
napr = int(input("По возрастанию - 0, по убыванию - 1: "))
if napr == 1:
    m.reverse()
print("Sorted array: ")
print(m)