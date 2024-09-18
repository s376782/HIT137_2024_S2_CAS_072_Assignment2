# 3.3 Corrected Code with Comments

# Initialize a global variable to hold a value
global_variable = 100

# Dictionary with some keys and values
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process a list of numbers
def process_numbers():
    global global_variable  # Access global variable
    local_variable = 5  # Local variable initialized to 5
    numbers = [1, 2, 3, 4, 5]  # A list of numbers

    # While loop to manipulate the numbers list based on local_variable
    while local_variable > 0:
        if local_variable % 2 == 0:  # If local_variable is even
            numbers.remove(local_variable)  # Remove the number from the list
        local_variable -= 1  # Decrease the local variable by 1

    return numbers  # Return the processed list of numbers

# Set of numbers (with duplicates removed)
my_set = {1, 2, 3, 4, 5}

# Get the result after processing the numbers
result = process_numbers()

# Function to modify the dictionary
def modify_dict():
    local_variable = 10  # Local variable initialized to 10
    my_dict['key4'] = local_variable  # Add a new key-value pair to the dictionary

# Call the modify_dict function to update the dictionary
modify_dict()

# Function to update the global variable and perform checks
def update_global():
    global global_variable  # Access global variable
    global_variable += 10  # Increment global variable by 10

    # Loop through numbers from 0 to 4 and print them
    for i in range(5):
        print(i)
        i += 1  # This increment does not affect the loop, as `for` loop handles it automatically

    # Check if my_set is not None and if a condition in the dictionary is met
    if my_set is not None and my_dict['key4'] == 10:
        print("Condition met!")  # Print a message if the condition is true

    # Check if 5 is not in the dictionary keys
    if 5 not in my_dict:
        print("5 not found in the dictionary!")  # Print if 5 is not a key in the dictionary

    # Print the values of global_variable, my_dict, and my_set
    print(global_variable)
    print(my_dict)
    print(my_set)

# Call the function to update the global variable and print data
update_global()
