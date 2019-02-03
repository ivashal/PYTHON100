
import random

end = 'y'
chose = 0
kol_game = 0
step = 0
rounds = 15
vin = random.randint(1, 100)
# print('Подсказка: число = '+str(vin)) # Для проверки.
while chose != vin and end == 'y' and step < rounds:
    chose = int(input("Введите число: "))
    step += 1
    if chose == vin:
        print("Да! это оно!")
        end = input('Вы угадали! Хотите сыграть еще раз наберите "y" ?: ')
        vin = random.randint(1, 100)
        kol_game += 1
    elif chose < vin:
        print("Больше!")
    elif chose > vin:
        print("Меньше!")
if step >= rounds:
    print("Вы привысили количество попыток!")

print("Спасибо за игру!" + '\n' + 'Кол-во игр:' + str(kol_game) + '\n' + 'Кол-во попыток: ' + str(step))

