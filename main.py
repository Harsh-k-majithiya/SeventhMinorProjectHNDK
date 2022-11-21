import string
import text_extract
import keyword_extractation
import answer_dictionary
import autocorrect_fuzzywuzzy
import keyword_marking
import warnings
from lengthwisemarking import length_wise_marking
from trial2 import no_of_ques
warnings.filterwarnings("ignore")
from summarization import summarization_student
from summary_marking import summmarization_marking
from trial2 import no_of_ques
from trial2 import gen_excel
import xlsxwriter
import os
# text_extract.fun_text_extract(r'test_pdfs\\19IT450_MinorProj.pdf')

# student_word_list , faculty_word_list = tokenization.fun_tokenize()


#excel code
workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'ID')
# workbook.close()

first='B'
entries = os.listdir('C:\\Users\Harsh Majithiya\\Documents\\nikhilproject\\4IT43_MINOR_PROJECT\\Students_Answer')
newlist=[]
for i in entries:
    newlist.append(i)  

# faculty code : 
faculty_answers ,faculty_marks= answer_dictionary.fun_facutly_answer_dictionarywise()
faculty_answers_dict = dict()

cnt = 1
for i in faculty_answers.values() : 
    faculty_answers_dict[str(cnt)] = keyword_extractation.fun_keyword_extraction(i)
    cnt = cnt + 1

print(faculty_answers_dict)

tot_ques=no_of_ques(faculty_answers_dict,worksheet)


faculty_summary_dict=summarization_student(faculty_answers)
# print(faculty_summary_dict)
# faculty_marks={'1' : 5 , '2'  : 4}

# student code : 

count=0
for i in range(len(newlist)) : 
    print(newlist[i])
    student_answers_dict = dict()   

    text_extract.fun_text_extract(f'Students_Answer\\{newlist[i]}')

    student_answer = answer_dictionary.fun_student_answer_dictionarywise()
    # print(student_answer)
    #length wise marking
    len_marks=length_wise_marking(student_answer,faculty_answers_dict,faculty_marks)
   
   





    cnt = 1
    for i in student_answer.values() : 
        i = i.translate(str.maketrans('', '', string.punctuation))

        faculty_answer_str = faculty_answers.get(str(cnt))
        # print(faculty_answer_str + 'h'*20)
        faculty_answer_str = faculty_answer_str.translate(str.maketrans('', '', string.punctuation))


        student_answers_dict[str(cnt)] = autocorrect_fuzzywuzzy.correctIt(i.split(" "), faculty_answer_str.split(' '))
        cnt = cnt + 1
    ans = keyword_marking.give_marks_by_keywords(student_answers_dict , faculty_answers_dict, faculty_marks)
    

    student_summary_dict=summarization_student(student_answer)

    summary_marks_dict=summmarization_marking(student_summary_dict,faculty_summary_dict,faculty_marks)
    
    print(summary_marks_dict)
    print("===================")
    print(len_marks)
    print("===================")
    print(ans)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


    gen_excel(summary_marks_dict,len_marks,ans,newlist[count],count,worksheet) 
    count+=1   
# print("=======================================================")
# print(student_summary_dict)
# print("-----------------------------------------------------")



# student_keyword_list = (keyword_extractation.fun_keyword_extraction(student_word_list))
# print(student_keyword_list)
workbook.close()