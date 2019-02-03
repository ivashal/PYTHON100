def zadanie81(a_max=1000):
    run_run = 0
    day = 0
    while run_run < a_max:
        day += 1
        run_run += 2**day
    return day

def zadanie82(allrun=1000):
    days = 0
    run = 0
    f = list(range(100))
    f[1] = 0
    step = 2
    while run <= allrun:
        if f[step] != 0:
            run += f[step]
            days += 1
            for j in range(step, 100, step):
                f[j] = 0
        step += 1
    return days


def zadanie83(run=10, upprocent=0.15, sumdays=30):
    #upprocent = 0.15
    #run = 10
    runsumm = 10
    #sumdays = 30
    days = 1
    while days < sumdays:
        if days % 2 != 0:
            run += run * upprocent
        days += 1
        runsumm += run
    return round(runsumm) # Получаем округленный результат.


def zadanie84_1(all_put=100):
    run = 10
    run_summ = 10
    days = 1
    upday = 0.1
    while run_summ < all_put:
        run += run * upday
        run_summ += run
        days += 1

    return days, round(run_summ)

def zadanie84_2(bolshe_km=20):
    run = 10
    days = 1
    up_day = 0.1
    while run < bolshe_km:
        run += run * up_day
        days += 1
    return days, round(run)

if __name__ == "__main__":
    print(zadanie81(a_max=1000))
    print(zadanie82(allrun=1000))
    print(zadanie83(run=10, upprocent=0.15, sumdays=30))
    print(zadanie84_1(all_put=100))
    print(zadanie84_2(bolshe_km=20))