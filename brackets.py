def checkio(expression):
    brackets = ['()', '{}', '[]']
    bracketOpen = {x for x, _ in brackets}
    bracketClose = {y: x for x, y in brackets}
    result = []
    
    for char in expression:
        
        if char in bracketOpen:
            result.append(char)
        
        elif char in bracketClose:
        
            if not result or result[-1] != bracketClose[char]:
                return False
            
            result.pop()

    return not result