from os import remove
from keybert import KeyBERT
import warnings
warnings.filterwarnings("ignore")
model = KeyBERT(model="distilbert-base-nli-mean-tokens")

def fun_keyword_extraction(list) : 
    for i in list : 
        if i == '' : 
            list.remove(i)
    key_list = model.extract_keywords(
        list,
        top_n=int(len(list)/2),
        keyphrase_ngram_range=(1, 1),
        stop_words="english",
    )
    mylist=[]
    for i in key_list:
        mylist.append(i[0])
    # print(len(mylist))
    return mylist

