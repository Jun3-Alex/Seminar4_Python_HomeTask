# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
'''
my_string = 'a a a b c a a d c d d'

my_list = my_string.split()

my_dict = {}

for i in my_list:
    if i not in my_dict:
        my_dict[i] = 0
        print(i+' ',end='')
    else:
        print(i,end='')
        my_dict[i] += 1  
        print('_' + str(my_dict[i]) +' ',end='')

////////////////////////////////////////////////

start_str = 'a a a b c a a d c d d'.split()
print(start_str)

char_dict = {}
result_str = ''

for char in start_str:
    if char not in char_dict:
        char_dict[char] = 1
        result_str += f'{char} '
    else:
        result_str += f'{char}_{char_dict[char]} '
        char_dict[char] += 1
        
print(result_str)
'''

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
'''
my_str = "She sells sea shells on the sea shore \
    The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore \
    I'm sure that the shells are sea"
my_str = my_str.lower()
my_list = my_str.split()
print(my_list)
my_mn = set(my_list)
print(my_mn)
print(len(my_mn))
'''    

# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
'''
max_number = -1

while True:
    num = int(input(f'Введите неотрицательное целое число:'))
    if num == 0:
        break
    if num >= max_number:
        max_number = num
print(f'Наибольшее число:{max_number} ')
'''  











