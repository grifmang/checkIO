def checkio(first, second):
    result = []
    
    if len(first) > len(second):
        
        for word in first.split(','):
            
            if word in second.split(','):
                result.append(word)
        
        return ','.join(sorted(result))
    
    elif len(second) > len(first):
        
        for word in second.split(','):
            
            if word in first.split(','):
                result.append(word)
        
        return ','.join(sorted(result))
    
    else:
        
        for word in first.split(','):
            
            if word in second.split(','):
                result.append(word)
        
        return ','.join(sorted(result))