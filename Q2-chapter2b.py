COMMON_ENGLISH_WORDS = [
    "THE", "BE", "AND", "OF", "A", "IN", "TO", "HAVE", "IT", "I", "THAT", "FOR", "YOU", "HE", "WITH",
    "ON", "DO", "SAY", "THIS", "THEY", "AT", "BUT", "WE", "HIS", "FROM", "NOT", "BY", "SHE", "OR",
    "AS", "WHAT", "GO", "THEIR", "CAN", "WHO", "GET", "IF", "WOULD", "HER", "ALL", "MY", "MAKE",
    "ABOUT", "KNOW", "WILL", "AS", "UP", "ONE", "TIME", "THERE", "YEAR", "SO", "THINK", "WHEN",
    "WHICH", "THEM", "SOME", "ME", "PEOPLE", "TAKE", "OUT", "INTO", "JUST", "SEE", "HIM", "YOUR",
    "COME", "COULD", "NOW", "THAN", "LIKE", "OTHER", "HOW", "THEN", "ITS", "OUR", "TWO", "MORE",
    "THESE", "WANT", "WAY", "LOOK", "FIRST", "ALSO", "NEW", "BECAUSE", "DAY", "MORE", "USE", "NO",
    "MAN", "FIND", "HERE", "THING", "GIVE", "MANY", "WELL", "ONLY", "THOSE", "TELL", "VERY", "EVEN",
    "BACK", "ANY", "GOOD", "WOMAN", "THROUGH", "US", "LIFE", "CHILD", "THERE", "WORK", "DOWN",
    "MAY", "AFTER", "SHOULD", "CALL", "WORLD", "OVER", "SCHOOL", "STILL", "TRY", "LAST", "ASK",
    "NEED", "TOO", "FEEL", "THREE", "WHEN", "STATE", "NEVER", "BECOME", "BETWEEN", "HIGH", "REALLY",
    "SOMETHING", "MOST", "ANOTHER", "MUCH", "FAMILY", "OWN", "OUT", "LEAVE", "PUT", "OLD", "WHILE",
    "MEAN", "ON", "KEEP", "STUDENT", "WHY", "LET", "GREAT", "SAME", "BIG", "GROUP", "BEGIN", "SEEM",
    "COUNTRY", "HELP", "TALK", "WHERE", "TURN", "PROBLEM", "EVERY", "START", "HAND", "MIGHT", "AMERICAN",
    "SHOW", "PART", "AGAINST", "PLACE", "SUCH", "AGAIN", "FEW", "CASE", "MOST", "WEEK", "COMPANY",
    "WHERE", "SYSTEM", "EACH", "RIGHT", "PROGRAM", "HEAR", "QUESTION", "DURING", "WORK", "PLAY", "GOVERNMENT",
    "RUN", "SMALL", "NUMBER", "OFF", "ALWAYS", "MOVE", "LIKE", "NIGHT", "LIVE", "MR", "POINT", "BELIEVE",
    "HOLD", "TODAY", "BRING", "HAPPEN", "NEXT", "WITHOUT", "BEFORE", "LARGE", "ALL", "MILLION", "MUST",
    "HOME", "UNDER", "WATER", "ROOM", "WRITE", "MOTHER", "AREA", "NATIONAL", "MONEY", "STORY", "YOUNG"
]

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            shifted_char = chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char  # Non-alphabet characters remain the same
    return decrypted_text

def count_english_words(text, english_words):
    words_in_text = text.split()
    count = 0
    for word in words_in_text:
        word = word.strip().upper()
        if word in english_words:
            count += 1
    return count

def find_best_shift(ciphertext):
    best_shift = 0
    max_word_count = 0
    best_decryption = ""

    for s in range(1, 26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, s)
        word_count = count_english_words(decrypted_text, COMMON_ENGLISH_WORDS)
        
        if word_count > max_word_count:
            max_word_count = word_count
            best_shift = s
            best_decryption = decrypted_text

    return best_shift, best_decryption

ciphertext = ("VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS "
              "PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL "
              "JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR")

best_shift, best_decryption = find_best_shift(ciphertext)
print(best_shift)
print(best_decryption)