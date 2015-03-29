import itertools
​
​
digit, letter = ('0','1'), ('L', 'D')
​
​
def check_command(pattern, command):
    counter = 0
    pattern = convert_pattern(pattern, command)
    if len(pattern) > len(command): return False
    command = convert_command(command)
    for d in pattern:
        if d == '0':
            try:
                if 'D' == command[counter]:
                    counter += 1
                    continue
                else:
                    return False
            except IndexError:
                break
            counter += 1
        elif d == '1':
            try:
                if 'L' == command[counter]:
                    counter += 1
                    continue
                else:
                    return False
            except IndexError:
                break
            counter += 1

    return True
​

def convert_pattern(p, c):
    pattern = bin(p)[2:]
    command = convert_command(c)
    diff = len(command) - len(pattern)
    for i in range(diff):
        pattern = '0' + pattern
    return pattern

def convert_command(command):
    result = ''
    for char in command:
        if char.isdigit():
            char = 'D'
        else:
            char = 'L'
        result += char
    return result


check_command(0, u"478103487120470129")
# True
check_command(42, u"12a0b3e4")
# True
check_command(7, u"Hello")
# False
