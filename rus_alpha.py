rus_lower = ''.join([chr(i) for i in range(ord('а'),ord('а')+6)] + [chr(ord('а')+33)] + [chr(i) for i in range(ord('а')+6,ord('а')+32)])
rus_upper = rus_lower.upper()
def rus_word_check(word):
    for letter in word:
        if letter not in rus_lower and letter not in rus_upper:
            return False
    return True