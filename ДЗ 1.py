
name = input("Введите ФИО")
year = int(input("Введите год вашего рождения"))
age = 2022 - year
print(name,"вам сейчас",age)




t = int(input("Введите время в сек: "))
a = t // 3600
a = round(a,0)
b = t // 60
b = round(b,0)
c = (t / 60 - b) * 60
c = round(c)
print(f"{a:02}:{b:02}:{c:02}")




a = input("Введите число n: ")
result1 = a + a + a
result2 = a + a
result3 = a
summ = int(result1) + int(result2) + int(result3)
print(summ)




a = int(input("Введите любое число"))
min = a % 10
max = min
while a > 0:
    b = a % 10
    if b >= max:
        max = b
    elif b <= min:
        min = b
    a = a // 10
print(max,"- Макс число")
print(min,"- Мин число")





a = int(input("Введите вашу выручку:  "))
b = int(input("Введите издержки:  "))
if a > b:
    c = a - b
    print("Ваша прибыль", c)
elif a < b:
    c = b - a
    print("Убыток фирмы:", c)
else:
    print("ваша выручка = 0")





a = int(input("Введите км:  "))
b = int(input("Введите макс число км: "))
c = a
n = 1
while c <= b:
    c = c + c * 0.1
    c = round(c,2)
    print("На",n,"день вы пробежали",c,"километра")
    n = n + 1
else:
    print("Ддя достиженя",b,"кмлометров вам понадобилось",n,"дней")












