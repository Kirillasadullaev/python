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
    question_quantity = ''  # количество вопросов
    max_answer = ''  # до скольки будем считать

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
        print('Пример ' + str(question+1) + ':')    

if ready == 'нет':
    print('''Передумал? Хорошо, может как-нибудь в следущий раз...
Пока!''')
