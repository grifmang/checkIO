def digit_stack(commands):
    stack = []
    result = []
    newCMD = []
    answer = 0
    
	for entry in commands:
        newCMD.append(entry.split())
    
	for element in newCMD:
        
		if element[0] == 'PUSH':
            stack.append(element[1])
        
		elif element[0] == 'PEEK':
            
			if len(stack) == 0:
                continue
            
			else:
                spot = len(stack)
                newChar = stack[spot-1]
                result.append(newChar)
        
		elif element[0] == 'POP':
            
			if len(stack) == 0:
                continue
            
			else:
                spot = len(stack)
                newChar = stack[spot-1]
                result.append(newChar)
                stack.pop()
    
	for digit in result:
        answer = int(answer) + int(digit)
    
	return answer