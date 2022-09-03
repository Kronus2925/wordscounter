import re
import pandas as pd

with open('lorem.ipsum.txt') as f:
    contents = f.readlines()
    text = " ".join(contents).lower()

def wordcounter(text: str):
    words = re.split(pattern = r'[][\-\d ,.\(\)\n\:]',
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
print(wordcounter(text))


