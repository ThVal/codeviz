import pandas as pd
import re

file = open('data/ddhc.txt', 'r')
stop_words_file= open('stop_words_french.txt', 'r')

stop_words = ' '.join(line for line in stop_words_file.read().splitlines()).lower()
content = ' '.join(line for line in file.read().splitlines()).lower().replace("'"," ").replace(","," ")
content= re.sub("[0-9.,°€—'%)-]",'', content)
#content= re.sub("[]", '', content)
content = content.split(' ')

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


