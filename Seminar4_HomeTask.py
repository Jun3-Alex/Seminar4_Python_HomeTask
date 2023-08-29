# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input(f'Введите количество элементов первого множества: '))
list1 = []
for i in range(n):
    list1.append(int(input("Введите элемент 1-го множества: ")))

m = int(input(f'Введите количество элементов второго множества: '))
list2 = []
for i in range(m):
    list2.append(int(input("Введите элемент 2-го множества: ")))

sort_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            if list1[i] not in sort_list:
                sort_list.append(list1[i])
sort_list.sort()
# for i in range(len(sort_list)):
#     min = i
#     for j in range (i + 1, len(sort_list)):
#         if sort_list[min] > sort_list[j]:
#             min = j
#     temp = sort_list[i]
#     sort_list[i] = sort_list[min]
#     sort_list[min] = temp
    
print(f'{list1} \n' + f'{list2} \n' + f'{sort_list}')










