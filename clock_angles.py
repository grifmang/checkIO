from string import punctuation

def clock_angle(time):
    newTime = remove_punc(time)
    hours = int(newTime[0])
    minutes = int(newTime[1])
    return calc_angle(hours, minutes)

def remove_punc(i):
    result = []
    cleanText = ''
    for number in i:
        if number in punctuation:
            number = ' '
        cleanText += number
    result = cleanText.split()
    return result

def calc_angle(hour,minute):
    ans = abs((hour * 30 + minute * 0.5) - (minute * 6))
    return abs(min(360-ans,ans))


clock_angle("02:30")