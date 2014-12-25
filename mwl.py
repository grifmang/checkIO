import string

def MostWantedLetter(text):
    text = text.lower()
    text = sorted(text)
    result = {}
    resultLowest = []
    higher = 0
    alphaIndex = 0
    lowIndex = 27
    for letter in text:
        if letter not in string.ascii_lowercase:
            continue
        if letter in result.keys():
            result[letter] = result.get(letter, 0) + 1
        elif letter not in result.keys():
            result[letter] = 1
    for key, value in result.items():
        if value > higher:
            higher = value
            highest = key
    for key, value in result.items():
        if value == higher:
            resultLowest.append(key)
        else:
            continue
    if len(resultLowest) > 1:
        for item in resultLowest:
            alphaIndex = string.ascii_lowercase.index(item)
            if alphaIndex < lowIndex:
                lowIndex = alphaIndex
        return string.ascii_lowercase[lowIndex]
    else:
        return highest