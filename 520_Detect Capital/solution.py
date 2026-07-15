#USA
#leetcode
#Google
word = "ALphA"

def detectCapitalUse(word):
    word1 = word.upper()
    word2 = word.lower()
    word3 = word.capitalize()

    if (word == word1 or word == word2 or word == word3):
        return True
    else :
        return False
    
print(detectCapitalUse(word))
