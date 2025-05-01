import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()  # сортируем список учеников

# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']

# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}

# генерируем данные по оценкам
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for _ in range(3)]  # 3 случайные оценки
        students_marks[student][class_] = marks

# выводим получившийся словарь с оценками
def print_all_marks():
    for student in students:
        print(student)
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()

# вывод списка команд
def print_commands():
    print('''
    Список команд:
    1. Добавить оценку ученика по предмету
    2. Вывести средний балл по всем предметам по каждому ученику
    3. Вывести все оценки по всем ученикам
    4. Добавить нового ученика
    5. Добавить новый предмет для всех учеников
    6. Удалить ученика
    7. Удалить предмет у всех учеников
    8. Выход из программы
    ''')

# основной цикл программы
while True:
    print_commands()
    try:
        command = int(input('Введите команду: '))
    except ValueError:
        print("Ошибка: введите число от 1 до 8!")
        continue

    if command == 1:  # Добавить оценку ученика по предмету
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student not in students_marks or class_ not in students_marks[student]:
            print('ОШИБКА: неверное имя ученика или название предмета')
            continue
        try:
            mark = int(input('Введите оценку (1-5): '))
            if mark < 1 or mark > 5:
                print("Ошибка: оценка должна быть от 1 до 5!")
                continue
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        except ValueError:
            print("Ошибка: введите число!")

    elif command == 2:  # Средний балл по всем предметам
        print('2. Средний балл по всем предметам')
        for student in students:
            print(student)
            for class_ in classes:
                marks = students_marks[student][class_]
                avg = sum(marks) / len(marks)
                print(f'\t{class_} - {avg:.2f}')
            print()

    elif command == 3:  # Вывести все оценки
        print('3. Все оценки по всем ученикам')
        print_all_marks()

    elif command == 4:  # Добавить нового ученика
        new_student = input('Введите имя нового ученика: ')
        if new_student in students_marks:
            print('Ошибка: такой ученик уже есть!')
            continue
        students.append(new_student)
        students.sort()
        students_marks[new_student] = {}
        for class_ in classes:
            students_marks[new_student][class_] = [random.randint(1, 5) for _ in range(3)]
        print(f'Ученик {new_student} успешно добавлен!')

    elif command == 5:  # Добавить новый предмет
        new_class = input('Введите название нового предмета: ')
        if new_class in classes:
            print('Ошибка: такой предмет уже есть!')
            continue
        classes.append(new_class)
        for student in students:
            students_marks[student][new_class] = [random.randint(1, 5) for _ in range(3)]
        print(f'Предмет {new_class} добавлен для всех учеников!')

    elif command == 6:  # Удалить ученика
        student = input('Введите имя ученика для удаления: ')
        if student not in students_marks:
            print('Ошибка: такого ученика нет!')
            continue
        students.remove(student)
        del students_marks[student]
        print(f'Ученик {student} удалён!')

    elif command == 7:  # Удалить предмет
        class_ = input('Введите предмет для удаления: ')
        if class_ not in classes:
            print('Ошибка: такого предмета нет!')
            continue
        classes.remove(class_)
        for student in students:
            del students_marks[student][class_]
        print(f'Предмет {class_} удалён у всех учеников!')

    elif command == 8:  # Выход
        print('Программа завершена.')
        break

    else:
        print('Ошибка: неизвестная команда!')