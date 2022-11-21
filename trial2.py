import random
import math
import xlsxwriter
import os

# workbook = xlsxwriter.Workbook('result.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.write('A1', 'ID')
# first='B' 

# entries = os.listdir('E:\\4IT43_MINOR_PROJECT\\test_pdfs')
# newlist=[]
# for i in entries:
#     s=i[:-4]
#     newlist.append(s)  

def no_of_ques(faculty_ans_dic,worksheet):
        first='B'
        questions=len(faculty_ans_dic)
       
        for i in range(questions):
                cell=first+str('1')
                question='Q'+str(i+1)
                worksheet.write(cell, question)
                first=chr(ord(first)+1)
        cell=first+str('1')
        worksheet.write(cell,"Total")
        return questions

# cell=first+str('1')
# worksheet.write(cell,"Total")


def gen_excel(param1,param2,param3,stu_name,count,worksheet):
        first=count+2
      
        
        for_id='A'
        cell=for_id+str(first)
        worksheet.write(cell, stu_name)
                
                # param1={"q1":random.random()*2,"q2":random.random()*1.5,"q3":random.random()*2,"q4":random.random()*1}
                # param2={"q1":random.random()*2,"q2": random.random()*1.5,"q3":random.random()*2,"q4":random.random()*1}
                # param3={"q1":random.random()*1,"q2":random.random()*1,"q3":random.random()*1,"q4":random.random()*1}

        for k in range(len(param1)):
        #taking question wise marks where a,b,c store marks of single question from different evaluation parameters 
                a=param1[str(k+1)]
                b=param2[str(k+1)]
                c=param3[str(k+1)]

                if (a>=(math.floor(a))) and (a<=(int(a)+0.5)):
                    if (abs(a-math.floor(a))>=abs(a-(int(a)+0.5))):
                        e=(int(a)+0.5)
                    else:
                        e=math.floor(a)
                else:
                    if (abs(a-math.ceil(a))>=abs(a-(int(a)+0.5))):
                        e=(int(a)+0.5)
                    else:
                        e=math.ceil(a)   
                
                if (b>=(math.floor(b))) and (b<=(int(b)+0.5)):
                    if (abs(b-math.floor(b))>=abs(b-(int(b)+0.5))):
                        f=(int(b)+0.5)
                    else:
                        f=math.floor(b)
                else:
                    if (abs(b-math.ceil(b))>=abs(b-(int(b)+0.5))):
                        f=(int(b)+0.5)
                    else:
                        f=math.ceil(b)   
                
                if (c>=(math.floor(c))) and (c<=(int(c)+0.5)):
                    if (abs(c-math.floor(c))>=abs(c-(int(c)+0.5))):
                        g=(int(c)+0.5)
                    else:
                        g=math.floor(c)
                else:
                    if (abs(c-math.ceil(c))>=abs(c-(int(c)+0.5))):
                        g=(int(c)+0.5)
                    else:
                        g=math.ceil(a)   
                
                
                        
                # if (a>=(math.floor(a))) and (a<=(int(a)+0.5)):
                #         e=(int(a)+0.5)
                # else:
                #         e=math.ceil(a)          
                # if (b>=(math.floor(b))) and (b<=(int(b)+0.5)):
                #         f=(int(b)+0.5)
                # else:
                #         f=math.ceil(b)          
                # if (c>=(math.floor(c))) and (c<=(int(c)+0.5)):
                #         g=(int(c)+0.5)
                # else:
                #         g=math.ceil(c)
                        
                total_mark_of_ques=e+g+f 

                for_id=chr(ord(for_id)+1)
                cell=for_id+str(first)
                worksheet.write(cell, total_mark_of_ques)
        for_id=chr(ord(for_id)+1)
        cell=for_id+str(first)
        for_id=chr(ord(for_id)-1)
        lastcell=for_id+str(first)
        firstcell="B"+str(first)
        formula="=SUM("+firstcell+":"+lastcell+")"
        worksheet.write(cell, formula)
