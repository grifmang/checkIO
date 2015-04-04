def checkio(words):
    count = 0
    words = words.split()
    print "String before check: ", words
    print "###############################"
    for o in words:
        if len(o) >= 3:
            count += 1
        if o.isdigit() == True:
            count = 0
        if count >= 3:
            print "True"
            return True
        else:
            print "False"
            return False

checkio('start 5 one two three 7 end')
