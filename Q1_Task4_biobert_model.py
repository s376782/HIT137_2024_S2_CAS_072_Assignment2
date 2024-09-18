import multiprocessing as mp
import multiprocessing.pool as p
from transformers import pipeline

class BioBERTNerProcessor:
    def __init__(self, model_name):
        # Load the tokenizer and models
        self.__model = pipeline("ner", model=model_name)

    def __process_chunk(self, chunk, chunk_counter, processed_entities):
        # Process the chunk
        print(f"Processing chunk {chunk_counter}...")

        ner_results = self.__model(chunk)
        for res in ner_results:
            processed_entity = processed_entities.get(res['entity'])
            if processed_entity is None:
                processed_entity = processed_entities[res['entity']] = set()
            processed_entity.add(res['word'])

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

diseases_biobert = set()
drugs_biobert = set()

models = ['dmis-lab/biobert-v1.1', 'alvaroalon2/biobert_diseases_ner', 'alvaroalon2/biobert_chemical_ner']
for model in models:
    # Process the file and extract diseases
    processor = BioBERTNerProcessor(model)
    entities = processor.process(file_path)
    for key, value in entities.items():
        if "DISEASE" in key:
            diseases_biobert.update(value)
        elif "CHEMICAL" in key:
            drugs_biobert.update(value)

# Print results
print(f"Extracted Diseases: {diseases_biobert}")
print(f"Extracted Drugs: {drugs_biobert}")

# Convert all texts to .txt files
with open('Q1_Task4_diseases_BioBERT.txt', 'w', encoding='utf-8') as result:
    for text in diseases_biobert:
        result.write(text + '\n')

with open('Q1_Task4_drugs_BioBERT.txt', 'w', encoding='utf-8') as result:
    for text in drugs_biobert:
        result.write(text + '\n')