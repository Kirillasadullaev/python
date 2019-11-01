from random import randint, choice
from timeit import default_timer

print('Привет, меня зовут Роджер. А как тебя?')
name = input()
name = name.title()
print('Приятно познакомиться, ' + name)

print('''Давай проверим твои знания в математике.
Ты готов? (да или нет).''')
ready = input()
ready = ready.lower()
while ready not in {'да', 'нет'}:
    print('Должно быть да или нет, введи заново')
    ready = input()
    ready = ready.lower()

if ready == 'да':

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
            print('Неправильно')
            print(f'Правильный ответ: {right_answer}')
            fails += 1    

    # определим кол-во. минут и секунд
    if time_spent < 60:
        time_spent = f'{round(time_spent)} секунд{time_endings(time_spent)}'

    else:
        minutes = round(time_spent) // 60  # Целое число минут, без остатка
        seconds = round(time_spent) - minutes * 60  # Остаток секунд
        
        if time_spent - (minutes*60) == 0:
            time_spent = f'{minutes} минут{time_endings(minutes)}'
        else:
            time_spent = f'{minutes} минут{time_endings(minutes)} и {seconds} секунд{time_endings(seconds)}'

    # если нет ошибок
    if fails == 0:
        print(f'Молодец, {name}! Ты правильно ответил на все вопросы за {time_spent} ')
    else:
        print(f'Правильных ответов: {right_answers}')
        print(f'Ошибок: {fails}')
        print(f'Затраченное время: {time_spent}')    
              

if ready == 'нет':
    print('''Передумал? Хорошо, может как-нибудь в следущий раз...
Пока!''')
