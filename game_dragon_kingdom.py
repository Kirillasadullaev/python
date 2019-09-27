from random import randint
from time import sleep

# отображаем вступление
def displayIntro ():
    print('''
Вы находитесь в землях, заселённых драконами.
Перед собой вы видите 2 пещеры.
В одной из них - дружелюбный дракон,
который готов поделиться с вами своими сокровищами.
Во второй - жадный и голодный дракон, который мигом вам съест.
''')
    sleep(2)

def displayIntro2():
    print('Вы приближаетесь к пещере...')
    sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    sleep(2)


def chooseCave ():
    print('В какую пещеру вы войдёте? (нажмите клавишу 1 или 2)')
    cave = int(input())
    return cave

def checkCave (my_cave):
    friendly_cave = randint(1, 2)
    if friendly_cave == my_cave:
        displayIntro2()
        print('делиться с вами своими сокровищами!')
    else:
        displayIntro2()
        print('моментально вас съедает!')

displayIntro()
play_again = 'да'

while play_again == 'да':
    checkCave(chooseCave())
    print('Попытаете удачу ещё раз? (да или нет)')
    play_again = input()