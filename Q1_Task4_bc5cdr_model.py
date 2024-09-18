import multiprocessing as mp
import multiprocessing.pool as p
import spacy

class Bc5cdrNerProcessor:
    def __init__(self):
        # Load the tokenizer and modelb
        self.__model = spacy.load("en_ner_bc5cdr_md")

    def __process_chunk(self, chunk, chunk_counter, processed_entities):
        # Process the chunk
        print(f"Processing chunk {chunk_counter}...")

        ner_results = self.__model(chunk)
        for res in ner_results.ents:
            prossed_entity = processed_entities.get(res.label_)
            if prossed_entity is None:
                prossed_entity = processed_entities[res.label_] = set()
            prossed_entity.add(res.text)

    # Function to process large text files in chunks
    def process(self, file_path):
        processed_entities = {}

        # Initialize variables to track progress
        chunk_counter = 0

        # Open and read the large text file
        with p.ThreadPool(mp.cpu_count()) as pool:
            with open(file_path, 'r', encoding='utf-8') as f:
                while True:
                    # Read a chunk from the file
                    chunk = f.read(1024*1024)
                    if not chunk:
                        break

                    chunk_counter += 1
                    pool.apply_async(self.__process_chunk, args=(chunk, chunk_counter, processed_entities))

            pool.close()
            pool.join()

        return processed_entities 

# File path for the large .txt file
file_path = "Q1_Task1_all_text_output.txt"

diseases_bc5cdr = set()
drugs_bc5cdr = set()

# Process the file and extract diseases
processor = Bc5cdrNerProcessor()
entities = processor.process(file_path)
for key, value in entities.items():
    if "DISEASE" in key:
        diseases_bc5cdr.update(value)
    elif "CHEMICAL" in key:
        drugs_bc5cdr.update(value)

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