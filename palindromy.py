#palindrom np. kajak, kobyła ma mały bok
def palindrom(word):
    n = len(word)
    #zmienna zachwująca długość słowa
    for i in range(n - 1):
        #n -1 ponieważ działamy na indeksach
        if word[i] != word[n - 1 - i]:
            return False
    return True
    

print(palindrom("Kajak"))