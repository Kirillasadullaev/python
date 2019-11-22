from random import randint, choice
from timeit import default_timer
from time import sleep


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
def count():

    question_quantity = ''  # количество вопросов
    max_answer = ''  # до скольки будем считать
    right_answers = 0  # кол-во. правильных ответов
    fails = 0  # кол-во. ошибок
    time_spent = 0  # затраченное время на ответы 

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

    print('Хорошо, тогда начинаем...')

    for question in range(int(question_quantity)):

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

        print('Пример ' + str(question+1) + ':')


        student_answer = ''

        while not student_answer.isdigit():
            print('Сколько будет ' + str(first_num) + sign+  str(second_num) +'?')
            
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



while True:
    selected_mode = select_mode()
    if selected_mode == '1':
        count()
    elif selected_mode == '0':
        break
    else:
        pass