def verify_anagrams(first_word, second_word):
    first_word = first_word.replace(" ", "")
    second_word = second_word.lower()
    second_word = second_word.replace(" ","")
    
	if len(first_word) != len(second_word):
            return False
    
	for char in first_word.lower():
        
		if char in second_word:
            spot = second_word.index(char)
            second_word = second_word[:spot] + second_word[spot+1:]
        
		else:
            return False
    
	if len(second_word) == 0:
        return True