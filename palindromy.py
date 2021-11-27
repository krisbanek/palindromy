#palindrome for example: kajak, kobyła ma mały bok

#Enter your word/sentence below, please:
word = "Kobyła ma mały bok"
def palindrom(word):
    word = word.lower()          #Capital letters doen't matter any more.
    word = word.replace(" ", "") # removing the spaces so sentences ca be checked.
    n = len(word)                #calculating lenght of given word.
    for i in range(n - 1):       #n -1 due to switching to index domain.
        if word[i] != word[n - 1 - i]:
            return False
    return True
print(f"Is {word} a palindrome?")
result = palindrom(word)
print(result)