import multiprocessing as mp
import multiprocessing.pool as p
import spacy

class CTokenizer:
    def __init__(self):
        # Load the tokenizer and modelb
        self.__model = spacy.load("en_ner_bc5cdr_md")

    def __process_chunk(self, chunk):
        # Process the chunk
        self.__chunk_counter += 1
        print(f"Processing chunk {self.__chunk_counter}...")

        doc = self.__model(chunk)
        # Tokenize and split the chunk into smaller sub-chunks if necessary
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        # Process each tokenized chunk
        self.__diseases.update([ent[0] for ent in entities if ent[1] == 'DISEASE'])
        self.__drugs.update([ent[0] for ent in entities if ent[1] == 'CHEMICAL'])

    # Function to process large text files in chunks
    def process(self, file_path):
        # Load the tokenizer and model        
        self.__diseases = set()
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
                    pool.apply_async(self.__process_chunk, args=(chunk,))
            pool.close()
            pool.join()
        return self.__diseases, self.__drugs

# File path for the large .txt file
file_path = "Q1_Task1_all_text_output.txt"

# Process the file and extract diseases and drugs
x = CTokenizer()
diseases_bc5cdr, drugs_bc5cdr = x.process(file_path)

# Print results
print(f"Extracted Diseases: {diseases_bc5cdr}")
print(f"Extracted Drugs: {drugs_bc5cdr}")

#Convert all texts to .txt files
with open('Q1_Task4_diseases_bc5cdr.txt', 'w', encoding='utf-8') as result:
    for text in diseases_bc5cdr:
        result.write(text + '\n')

with open('Q1_Task4_drugs_bc5cdr.txt', 'w', encoding='utf-8') as result:
    for text in drugs_bc5cdr:
        result.write(text + '\n')