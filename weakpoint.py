def weak_point(matrix):
    
    if len(matrix) == 1:
        return [0,0]
    
    rows = []
    
    for row in matrix:
        count = 0
    
        for element in row:
            count += element
            
        rows.append(count)
    
    sumList = []
    counter = 1
    a = 0
    summed = 0
    sumTotals = []
    
    while counter <= len(matrix):
        
        for line in matrix:
            sumList.append(line[a])
            
        for num in sumList:
            summed += num
            
        sumTotals.append(summed)
        summed = 0
        sumList = []
        a += 1
        counter += 1
    
    minRow = min(rows)
    minCol = min(sumTotals)
    
    if minRow in rows:
        rowIndex = rows.index(minRow)
    
    if minCol in sumTotals:
        colIndex = sumTotals.index(minCol)
    
    return [rowIndex,colIndex]
	
weak_point([[7, 2, 7, 2, 8],
             [2, 9, 4, 1, 7],
             [3, 8, 6, 2, 4],
             [2, 5, 2, 9, 1],
             [6, 6, 5, 4, 5]])