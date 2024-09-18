import warnings
import concurrent.futures as f    # for parallel processing
import multiprocessing as mp      # for parallel processing
import multiprocessing.pool as p
from collections import Counter
from transformers import AutoTokenizer
import csv

# Ignore the warning that might arise from using older versions of libraries 
# Here we use the Python version to ver 3.10 for this assignment in order to install spispaCy library 
warnings.filterwarnings("ignore", category=FutureWarning)   

class CTokenizer:
    def __init__(self, model_name='bert-base-uncased'):    # Split text into tokens following BERT's tokenization rules.
        self.__tokenizer = AutoTokenizer.from_pretrained(model_name)    

    def __process_chunk(self, chunk):
        # Process the chunk
        self.__chunk_counter += 1
        print(f"Processing chunk {self.__chunk_counter}...")

        tokens = self.__tokenizer.tokenize(chunk)
            
        # Update the token counter
        self.__token_counts.update(tokens)

        # Update the total tokens processed
        self.__total_tokens_processed += len(tokens)
        print(f"Chunk {self.__chunk_counter} processed. Total tokens processed: {self.__total_tokens_processed}")

        return True

    def process(self, file_path):
        # Initialize a counter for token frequencies
        self.__token_counts = Counter()

        # Initialize variables to track progress
        self.__chunk_counter = 0
        self.__total_tokens_processed = 0

        with p.ThreadPool(mp.cpu_count()) as pool:    # process text chunks concurrently to speed up the processing.
            with open(file_path, 'r') as file:
                while True:
                    chunk = file.read(1024*1024)    # Read chunk with size of 1024*1024 (1MB)
                    if not chunk:
                        break
                    pool.apply_async(self.__process_chunk, args=(chunk,))

            pool.close()
            pool.join()

        # Get the top 30 most common tokens
        top_30 = self.__token_counts.most_common(30)
        return top_30

# File path for the large .txt file
file_path = "Q1_Task1_all_text_output.txt"

# Process the file and extract diseases and drugs
x = CTokenizer()
top_30 = x.process(file_path)

#Store result of top 30 common words in csv file: Q1_Task3.2_Top_30_common_words.csv
with open('Q1_Task3.2_Top_30_common_words_AutoTokenizer.csv','w',encoding='utf-8') as result:
    top30_file = csv.writer(result) #Write data into CSV file
    top30_file.writerow(['Common word', 'Count frequency']) #Write name of the header
    top30_file.writerows(top_30) #Add value of top 30 common words in rows of csv file

# Print the results
print("Top 30 tokens and their counts:")
for token, count in top_30:
    print(f"Token: {token}, Count: {count}")
