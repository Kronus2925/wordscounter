import re
import pandas as pd
import os

os.chdir(os.getcwd())

with open('lorem.ipsum.txt') as f:
    contents = f.readlines()
    text = " ".join(contents).lower()

def wordcounter(text: str):
    words = re.split(pattern = r'[\W]+|[\d]',
    string = text)
    fullword = list(filter(lambda x: x!='' , words))
    d = {}
    for element in fullword:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1
    df = pd.DataFrame(d.items(),columns=['Słowo','Występowanie'])
    df.to_excel('licz_słowa.xlsx')
    return df   
print(wordcounter(text))


