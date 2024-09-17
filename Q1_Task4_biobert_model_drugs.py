import multiprocessing as mp
import multiprocessing.pool as p
from transformers import AutoTokenizer, pipeline

class BioBERTNerProcessor:
    def __init__(self):
        # Load the tokenizer and models
        self.__model = pipeline("ner", model="alvaroalon2/biobert_chemical_ner")

    def __split_text_into_segments(self, text, max_length=512):
        # Tokenize the text
        tokens = self.__tokenizer(text, max_length=max_length, truncation=True, return_tensors='pt')["input_ids"][0]

        # Split the tokens into chunks that are less than or equal to the max_length
        for i in range(0, len(tokens), max_length):
            yield self.__tokenizer.decode(tokens[i:i + max_length], skip_special_tokens=True)

    def __process_chunk(self, chunk):
        self.__chunk_counter += 1
        print(f"Processing chunk {self.__chunk_counter}...")

        # Ensure the segment length is within the model's max length
        ner_results = self.__model(chunk)

        # Tokenize and split the chunk into smaller sub-chunks if necessary
        entities = [(res['word'], res['entity']) for res in ner_results]
        
        # Process each tokenized chunk
        self.__drugs.update([ent[0] for ent in entities if "CHEMICAL" in ent[1]])

    # Function to process large text files in chunks
    def process(self, file_path):
        # Load the tokenizer and model        
        self.__drugs = set()

        # Initialize variables to track progress
        self.__chunk_counter = 0

        # Open and read the large text file
        with p.ThreadPool(mp.cpu_count()) as pool:
            with open(file_path, 'r', encoding='utf-8') as f:
                while True:
                    # Read a chunk from the file
                    chunk = f.read(1024*1024)
                    if not chunk:
                        break
                    # self.__process_chunk(chunk)
                    pool.apply_async(self.__process_chunk, args=(chunk,))
            pool.close()
            pool.join()

        return self.__drugs

# File path for the large .txt file

file_path = "Q1_Task1_all_text_output.txt"

# Process the file and extract drugs
processor = BioBERTNerProcessor()
drugs_biobert = processor.process(file_path)

# Print results
print(f"Extracted Drugs: {drugs_biobert}")

with open('Q1_Task4_drugs_BioBERT.txt', 'w', encoding='utf-8') as result:
    for text in drugs_biobert:
        result.write(text + '\n')


