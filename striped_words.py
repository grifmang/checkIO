from itertools import cycle

VOWELS = "AEIOUY".lower()
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ".lower()

def checkio(text):
    newText = ''
    result = []
    counter = 0
    for word in text:
        for char in word:
            if char.isdigit():
                pass
            elif char.lower() not in VOWELS and char.lower() not in CONSONANTS:
                char = ' '
            char = char.lower()
            newText += char

    result = newText.split()

    for word in result:
        if len(word) == 1:
            continue
        if any(char.isdigit() for char in word):
            continue
        elif check_striped(word):
            counter += 1

    return counter


def check_striped(word):
    first=word[0] in VOWELS
    condition_cycle=cycle([first,not first])
    if all([((letter in VOWELS) == condition_cycle.next()) for letter in word]):
        return True
    else:
        return False



checkio(u"Dog,cat,mouse,bird.Human.")