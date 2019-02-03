
def zadanie11_1(kol_vo_mon_x, kol_vo_nom_y, nominal_x, nominal_y, summ_pay_z, chance_pay=False):
    for i in range(kol_vo_mon_x + 1):
        for j in range(kol_vo_nom_y + 1):
            if i*nominal_x+j*nominal_y == summ_pay_z:
                chance_pay = True
                return True and print("Можно оплатить: " + "Монет номиналом-" + str(nominal_x) + " " + str(i) + "шт" + " и" + " монет номиналом-" + str(nominal_y) + " " + str(j) + " " + "шт")
    if chance_pay == False:
        return False and print("Невозможно оплатить")

def zadanie11_2(cel_chis1):
    cel_chis1 = abs(cel_chis1)
    count = 1
    cel_chis1 //= 10
    while cel_chis1 > 0:
        cel_chis1 //= 10
        count += 1
    return count

def zadanie11_3(word):
    return word == word[::-1]

def zadanie11_4(stroka,old, new):
    return stroka.replace(old, new,)

if __name__ == "__main__":
    print(zadanie11_1(kol_vo_mon_x=4, kol_vo_nom_y=6, nominal_x=2, nominal_y=5, summ_pay_z=13, chance_pay=False))
    print(zadanie11_2(cel_chis1=323232))
    print(zadanie11_3(word="mom"))
    print(zadanie11_3(word="moma"))
    print(zadanie11_4(stroka="barbarian", old="bar", new="mur"))