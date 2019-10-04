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
    question_quantity = ''
    if not question_quantity.isdigit():
        print('Сколько примеров ты готов решить?')
        question_quantity = input()
        while not question_quantity.isdigit():
            print('Должна быть цифра')
            question_quantity = input()
            if question_quantity.isdigit():
                while int(question_quantity) < 1:
                    print('Введи число больше 0')
                    question_quantity = input()

if ready == 'нет':
    print('''Передумал? Хорошо, может как-нибудь в следущий раз...
Пока!''')
