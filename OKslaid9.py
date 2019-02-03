def zadanie91(n):
    if n == 1 or n == 2:
        return 1
    else:
       return zadanie91(n-1) + zadanie91(n-2)

def zadanie92(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
       return zadanie91(n-1) + zadanie91(n-2) + zadanie91(n-3)

def zadanie93(n):
    return [n**2 for n in range(1, n+1, 2)]

def zadanie94(shirina,visota, simvol='*'):
    for i in range(visota + 1):
        if i == 0 or i == visota:
            print(simvol*shirina)
        else:
            print(simvol + ' '*(shirina - 2) + simvol)

        # s = '*'
        # for i in range(vis + 1):
        #     if i == 0 or i == vis:
        #         print(s * shir)
        #     else:
        #         print(s + ' ' * (shir - 2) + s)

def zadanie95(start_nat_num=10, end_nat_num=15):
    # "Функция вычисляет сумму и произведение всех натуральных чисел от А до В включительно"
    summNum = 0
    prz = 1
    for i in range (start_nat_num, end_nat_num + 1):
        summNum += i
        prz *= i
    return summNum, prz

def zadanie96(start_nat_num=10, end_nat_num=15):
    chet = []
    nechet = []

    chet = [i for i in range(start_nat_num + 1, end_nat_num) if i % 2 == 0]
    nechet = [i for i in range(start_nat_num + 1, end_nat_num) if i % 2 != 0]
    return ("Четные числа: " + str(chet)), ("Нечетные числа: " + str(nechet))


def zadanie97(*args, boolian=True):
    mylist = args
    poloj = []
    otriz = []
    poloj = [i for i in mylist if i >= 0]
    otriz = [i for i in mylist if i < 0]
    if boolian == True:
        return poloj
    else:
        return otriz


if __name__ == "__main__":
    print(zadanie91(n=9))
    print(zadanie92(n=9))
    print(zadanie93(n=6))
    print(zadanie94(shirina=10, visota=10))
    print(zadanie95(start_nat_num=10, end_nat_num=15))
    print(zadanie96(start_nat_num=10, end_nat_num=15))
    print(zadanie97(1, 3, 4, -3, -2, 3, -7, 7, -12, boolian=True))
    print(zadanie97(1, 3, 4, -3, -2, 3, -7, 7, -12, boolian=False))