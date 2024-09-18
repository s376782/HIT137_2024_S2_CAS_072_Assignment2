#import library to collect word
import collections
import csv

#Read the text file in the task 1
def count_common_word(input_file, output_file,n): # n is number of common words need  to count
    with open(input_file, 'r', encoding = 'utf-8') as textfile:
        alltext = textfile.read()

    #Convert to lowercase, split by whitespace to get words
    word = alltext.lower().split()

    #Count the frequency of each word
    word_count_frequency = collections.Counter(word)

    #Get the Top n most common words
    top_common_words = word_count_frequency.most_common(n)

    #Store result of top 30 common words in csv file: Q1_Task3.1_Top_30_common_words.csv
    with open(output_file,'w', newline= '', encoding='utf-8') as result:
        result = csv.writer(result) #Write data into CSV file
        result.writerow(['Common words', 'Count frequency']) #Write name of the header
        result.writerows(top_common_words) #Add value of top n common words in rows of csv file

    #Print message after saving result successfully
    print('Result has been saved successfully')
    
input_file = 'data/Q1_Task1_all_text_output.txt'
output_file = 'data/Q1_Task3.1_Top_30_common_words.csv'
n = 30
count_common_word(input_file, output_file,n)
