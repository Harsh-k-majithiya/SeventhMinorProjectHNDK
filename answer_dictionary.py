import warnings
warnings.filterwarnings("ignore")
import re

def fun_student_answer_dictionarywise() : 
    f=open("opFile.txt","r",encoding='utf-8')
    s=f.read()
    s=s.replace("\n"," ")
    texts=s

    # a=texts.count("Scanned with CamScanner")
    # while a>0:
    #     if "Scanned with CamScanner" in texts:
    #         texts.replace("Scanned with CamScanner"," ")
    #         a-=1
    stri = texts
    stri=(re.sub("Scanned with CamScanner", "\n", stri))
    li=stri.split("\n")
    li.pop()
    dic={}
    # print(li)
    for i in li:
    #     print(i[14])
        if (i[14] == ' ' or i[14] == '\n') and i[13].isdigit() : 
    
            digit = i[13]
        else : 
            digit = i[14]
        
            if str(digit) in dic.keys():
                dic[digit]+=i
            else:
                dic[digit]=i
    dic
    for i in dic:
        dic[i]=(re.sub(f"QUESTION NO.: {i}",".", dic[i]))
        # dic[i]=(re.sub(f"QUESTION NO.:{i}",".", dic[i]))
        
    return (dic)



def fun_facutly_answer_dictionarywise() : 
    f=open("C:\\Users\\Harsh Majithiya\\Documents\\nikhilproject\\4IT43_MINOR_PROJECT\\Faculty_Answer\\ModelAnswersheet.txt","r",encoding='utf-8')
    s=f.read()
    # print(s)
    s=s.replace("\n"," ")
    answer_of_faculty=s
    li=answer_of_faculty.split('QUESTION NO.: ')
    li.pop(0)
    mark_dict={}
    newl=[]
    k=1
    for i in li:
        mark_dict[str(k)]=i[8:10]
        news=i[10:]
        newl.append(news)
        k+=1

    dic={}
    k=1
    for i in newl:
        dic[str(k)]=i
        k+=1
    return dic,mark_dict
    
# a,b=fun_facutly_answer_dictionarywise()
# print(a,b)