#список,типы данных
#задание 1
my_list = [1, 3.4, {"Максим", "Роман", "Алиса"}, ("Максим", "Роман", 5), ["Максим", "Роман", "Алиса"], False, True, 'str']
for i in my_list:
    print(type(i))

#задание 2
friends = input("Впишите имена своих друзей: ").split()
res1 = len(friends)
print(res1)
a = res1 % 2
if a == 0:
    for i in range(0, res1, 2):
        friends[i],friends[i + 1] = friends[i + 1], friends[i]
    print(friends)
elif a == 1:
    for i in range(0, res1-1, 2):
        friends[i],friends[i + 1] = friends[i + 1], friends[i]
print(friends)


#задание 3
month = input("введите месяц в формате числа mm: ")
mm = month[0:2]
month_dict = {
'01': 'зима',
'02': 'зима',
'03': 'весна',
'04': 'весна',
'05': 'весна',
'06': 'лето',
'07': 'лето',
'08': 'лето',
'09': 'осень',
'10': 'осень',
'11': 'осень',
'12': 'зима'
}
if month in month_dict:
    print(list((month, month_dict[mm])))
else:
    print('Некорректно введен месяц')

#задание 4
stroka = input("Введите любую строку")
lis = stroka.split()
print(lis)
i = 0
while i < len(lis):
    elem = lis[i]
    print(i+1,elem[0:10])
    i = i+1
# Возможно в задании опечатка и требуется найти количество слов в строке, а не строк ведь пользователь вводит одну строку?

# задание 5
my_list = [6,5,3,3,2]
print(max(my_list))
i = 0
while i < len(my_list):
      a = int(input("Введите а "))
      if a > max(my_list):
        my_list.insert(0, a)
        print(my_list)
      elif a in my_list:
        my_list.insert(my_list.index(a), a)
        print(my_list)
      elif a < min(my_list):
        my_list.append(a)
        print(my_list)
      else:
        my_list.insert(my_list.index(a - 1), a)
        print(my_list)
      b = int(input("Если продолжаем нажмите-1,для выхода нажмите любую кнопку"))
      if b == 1:
         continue
      else:
             break

# задание 6
products = []
i = 0
n = int(input('Введите количество наименований'))
while i < n:
    name = input('Введите наименование товара ')
    price = int(input('Введите цену '))
    qty = int(input('Введите количество товара '))
    measure = input('Введите еденицу измерения ')
    products.append((i, {'наименование': name, 'цена': price, 'количество': qty, 'еденица измерения': measure}))
    i = i + 1
print(products)
products_dict = {'наименование': [],'цена': [],'количество': [], 'еденица измерения': []}
for product in products:
    products_dict['наименование'].append(product[1]['наименование'])
    products_dict['цена'].append(product[1]['цена'])
    products_dict['количество'].append(product[1]['количество'])
    products_dict['еденица измерения'].append(product[1]['еденица измерения'])
print(products_dict)
