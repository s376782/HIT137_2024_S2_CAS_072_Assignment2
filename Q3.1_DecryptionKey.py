# Link git: https://github.com/s376782/HIT137_2024_S2_CAS_072_Assignment2/blob/main/Q3.1_DecryptionKey.py
# 3.1 Finding decryption key
# Function to calculate the decryption key
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
