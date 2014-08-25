fb = 'Fizz Buzz'
f = 'Fizz'
b = 'Buzz'

def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return fb
    elif number % 3 == 0:
        return f
    elif number % 5 == 0:
        return b
    else:
        return str(number)

