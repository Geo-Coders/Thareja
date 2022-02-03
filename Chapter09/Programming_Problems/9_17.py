# Write a program that has a class student with data members-- roll_no and marks in three subjects.
# Make at least four objects of this class. Use one or more function that find total of each student
# and then sorts the student's records in descending order basess on their marks.

print('--- A Program to display Students Records ---')
print()

class Student:
    def get_data(self):
        self.roll_no = input('Enter the Roll Number of the Student : ')
        self.list0 = []
        for i in range(4):
            subj_mark = int(input(f'Enter the marks of subject{i+1} : '))
            self.list0.append(subj_mark)
            i += 1 
    
    def __sum(self):
        return sum(self.list0)

    def __sorting_data(self):
        self.list0.sort(reverse=True)
        return self.list0
            
    def display(self):
        print(f"""
        1. The Roll Number : {self.roll_no}
        2. The Marks : {self.__sorting_data()}
        3. The sum of the marks : {self.__sum()}
        """)

a = Student()
a.get_data()
a.display()