def length_wise_marking(student_answers,faculty_answers,faculty_marks):
    marks=dict()
    print(student_answers)
    for i in student_answers.items():
        lx = student_answers.get(i[0]).split(' ')
        sl = len(lx)
        fl=len(faculty_answers.get(i[0]))
        print(i[0] + 'h')
        marks[i[0]]=(sl/fl)*0.2*(int(faculty_marks.get(i[0])))
        if(marks[i[0]]>.2*(int(faculty_marks.get(i[0])))):
            marks[i[0]]=.2*(int(faculty_marks.get(i[0])))
    return marks

        