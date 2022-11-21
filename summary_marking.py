from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def similarity(X, Y):
    # X = input("Enter first string: ").lower()
    # Y = input("Enter second string: ").lower()
    # X = """the person wear red T-shirt
    # """
    # Y = """the boy wear red T-shirt"""
    # a=len(X)
    # b=len(Y)
    # print(b/a)
    # tokenization
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    # sw contains the list of stopwords
    sw = stopwords.words('english')
    l1 = []
    l2 = []

    # remove stop words from the string
    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)

    # print(rvector)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    return cosine
    
    
    
def summmarization_marking(student_answer,faculty_answers,faculty_marks):
    summary_mark=dict()
    for i in faculty_marks.items():

        if i[0] in student_answer.keys() : 

            summary_mark[i[0]]=similarity(student_answer.get(i[0]),faculty_answers.get(i[0]))*.6*int(i[1])
            if(summary_mark[i[0]]>.4*(int(i[1]))):
                summary_mark[i[0]]=.4*(int(i[1]))
    return summary_mark


