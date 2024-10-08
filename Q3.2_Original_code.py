
# Link git: https://github.com/s376782/HIT137_2024_S2_CAS_072_Assignment2/blob/main/Q3.2_Original_code.py
# 3.2 it reveals the original code with many errors.
# QUESTION 3: 
# it reveals the original code with many errors.

# Function to find decryption key
def key():
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2
    return total

print(f"The decryption key is: {key()}")

# Decryption function to decrypt the ‘encrypted code’ to the original code
def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key # Decrypting by shifting back
            if char.islower():
                if shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted < ord("A"):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Encrypted code provided 
encrypted_code = """
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl14'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

    sbe v va enatr(5):
        cevag(v)
        v += 1

    vs zl_frg vf abg Abar naq zl_qvpg['xrl14'] == 10:
        cevag("Pbaqvgvba zrg!")

    vs 5 abg va zl_qvpg:
        cevag("5 abg sbhaq va gur qvpgvbanel!")

    cevag(tybony_inevnoyr)
    cevag(zl_qvpg)
    cevag(zl_frg)
"""
# Use the key to decrypt the entire block of code
key_used_for_decryption = 13
decrypted_code = decrypt(encrypted_code, key_used_for_decryption)

# Print the decrypted code
print("Decrypted code is:")
print(decrypted_code)
