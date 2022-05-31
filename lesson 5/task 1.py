# Задание 1
# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.
f = open('../personal.txt', 'w')
line = input('Введите любую строку\n')
while True:
    f.writelines(line)
    line = input('Введите любую строку\n')
    if not line:
        break
f.close()
f = open('../personal.txt', 'r')
print(f.readlines())
f.close()