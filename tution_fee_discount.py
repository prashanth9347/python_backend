student_name = input("enter the name: ")
student_grade = int(input("enter the grade: "))
Base_tution_fee = int(input("enter the tuition fee: "))
discount_percentage = 0
academic_topper = input("enter true or false: ")

if student_grade > 0 and student_grade <= 12:
    if student_grade >= 9 and student_grade <= 12:
        if academic_topper == "true":
            total_discount = 20
        else:
            total_discount = 10
    elif student_grade >= 6 and student_grade <= 8:
        total_discount = 5
    else:
        total_discount = 0

    if student_grade == 10:
        total_discount = total_discount + 3
    elif student_grade == 12:
        total_discount = total_discount + 5
    else:
        total_discount = total_discount + 0

    if discount_percentage > 0:
        total_discount = total_discount + discount_percentage

    discount_amount = (Base_tution_fee * total_discount) / 100
    final_fee = Base_tution_fee - discount_amount

    print(f"student name: {student_name}")
    print(f"Grade: {student_grade}")
    print(f"academic topper: {academic_topper}")
    print(f"Base tuition fee: {Base_tution_fee}")
    print(f"total discount: {total_discount}%")
    print(f"discount amount: {discount_amount}")
    print(f"final tuition fee: {final_fee}")
else:
    print("invalid grade")
