# Write a program that determines whether a student is eligible for PG course or not. 
# To be elible, the student must have obtained more than 80% in X and XII examination, 
# and 70% plus marks in Graduation. if the student changes his stream (Science, Commerce, or Arts),
# then deduct 5% from his Graduation score.

print('--- A Program to determine the eligibility of a student ---')
print()

marks_x = int(input("Enter the marks obtain in the X: "))
grad_marks = int(input("Enter the Graduation marks: "))
exam_marks = int(input("Enter the XII Examination marks: "))

stream_change = input("Was there change of stream? (y/n): ")

print()

if (marks_x >= 80) and (exam_marks >= 80):
    if stream_change.lower() == 'y':
        grad_marks *= 100/105
        if grad_marks >= 70:
            print("Hurray! The student is eligible for PG Course!")
        else:
            print("Sorry! The student couldn't get the required Graduation Marks to Pass")
            pass
    else:
       if grad_marks >= 70:
            print("Hurray! The student is eligible for PG Course!")
       else:
            print("Sorry! The student couldn't get the required Graduation Marks to Pass")
            pass
else:
    print("Sorry! The student couldn't get the required pass in the exam marks")

