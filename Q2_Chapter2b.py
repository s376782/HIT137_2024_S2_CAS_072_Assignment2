# Link git: https://github.com/s376782/HIT137_2024_S2_CAS_072_Assignment2/blob/main/Q2_Chapter2b.py
# List of 200 common English words to check against the decrypted text
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

# Function to decrypt the cipher using a given shift value
def decrypt_cipher(ciphertext, shift):
    decrypted_text = '' # Holds the decrypted message
    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            # Convert the character to uppercase, apply the shift, and wrap around using modulo
            shifted_char = chr((ord(char.upper()) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += shifted_char
        else:
            # Non-alphabet characters (like spaces, punctuation) are added unchanged
            decrypted_text += char
    return decrypted_text

# Function to count the number of valid English words in a given decrypted text
def count_english_words(text, english_words):
    words_in_text = text.split() # Split the text into individual words
    count = 0 # Holds the number of valid words found
    for word in words_in_text:
        # Trim spaces from each word and convert it to uppercase for matching
        word = word.strip().upper()
        # Check if the word is in the list of common English words
        if word in english_words:
            count += 1
    return count

# Function to find the best shift value that results in the most valid English words
def find_best_shift(ciphertext):
    best_shift = 0 # Holds the shift value that results in the most valid words
    max_word_count = 0 # Tracks the maximum number of valid words found
    best_decryption = "" # Holds the decrypted message corresponding to the best shift

    # Try all possible shift values (1 through 25) and decrypt the message for each
    for s in range(1, 26):
        decrypted_text = decrypt_cipher(ciphertext, s) # Decrypt with the current shift
        word_count = count_english_words(decrypted_text, COMMON_ENGLISH_WORDS) # Count valid words
        
        # If this shift produces more valid words than the previous best, update the best shift
        if word_count > max_word_count:
            max_word_count = word_count
            best_shift = s
            best_decryption = decrypted_text

    return best_shift, best_decryption # Return the best shift and corresponding decrypted message

# Example ciphered text
ciphertext = ("VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS "
              "PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL "
              "JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR")

# Find the best shift and the decrypted message
best_shift, best_decryption = find_best_shift(ciphertext)

# Print the results
print(f"The best shift value is: {best_shift}")
print(f"The decrypted message is:\n{best_decryption}")
