# Задание 5
# Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.
class Stationery():

    def __init__(self, title):
        self.title = title
        print(f'Создан новый объект класса Stationary \n {self.title}\n')

    def Draw(self):
        print('Запуск отрисовки для родительского класса\n')

class Pen(Stationery):
    def Draw(self):
        print('Запуск отрисовки для дочернего класса Pen\n')

class Pencil(Stationery):
    def Draw(self):
        print('Запуск отрисовки для дочернего класса Pencil\n')

class Handle(Stationery):
    def Draw(self):
        print('Запуск отрисовки для дочернего класса Handle\n')

new_stationary = Stationery('Здесь должен быть title для вызова родительского класса')
new_stationary.Draw()

new_pen = Pen('Здесь должен быть title для вызова дочернего класса Pen')
new_pen.Draw()

new_pencil = Pencil('Здесь должен быть title для вызова дочернего класса Pencil')
new_pencil.Draw()

new_handle = Handle('Здесь должен быть title для вызова дочернего класса Handle')
new_handle.Draw()