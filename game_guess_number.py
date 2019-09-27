# игра "Угадай число"
from random import randint

print('Как Вас зовут?')
name = input()
print('Здравствуйте, ' + name)
print("Я загадываю число от 1 до 20")

number = randint(1,20)

for i in range(6):
    print("Попробуй угадать его:")
    guess_number = int(input())
    if guess_number < number:
        print("Число слишком маленькое")
    if guess_number > number:
        print("Число слишком большое")
    if guess_number == number:
        break

if guess_number == number:
    print("Ты угадал за " + str(i+1) + " попыток")
else:
    print("Ты проиграл, я загадывала число " + str(number))