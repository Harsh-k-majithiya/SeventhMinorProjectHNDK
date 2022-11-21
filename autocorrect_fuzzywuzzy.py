from fuzzywuzzy import fuzz , process
def correctIt(student_list , faculty_list) :
    for i in range(len(student_list)) : 
        conf = process.extract(student_list[i], faculty_list , limit=10)
        if len(conf) > 0 :

            if (conf[0][1]) > 50 : # 50 for sample discuss
                student_list[i] = conf[0][0]
    return student_list