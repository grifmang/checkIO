def letter_queue(commands):
    result = ''
    
    for element in commands:
        
        if element.split()[0] == 'PUSH':
            result += element.split()[1]
        
        elif element == 'POP':
            
            if not result: continue
            result = result[1:]
    
    return ''.join(result)