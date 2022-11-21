import warnings
warnings.filterwarnings("ignore")
keyword_obtained_marks = dict()

def give_marks_by_keywords(student_list, faculty_list , mark_dict={'1':5,'2':4}) :

    for i in mark_dict.items():

        if i[0] in student_list.keys() :
            # print('h'*20) 
            # print(faculty_list)
            # print('h'*20) 
            
            updated_student_inLower=[x.lower() for x in student_list.get(i[0])]
            updated_faculty_inLower=[x.lower() for x in faculty_list.get(i[0])]
     
            d= set(updated_student_inLower) & set(updated_faculty_inLower)
            # print(updated_student_inLower,len(updated_student_inLower))
            matched_score=len(d)/len(set(faculty_list.get(i[0])))
            keyword_obtained_marks[i[0]] = (matched_score*0.55*(int(i[1])))
            if(keyword_obtained_marks[i[0]]>=.4*(int(i[1]))):
                keyword_obtained_marks[i[0]]=.4*(int(i[1]))
            # if(keyword_obtained_marks[i[0]]<.4*i[1]):
            #     keyword_obtained_marks[i[0]]=.33*i[1]


    return keyword_obtained_marks


# ans = give_marks_by_keywords(

#     {
#         '1' : ['backend' , 'to' , 'to' , 'Application' , 'database'],
#         '2' : ['velOciTy' , 'variety' , 'variety']
#     }
#     ,
#     {
#         '1' : ['backend' , 'to' , 'to' , 'applIcaTion' , 'database'],
#         '2' : ['velocity','big','data' , 'variety' , 'variety']
#     }


# )
# print(ans)