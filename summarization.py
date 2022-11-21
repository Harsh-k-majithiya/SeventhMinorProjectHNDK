
from multiprocessing.spawn import prepare
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('wordnet')
nltk.download('omw-1.4')

nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys

def summarization_student(student_answer):
    student_summary_dict=dict()
    k=1

    for i in student_answer.items():
        text=student_answer.get(i[0])
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)

        

        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1

  
        sentences = sent_tokenize(text)
        sentenceValue = dict()

        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq

        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]


        average = int(sumValues / len(sentenceValue))
        
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence
        

        student_summary_dict[i[0]]=summary
    k=k+1
    return student_summary_dict
