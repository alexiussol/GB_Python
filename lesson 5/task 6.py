# Задача 6
#Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
#учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
#Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
#были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по
#нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def calculate_hours(file_path):
    result = {}
    try:
        with open('lessons.txt', 'r', encoding="utf-8") as f:
            for line in f:
                subject, numbers = line.split(':')
                subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
                result[subject] = subject_sum
    except Exception as err:
        print('Unexpected error:', err)
    return result


if __name__ == '__main__':
   from pprint import pprint
   res_dict = calculate_hours('lessons.txt')
   pprint(res_dict,indent = 10,width = 1)


