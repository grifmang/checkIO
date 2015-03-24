def checkio(n, m):
    binN = bin(n)[2:]
    binM = bin(m)[2:]
    if len(binN) != len(binM):
        if len(binN) < len(binM):
            while len(binN) < len(binM):
                binN = '0' + binN
        elif len(binM) < len(binN):
            while len(binM) < len(binN):
                binM = '0' + binM
    hamm = 0
    counter = 0
    for num in binN:
        if num == binM[counter]:
            counter += 1
            continue
        else:
            hamm += 1
            counter += 1
    return hamm