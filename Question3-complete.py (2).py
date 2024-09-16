# QUESTION 3:
# 1. find decryption key
# 2. Decrypt the given code using a key.
# 3. Fix the errors in the decrypted code and add comments.
# 4. Display everything in your program.

# Step 1: Function to calculate the decryption key
def key():
    total = 0
    # Nested loop to calculate the total based on the values of i and j
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    # Adjust the total value to reach 13
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

# Step 2: Function to decrypt the encrypted code
def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Shift the character backward by the key value
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord("a"):
                    shifted += 26
            elif char.isupper():
                if shifted < ord("A"):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            # Keep non-alphabet characters the same
            decrypted_text += char
    return decrypted_text

# The encrypted code
encrypted_code = """
tybony inevnoyr
100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xr13': 'inyhr3'}
qrs cebprff_ahzoref():
tybony tybony_inevnoyr ybpny_inevnoyr = 5
ahzoref= [1, 2, 3, 4, 5]
juvyr ybpny_inevnoyr > >:
vs ybpny inevnoyr % 2 == 0: ahzoref.erzbir(ybpny_inevnoyr)
ybpny inevnoyr -= 1
erghea ahzoref
zl_frg (1, 2, 3, 4, 5, 5, 4, 3, 2, 1} erfhyg- cebprff_ahzoref(ahzoref-z1_frg)
qrs zbqvsl_qvpg():
ybpny inevnoyr
10
zl_qvpg['xr14'] = ybpny_inevnoyr
zbqvs1_qvpg(5)
qrs hcqngr_tybony():
tybony tybony_inevnoyr
tybony_inevnoyr += 10
sbe v va enatr(5):
cevag(v)
v +- 1
vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10: cevag("Pbaqvgvba zrg!")
vs 5 abg va z1_qvpg:
cevag("5 abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# Step 3: Use the key to decrypt the encrypted code
key_used_for_decryption = 13
decrypted_code = decrypt(encrypted_code, key_used_for_decryption)

# Print the decrypted code
print("The decrypted code is:")
print(decrypted_code)

# Step 4: The corrected code after decryption and fixing errors

# Initialize global variable
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process a list of numbers
def process_numbers():
    global_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while global_variable > 0:
        if global_variable % 2 == 0:
            numbers.remove(global_variable)
        global_variable -= 1
    return numbers

# Function to modify the dictionary
def modify_dict():
    global_variable = 10
    my_dict['key4'] = global_variable
    modify_dict(5)

# Function to update the global variable
def update_global():
    global global_variable
    global_variable += 10
    for i in range(5):
        print(i)
        i += 1
    if my_list is not None and my_dict['key4'] == 10:
        print("Condition met!")
    if 5 not in my_dict:
        print("5 not found in the dictionary!")
    print(global_variable)
    print(my_dict)
    print(my_list)
