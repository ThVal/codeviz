import re
from sandbox import file


""" 

parse .txt in /data
-> word frequence 
"""

<<<<<<< HEAD:parser.py
=======
# open data
file = open('data/constitution.txt', 'r')
>>>>>>> main:doc_scrapper.py

# clean file.txt
content = ' '.join(line for line in file.read().splitlines()).lower().replace("'", " ").replace(",", " ")
content = re.sub("[0-9.,°€—'%)-]", '', content)
content = content.split(' ')

<<<<<<< HEAD:parser.py
# open stop_word file
stop_words_file = open('stop_words_french.txt', 'r')
# load stopwoard from stopwords.txt
=======
#open stop_word file
stop_words_file= open('stop_words_french.txt', 'r')

# transform stopword for data processing
>>>>>>> main:doc_scrapper.py
stop_words = ' '.join(line for line in stop_words_file.read().splitlines()).lower()

# dict of word : frequency
freqs = {}

for word in content:
    if word in stop_words:
        pass
    else:
        if word not in freqs:
            freqs[word] = 1
        else:
            freqs[word] += 1

file.close()
