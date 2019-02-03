imya = str(input("Введите имя и фамилию без пробелов: "))

def zad_61(imya):
    return ({i: i + 2 for i in range(((len(imya) % 5) + 2) * 2)})

def zad_62(imya):
    list_my = {i: i + 2 for i in range(((len(imya) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return list_my

def zad_63(imya):
    list_my = {i: i + 2 for i in range(((len(imya) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return {i: list_my[i] for i in range(1, len(list_my) - 1)}

def zad_64(imya):
    list_my = {i: i + 2 for i in range(((len(imya) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return {i: list_my[i] for i in range(1, len(list_my), 3)}

def zad_65(imya, n=1):
    list_my = {i: i + 2 for i in range(((len(imya) % 5) + 2) * 2)}
    list_my.update({i + len(list_my): list_my[i] + 1 for i in range(len(list_my))})
    return {i: list_my[i] for i in range((n - 1) * round(len(list_my) / 3), round(n * len(list_my) / 3))}

if __name__ == "__main__":
    print(zad_61(imya))
    print(zad_62(imya))
    print(zad_63(imya))
    print(zad_64(imya))
    n = int(input("Введите часть списка которую хотите отобразить(1,2 или 3): "))
    print(zad_65(imya, n))