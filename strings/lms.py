print("="*30)
print("LMS GRADE TRACKER")
print("="*30)


#VALIDATE ID

student_id_valid=False

while not student_id_valid:
    student_id=input("enter your id:")
    #check valid based on sign it is positive r negative
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("please enter only positive vales")
    elif student_id.isdigit():
        student_id=int(student_id)
        if student_id>0:
            student_id_valid=True
        else:
            print("please input non zero value")
    else:
        print("enter only numbers")
print(student_id)

#formatting id
formatted_id="STU"+str(student_id).zfill(5)
print(formatted_id)


#validating name

student_name_valid=False

while not student_name_valid:
    student_name=input("enter the name:" )
    student_name=student_name.strip().title()
    #strip will remove front and back spaces not in between
    
    #name check should have only alphabets
    name_check=student_name.replace(" ","")
    if name_check.isalpha() and len(student_name)>3:
        student_name_valid=True
        print("Name:"+student_name)
    else:
        if not name_check.isalpha():
            print("name should contain only letters")
        elif len(student_name)<3:
            print("name should contain at least 3 letters")
    
#email generation
name_part=student_name.split()
first_name=name_part[0].lower()
student_email=first_name+"."+str(student_id)+"@university.edu"

print(student_email)    

#discount calculation

base_course_fee_valid=False
while not base_course_fee_valid:
    base_course_fee=input("enter the course fee:")
    
    if base_course_fee.startswith("-")and base_course_fee[1:].isdigit():
        print("please enter only positive value")
        
    elif base_course_fee.isdigit():
        base_course_fee=int(base_course_fee)
        if base_course_fee>0:
            base_course_fee_valid=True
        else:
            print("enter only numbers")
    else:
        print("enter only numbers")
        
        
#calculation for fee

discount=0
print("enetr the description")
description=input()

if description.lower().find("reference")!=-1:
    discount+=5000
    
if "scholrship" in description:
    discount+=7000
    
if "promo" in description:
    discount+=3000

final_course_fee=base_course_fee-discount
print(final_course_fee)
        
print(f"base course fee:",base_course_fee)
print(f"discount u got:",discount)
print(f"final course fee:",final_course_fee)
    