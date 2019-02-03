
def zadanie71(text="abc", numb=5):
    return text * numb + "!"

def zadanie72(chislo=10):
    for i in range(0, chislo+1):
        print(((chislo-1)-i) * '=' + ((i+1) * ' '))

def zadanie73(word):
    return {i: word.count(i, 0, len(word)) for i in word}

def zadanie74(text1):
    d = {}
    for word in text1.split():
        key = "слов длинной " + str(len(word))
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d



if __name__ == '__main__':
    print(zadanie71(text="abc", numb=5))
    print(zadanie72(chislo=10))
    print(zadanie73(word="solomon"))
    print(zadanie74(text1="aefawefef oijoi oijpoij poi09i ;lkj iugh oi"))