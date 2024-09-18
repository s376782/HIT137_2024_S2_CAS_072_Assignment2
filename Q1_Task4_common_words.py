# Link git: https://github.com/s376782/HIT137_2024_S2_CAS_072_Assignment2/blob/main/Q1_Task4_common_words.py
import collections
import pandas as pd

# List of file paths
file_paths = [
    'Q1_Task4_diseases_BioBERT.txt',
    'Q1_Task4_diseases_bc5cdr.txt',
    'Q1_Task4_drugs_BioBERT.txt',
    'Q1_Task4_drugs_bc5cdr.txt'
]

# Output file names
output_files = [
    'Q1_Task4_diseases_BioBERT_Top_30_common_words.xlsx',
    'Q1_Task4_diseases_bc5cdr_Top_30_common_words.xlsx',
    'Q1_Task4_drugs_BioBERT_Top_30_common_words.xlsx',
    'Q1_Task4_drugs_bc5cdr_Top_30_common_words.xlsx'
]

def get_top_30_common_words(file_path):
    # Read the text file
    with open(file_path, 'r', encoding='utf-8') as textfile:
        alltext = textfile.read()
    
    # Convert to lowercase, split by whitespace to get words
    word = alltext.lower().split()
    
    # Count the frequency of each word
    word_count_frequency = collections.Counter(word)
    
    # Get the Top 30 most common words
    top_30_common_words = word_count_frequency.most_common(30)
    
    return top_30_common_words

def save_to_excel(top_30_common_words, output_file):
    # Convert to DataFrame
    df = pd.DataFrame(top_30_common_words, columns=['Common word', 'Count frequency'])
    
    # Save to Excel
    df.to_excel(output_file, index=False)

for file_path, output_file in zip(file_paths, output_files):
    top_30_common_words = get_top_30_common_words(file_path)
    save_to_excel(top_30_common_words, output_file)
    print(f'Top 30 common words for {file_path} saved to {output_file}')
