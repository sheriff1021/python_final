class MakeMatrix():    
    def Get_Matrix(self):
        R = int(input("Enter the number of rows:"))
        C = int(input("Enter the number of columns:"))
        matrix = []
        print("Enter the entries rowwise:")
        for i in range(R):    
            a =[]
            for j in range(C):
                 a.append(int(input()))
            matrix.append(a)
        return matrix
    def Print_Matrix(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                print(matrix[i][j], end = " ")
            print()
    def Is_Identity(self,matrix):
        flag=True
        rows=len(matrix)
        cols=len(matrix[0])
        if(rows!=cols):
            print("identity matrix can be only square")
        else:
            for i in range(0,rows):
                for j in range(0,cols):
                    if(i==j and matrix[i][j]!=1):
                        flag=False
                        break;
                    if(i!=j and matrix[i][j]!=0):
                        flag=False
                        break
            if(flag):
                print("given matrix is edintity")
            else:
                print("given matrix is not edintity")
    def Is_Square(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        if(rows!=cols):
            print("imatrix is not suqare")
        else:
            print("matrix is square")
    def Is_Zero(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        flag=True
        for i in range(0,rows):
                for j in range(0,cols):
                    if(matrix[i][j]!=0):
                       flag=False
                       break
                    else:
                        flag=True
        if(flag):
            print("zero matrix")
        else:
            print("not zero matrix")
    def Is_Diagonal(self,matrix):
        flag=True
        rows=len(matrix)
        cols=len(matrix[0])
        if(rows!=cols):
            print("identity matrix can be only square")
        else:
            for i in range(0,rows):
                for j in range(0,cols):
                    if(i!=j and matrix[i][j]!=0):
                        flag=False
                        break
            if(flag):
                print("given matrix is diagonal")
            else:
                print("given matrix is not diagonal")
    def Transpone(self,matrix):
        new_matr=list(zip(*matrix))
        return new_matr
    def Sum_Matrix(self,m1,m2):
        rows=len(m1)
        cols=len(m2)
        result=[([0]*cols) for i in range(rows)]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j]=m1[i][j]+m2[i][j]
        return result
    def Subtraction_Matrix(self,m1,m2):
        rows=len(m1)
        cols=len(m2)
        result=[([0]*cols) for i in range(rows)]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j]=m1[i][j]-m2[i][j]
        return result
    def Multiplication_Matrix(self,m1,m2):
        rows=len(m1)
        cols=len(m2)
        result=[([0]*cols) for i in range(rows)]
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                result[i][j]=m1[i][j]*m2[i][j]
        return result
l=MakeMatrix()
m1=l.Get_Matrix()
m2=l.Get_Matrix()
R=l.Multiplication_Matrix(m1,m2)
l.Print_Matrix(R)