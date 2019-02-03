imya = str(input("Введите имя и фамилию без пробелов: "))

def zad_61(imya):
    return [i + 1 for i in range(((len(imya) % 5) + 2) * 2)]

def zad_62(imya):
    list_my = [i + 1 for i in range(((len(imya) % 5) + 2) * 2)]
    return list_my + [i + 1 for i in list_my]

def zad_63(imya):
    list_my = [i + 1 for i in range(((len(imya) % 5) + 2) * 2)]
    list2 = list_my + [i + 1 for i in list_my]
    return list2[1:-1]

def zad_64(imya):
    list_my = [i + 1 for i in range(((len(imya) % 5) + 2) * 2)]
    list2 = list_my + [i + 1 for i in list_my]
    return [list2[i] for i in range(1, len(list2), 3)]

def zad_65(imya, n=1):
    list_my = [i + 1 for i in range(((len(imya) % 5) + 2) * 2)]
    list2 = list_my + [i + 1 for i in list_my]
    return [list2[i] for i in range((n - 1) * round(len(list2) / 3), round(n * len(list2) / 3))]


if __name__ == "__main__":
    print(zad_61(imya))
    print(zad_62(imya))
    print(zad_63(imya))
    print(zad_64(imya))
    n = int(input("Введите часть списка которую хотите отобразить(1,2 или 3): "))
    print(zad_65(imya, n))


