#imports
import sys
import re
import collections
import string


def preprocess(student_file,faculty_file):
    
    #student's file processing
    student_file=student_file.replace("\n"," ")
    student_file=(re.sub( "Scanned with CamScanner","\n", student_file))
    stu_pagewise_list=student_file.split("\n")
    stu_pagewise_list.pop()

    #for appending multipaged questions
    dic={}
    for i in stu_pagewise_list:
        if str(i[14]) in dic.keys():
            dic[i[14]]+=i
        else:
            dic[i[14]]=i
    for i in dic:
        dic[i]=(re.sub(f"QUESTION NO.: {i}",".", dic[i]))

    #will generate list of students (question wise) 
    stu_words_list=[]
    for i in dic:
        words_list=dic[i]
        words_list=words_list.lower()
        words_list=words_list.replace("\n"," ")
        words_list=words_list.replace("."," ")
        words_list=words_list.replace(","," ")
        clear_def_dict = collections.defaultdict(str)
        innerlist=words_list.split(" ")
        for i in innerlist:
            if i in [':',';','.','!','?','@','#',')','(','&','->',',','-','_','<','-','>','::',' ',':-','"','-','','`','``','→',"'s" , '\u2192']:
                innerlist.remove(i)
            # corpus = i.translate(i.maketrans('', '', string.punctuation))

            # stu_words_list.append(i)
        stu_words_list=innerlist    
          
    #faculty's file processing
    faculty_words_list=[]
    words_list=faculty_file.lower()
    words_list=words_list.replace("\n"," ")
    words_list=words_list.replace("."," ")
    words_list=words_list.replace(","," ")
    words_list=words_list.split(" ")
    clear_def_dict2 = collections.defaultdict(str)
    for i in words_list:
            if i in [':',';','.','!','?','@','#',')','(','&','->',',','-','_','<','-','>','::',' ',':-','"','-','','`','``','→',"'s",'\u2192']:
                words_list.remove(i)
    faculty_words_list.append(words_list)
    
    return stu_words_list,faculty_words_list




def fun_tokenize() : 
    file=open('opFile.txt',"r",encoding='utf8')
    student_file=file.read()
    file.close()
    file=open("./ModelAnswersheetQ1.txt","r",encoding='utf8')
    faculty_file=file.read()
    file.close()
    stu_words_list,faculty_words_list=preprocess(student_file,faculty_file)
    return stu_words_list , faculty_words_list
