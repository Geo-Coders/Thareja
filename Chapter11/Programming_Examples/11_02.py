# Write a program that overloads the + operator to add two objects of class matrix

class Matrix:
    def __init__(self, List):
        self.List = List
        
    def display(self):
        print(self.List)
        
    def __add__(self,M):
        Temp = Matrix([])
        for i in range(len(self.List)):
            for j in range(len(self.List[0])):
                Temp.List.append(self.List[i][j] + M.List[i][j])
        return Temp

M1 = Matrix([[1,2], [3,4]])
M2 = Matrix([[3,4], [5,1]])
M3 = Matrix([])
M3 = M1 + M2
print('RESULTANT MATRIX IS : ')
M3.display()