def process_string(s):
    # Check if the string length is at least 16 characters
    if len(s) < 16:
        raise ValueError("The string must be at least 16 characters long.")

    # Separate the string into numbers and letters, ignoring special characters
    number_string = ''.join([char for char in s if char.isdigit()])
    letter_string = ''.join([char for char in s if char.isalpha()])

    even_numbers = [char for char in number_string if int(char) % 2 == 0]
    uppercase_letters = [char for char in letter_string if char.isupper()]
    
    # Convert even numbers to ASCII code decimal values
    even_numbers_ascii = [str(ord(num)) for num in even_numbers]

    # Convert upper-case letters to ASCII code decimal values
    uppercase_ascii = [str(ord(char)) for char in uppercase_letters]

    # Print the results
    print("Original String:", s)
    print("number string:", number_string)
    print("letter string:", letter_string)
    print()
    print('Even Numbers', even_numbers)
    print("Even Numbers ASCII:", even_numbers_ascii)
    print('Upper-case Letters', uppercase_letters)
    print("Upper-case Letters ASCII:", uppercase_ascii)

# Example usage
s = '56aAww1984sktr235270aYmn145ss785fsq31D0~'
process_string(s)
