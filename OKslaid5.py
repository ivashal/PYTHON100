def zadanie51(x=5, y=2.3, z=2, f=7.8):
    return (((x*(y-x))/z)+x+((f+z)/(f**y))-((z-f)/z))/(((z+f)/(z**y))-f)


if __name__ == "__main__":
    x = int(input('Введите x : '))
    y = int(input('Введите y : '))
    z = int(input('Введите z : '))
    f = int(input('Введите f : '))
    print(zadanie51(x, y, z, f))
