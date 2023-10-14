import pandas as pd
import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_lg')
nlp.add_pipe("merge_entities")

def main():
    data = {"MRN": [123456, 789456123], "text": ["Hello Benzon!", "Hi are you available today?"]}
    df = pd.DataFrame(data=data)
    df["new_text"] = df["text"].apply(lambda x: deidentify(x))
    print(df)


def deidentify(st):
    doc = nlp(st)
    newString = st

    #reversed to not modify the offsets of other entities when substituting
    for e in reversed(doc.ents): 
        start = e.start_char
        end = start + len(e.text)
        newString = newString[:start] + e.label_ + newString[end:]
    return newString


if __name__ == '__main__':
    main()