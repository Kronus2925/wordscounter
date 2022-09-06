import re
import pandas as pd
import os

os.chdir(os.getcwd())

with open('lorem.ipsum.txt') as f:
    contents = f.read().lower()

def wordcounter(text: str):
    words = re.findall(pattern = r'[a-ząćęłńóśźż]+',
    string = text)
    d = {}
    for element in words:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1
    df = pd.DataFrame(d.items(),columns=['Słowo','Występowanie'])
    df.to_excel('licz_słowa.xlsx')
    return df   
print(wordcounter(contents))


