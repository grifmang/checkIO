a = ["A", "B", "C"]
b = ["A","C"]
c = ["C","D","E"]

for aval,bval,cval in itertools.product(a,b,c):
    if aval == bval and bval == cval:
        print aval
