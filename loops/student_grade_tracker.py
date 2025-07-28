student_id=int(input("enter the student id:"))
student_name=input("enter the student name:")
attendance=int(input("enter the attendance :"))
number_of_subject=0
total_score=0


while True:
    score=int(input("enter the marks:" ))
    total_score+=score
    number_of_subject+=1
    
    x=input("do u want to continue and enter the marks?input yes/no:")
    if x!="yes" :
        break
    
if number_of_subject>0:
    average_score=total_score/number_of_subject
else:
    average_score=0
    
if average_score>=85:
    perf="Excellent"
elif average_score>=70:
    perf="Good"
elif average_score>=50:
    perf="average"    
else:
    perf="need improvement"
    
    
if attendance<75:
    attendance_status="low attendance"
else:
    attendance_status="satisfied attendance"
    
    

print("student id:",student_id)
print("student_name:",student_name)
print("total score:",total_score)
print("num of subjects:",number_of_subject)
print("average score:",average_score)
print("performance:",perf)
print("attendance:",attendance)
print("attendance status:",attendance_status)
    
    