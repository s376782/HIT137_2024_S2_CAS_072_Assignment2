#import library to collect word
import collections
import csv
import pandas as pd

#Read the text file in the task 1
with open('Q1_Task1_all_text_output.txt', 'r', encoding = 'utf-8') as textfile:
    alltext = textfile.read()
#print(alltext)

#Convert to lowercase, split by whitespace to get words
word = alltext.lower().split()

#Count the frequency of each word
word_count_frequency = collections.Counter(word)

#Get the Top 30 most common words
top_30_common_words = word_count_frequency.most_common(30)
#print(top_30_common_words)

#Store result of top 30 common words in csv file: Q1_Task3.1_Top_30_common_words.csv
with open('Q1_Task3.1_Top_30_common_words.csv','w', newline= '', encoding='utf-8') as result:
    top30_file = csv.writer(result) #Write data into CSV file
    top30_file.writerow(['Common 30 words', 'Count frequency']) #Write name of the header
    top30_file.writerows(top_30_common_words) #Add value of top 30 common words in rows of csv file

#Print message after saving result successfully
print('Top 30 common words and their counts have been saved to Q1_Task3.1_Top_30_common_words.csv')
