#import pandas library
import pandas as pd

#Initiate empty list to store text data
def extract_text_from_csv(dataset, output_file):
    alltext = []

    #Collect all text by a loop through each dataset
    for file in dataset:
        #Read each CSV file
        df = pd.read_csv(file)
    
        #Extract the columns contain name "TEXT" in the column name
        text_columns = df.filter(like = 'TEXT', axis = 1)
    
        #Convert the extracted columns from series to strings, then to python list
        for col in text_columns:
            alltext.extend(text_columns[col].dropna().astype(str).tolist())

    #Convert all texts to a single .txt file
    with open(output_file, 'w', encoding='utf-8') as result:
        for text in alltext:
            result.write(text + '\n')
    
    #Print message after converting successfully 
    print('All texts of 4 CSV files is successfully extracted to Q1_Task1_all_text_output.txt')

dataset = ['data/CSV1.csv', 'data/CSV2.csv', 'data/CSV3.csv', 'data/CSV4.csv']
output_file = 'data/Q1_Task1_all_text_output.txt'
extract_text_from_csv(dataset, output_file)    
    