def checkio(data):
    result = []
    length = len(data)
    if length < 10:
        return False
    elif length < 1:
        return False
    elif length > 64:
        return False
    elif data == data.upper():
        return False
    elif data == data.lower():
        return False
    else:
        count = 0
        for num in data:
            if num.isdigit() == True:
                count += 1
        if count > 0:
            return True
        else:
            return False
    return True