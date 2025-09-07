import count_letters
def is_anagram(word1, word2):
    """Checks if the inputted words are anagrams of each other """
    if (count_letters.count_letters(word1) != count_letters.count_letters(word2)): return False
    else:
        letters1 = list(word1)
        letters2 = list(word2)
        while(len(letters1) != 0) and (len(letters2) != 0):
            for char in letters1:
                if char in letters2:
                    letters1.pop(letters1.index(char))
                    letters2.pop(letters2.index(char))
                else: return False
        return True
    

#is_anagram("tar", "rat")


