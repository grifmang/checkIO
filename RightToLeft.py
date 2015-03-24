def left_join(phrases):
    result = []
    
	for element in phrases:
        
		if 'right' in element:
            change = element.replace('right', 'left')
            result.append(change)
        
		else:
            result.append(element)
    
	result = ','.join(result)
    
	return result
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"