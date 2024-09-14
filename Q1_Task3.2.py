from transformers import AutoTokenizer
from collections import Counter       # Count the time appear for the token
import csv

def count_unique_tokens(file_path, model_name='bert-base-uncased', top_n=30):
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Initialize a counter for tokens
    token_counter = Counter()     # A Counter object to track how many times each token (word or symbol) appears
    
    # Read the file in chunks to handle large files
    with open(file_path, 'r', encoding='utf-8') as file:       # Read file with UTF-8 encoding
        while True:
            chunk = file.read(1024 * 1024)  # Read the file in chunks (here is 1MB at a time)
            if not chunk:      
                break              # If there's no more text to read (end of the file), the loop breaks

            # Tokenize the read chunk 
            tokens = tokenizer.tokenize(chunk)   # Use tokenize in AutoTokenizer to change the chunk into tokens (words and sub-words, (special) characters).                           

            # Split tokens into smaller chunks to avoid exceeding the max sequence length, maximum length for BERT is 512 tokens
            max_length = 512
            for i in range(0, len(tokens), max_length):      # i runs from 0 to len(tokens) with the step of 512
                token_chunk = tokens[i : i+max_length]
                token_counter.update(token_chunk)
    
    # Get the top N most common tokens
    top_tokens = token_counter.most_common(top_n)    
    return top_tokens

# Example usage
file_path = 'Q1_Task1_all_text.txt'
top_tokens = count_unique_tokens(file_path)
print(top_tokens)

if top_tokens:
    with open('Q1_Task3.2_Top_30_common_words.csv','w',encoding='utf-8') as result:
        top30_file = csv.writer(result) #Write data into CSV file
        top30_file.writerow(['Common word', 'Count frequency']) #Write name of the header
        top30_file.writerows(top_tokens) #Add value of top 30 common words in rows of csv file
