#2 Задание
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
#нуля в качестве делителя программа должна корректно обработать эту ситуацию и
#не завершиться с ошибкой.


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на нуль нельзя")


div = DivisionByNull(50, 250)
print(DivisionByNull.divide_by_null(250, 0))
print(DivisionByNull.divide_by_null(250, 50))
print(div.divide_by_null(100, 0))