# Задание 5.
# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

f = open('file_task_05.txt', 'w', encoding="utf-8")
print("Введите набор чисел, разделенных пробелами: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f = open('file_task_05.txt', 'r', encoding="utf-8")
list = f.read().split()
list = [int(i) for i in list]
sum = 0
for i in range(len(list)):
    sum += list[i]
print('Сумма элементов равна: ',sum)
f.close()
