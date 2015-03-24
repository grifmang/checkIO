def fibgolf(type, num):
    
	if type == "fibonacci":
        fibs = [0, 1]
        [fibs.append(fibs[-2]+fibs[-1]) for i in xrange(num)]
        return fibs[num]
    
	elif type == "tribonacci":
        tribs = [0, 0, 1]
        [tribs.append(tribs[-3]+tribs[-2]+tribs[-1]) for i in xrange(num)]
        return tribs[num+1]
    
	elif type == "lucas":
        lucas = [2, 1]
        [lucas.append(lucas[-2]+lucas[-1]) for i in xrange(num)]
        return lucas[num]
    
	elif type == "jacobsthal":
        jacob = [0, 1]
        [jacob.append((2 * jacob[-2]) + jacob[-1]) for i in xrange(num)]
        return jacob[num]
    
	elif type == "pell":
        pellList = [0, 1]
        [pellList.append(pellList[-2] + (2 * pellList[-1])) for i in xrange(num)]
        return pellList[num]
    
	elif type == "perrin":
        perr = [3, 0, 2]
        [perr.append(perr[-3]+perr[-2]) for i in xrange(num)]
        return perr[num]
    
	elif type == "padovan":
        pad = [0, 1, 1]
        [pad.append(pad[-3]+pad[-2]) for i in xrange(num)]
        return pad[num]