from random import randint, choice
from timeit import default_timer
from time import sleep
import os

# выбор режима работы программы
def select_mode():
    print('''
    Выберите режим работы:
    1 Тренировка
    0 Выход
    ''')

    # сделатиь проверку
    mode = input()
    return mode

def delete_same_rows(file_name):

    uniques = []

    if os.path.exists(file_name):
        with open(file_name, 'r') as f, open(f'tmp_{file_name}', 'a') as f2:

            for row in f:
                if row not in uniques:
                    uniques.append(row)
                    f2.write(row)

        os.remove(file_name)
        os.rename(f'tmp_{file_name}', file_name)


        



# функция для возврта временных окончаний
def time_endings(digit):

    digit = str(digit)
    last_digit = digit[-1]

    if last_digit == '1':
        return 'у'
    elif 1<int(last_digit)<5:
        return 'ы'
    else:
        return ''


# функция перевода времени с секунд в минуты и секунды
def seconds_convert(time_in_seconds):

    # определим кол-во. минут и секунд
    if time_in_seconds < 60:
        spent_time = f'{round(time_in_seconds)} секунд{time_endings(time_in_seconds)}'

    else:
        minutes = round(time_in_seconds) // 60  # Целое число минут, без остатка
        seconds = round(time_in_seconds) - minutes * 60  # Остаток секунд
        
        if time_in_seconds - (minutes*60) == 0:
            spent_time = f'{minutes} минут{time_endings(minutes)}'
        else:
            spent_time = f'{minutes} минут{time_endings(minutes)} и {seconds} секунд{time_endings(seconds)}'
    
    return spent_time


# функция вывода и проверки примеров
def count(name):

    question_quantity = ''  # количество вопросов
    max_answer = ''  # до скольки будем считать
    right_answers = 0  # кол-во. правильных ответов
    fails = 0  # кол-во. ошибок
    time_spent = 0  # затраченное время на ответы 

    uniques_examples = []  # список уникальных примеров
    example_number = 0  # номер примера

    while not question_quantity.isdigit():
        print('Сколько примеров ты готов решить?')
        question_quantity = input()
        if question_quantity.isdigit():
            while int(question_quantity) < 1:
                print('Введи число больше 0')
                question_quantity = input()
                while not question_quantity.isdigit():
                    print('Должна быть цифра')
                    question_quantity = input()
        else:   
            print('Должна быть цифра')
            question_quantity = input()

    while not max_answer.isdigit():
        print('До скольки будем считать? Например до 100')
        max_answer = input()
        if max_answer.isdigit():
            while int(max_answer) < 2:
                print('Введи число больше 1')
                max_answer = input()
                while not max_answer.isdigit():
                    print('Должна быть цифра')
                    max_answer = input()
        else:   
            print('Должна быть цифра')
            max_answer = input()

    col_uniques_examples = int(max_answer)**2  # количество уникальных примеров


    print('Хорошо, тогда начинаем...')

    while len(uniques_examples) < col_uniques_examples:
        
        for i in range(int(question_quantity)):

            max_answer = int(max_answer)

            first_num = randint(1, max_answer)
            second_num = randint(1, max_answer)
            sign = choice('+-')

            if sign == '-':
                while first_num < second_num:
                    first_num = randint(1, max_answer)
                    second_num = randint(1, max_answer)

            if sign == '+':
                while first_num + second_num > max_answer:
                    first_num = randint(1, max_answer)
                    second_num = randint(1, max_answer) 

            example = f'{first_num} {sign} {second_num}' 

            if example not in uniques_examples:

                uniques_examples.append(example)
                example_number += 1

                if example_number > int(question_quantity):
                    break

                print(f'Пример {example_number}:')
                student_answer = ''

                while not student_answer.isdigit():
                    print(f'Сколько будет {example}?')
                    
                    start = default_timer()  # начнём отсчёт
                    student_answer = input()
                    stop = default_timer()  # заканчиваем отсчёт
                    time_spent += stop - start

                    if not student_answer.isdigit():
                        print('Введи число!')

                student_answer = int(student_answer)

                if sign == '+':
                    right_answer = first_num + second_num

                if sign == '-':
                    right_answer = first_num - second_num

                if student_answer == right_answer:
                    print('Правильно, молодец!')
                    right_answers += 1   
                else:
                    # добавим пример в файл
                    with open(f'{name}_errors.txt', 'a') as f:
                        f.write(f'{first_num} {sign} {second_num} 3\n')

                    
                    print('Неправильно')
                    print(f'Правильный ответ: {right_answer}')
                    fails += 1
    else:
        pass  # доделать сообщение о превышении лимита

    # если нет ошибок
    if fails == 0:
        print(f'Молодец, {name}! Ты правильно ответил на все вопросы за {seconds_convert(time_spent)} ')
    else:
        print(f'Правильных ответов: {right_answers}')
        print(f'Ошибок: {fails}')
        print(f'Затраченное время: {seconds_convert(time_spent)}')    

# основной блок программы
print('Привет, меня зовут Роджер. А как тебя?')
name = input()
print(f'Приятно познакомиться, {name.title()}.')
sleep(1)
print('Давай проверим твои знания в математике.')

delete_same_rows(f'{name}_errors.txt')

while True:
    selected_mode = select_mode()
    if selected_mode == '1':
        count(name)
    elif selected_mode == '0':
        break
    else:
        pass