VOWELS = "aeiouy"

def translate(phrase):
    result = []
    if len(phrase.split()) > 1:
        for word in phrase.split():
            result.append(get_words(word))
        return ' '.join(result)
    else:
        return get_words(phrase)

def get_words(words):
    string_result = ''
    words = list(words)
    for letter in words:
        string_result += letter
        if letter in VOWELS:
            del words[0:2]
        else:
            del words[0:1]
    return string_result

translate(u"hoooowe yyyooouuu duoooiiine")