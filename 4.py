# 1.2 завдання (різниця матриць)
    import numpy as np
    
    A = np.array([[2, 3, 1], [-1, 1, 0], [1, 2, -1]])
    
    B = np.array([[1, 2, 1], [0, 1, 2], [3, 1, 1]])
    
    print("Printing elements of first matrix")
    print(A)
    print("Printing elements of second matrix")
    print(B)
    
    print("Subtraction of two matrix")
    print(np.subtract(A, B))

# 2.2 завдання (піднесення матриці до степеня)
    from numpy.linalg import matrix_power
    import numpy as np

    i = np.array([[-1, 0, 2], [0, 1, 0], [1, 2, -1]]) 
    matrix_power(i, 2)

# 3.2 завдання (добуток матриць)

    import numpy as np
    
    A = np.array([[5, 8, -4], [6, 9, -5], [4, 7, -3]])
    
    B = np.array([[3, 2, 5], [4, -1, 3], [9, 6, 5]])
    
    print("Printing elements of first matrix")
    print(A)
    print("Printing elements of second matrix")
    print(B)
    
    print("Subtraction of two matrix")
    print(np.dot(A, B))

# 3.4 завдання (добуток матриць)
   
    import numpy as np
    
    A = np.array([[5, 0, 2, 3], [4, 1, 5, 3], [3, 1, -1, 2]])
    
    B = np.array([[6], [-2], [7], [4]])
    
    print("Printing elements of first matrix")
    print(A)
    print("Printing elements of second matrix")
    print(B)
    
    print("Subtraction of two matrix")
    print(np.dot(A, B))

# 4.4 завдання(визначильники)
    def getcofactor(m, i, j):
        return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

    
    def determinantOfMatrix(mat):
    
    
        if(len(mat) == 2):
            value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
            return value
    
        Sum = 0
    
        for current_column in range(len(mat)):
    
            sign = (-1) ** (current_column)
    
        
            sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
    
        
            Sum += (sign * mat[0][current_column] * sub_det)
    
        return Sum
    
    
    if __name__ == '__main__':
    
    
        mat = [[1, 2, 3],
            [-1, 2, 1],
            [1, 3, 2]]
    
        print('Determinant of the matrix is :', determinantOfMatrix(mat))


# 5.3 завдання(визначильники)
    def getcofactor(m, i, j):
        return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

    
    def determinantOfMatrix(mat):
    
    
        if(len(mat) == 2):
            value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
            return value
    
        Sum = 0
    
        for current_column in range(len(mat)):
    
            sign = (-1) ** (current_column)
    
        
            sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
    
        
            Sum += (sign * mat[0][current_column] * sub_det)
    
        return Sum
    
    
    if __name__ == '__main__':
    
    
        mat = [[1, 2, 0, 0, 0],
            [1, 0, 2, 0, 0],
            [1, 0, 0, 2, 0],
            [1, 0, 0, 0, 2],
            [0, 0, 1, 1, 1]]
    
        print('Determinant of the matrix is :', determinantOfMatrix(mat))

# 6.5 завдання(обернена матриця)
    import numpy as np
    
    A = np.array([[1, 1, 1, 1],
                [1, 1, -1, -1],
                [1, -1, 1, -1],
                [1, -1, -1, 1]])
    
    print(np.linalg.inv(A))

# 7.3 завдання(ранг матриці)
    import numpy as np

    a = np.array([[-2,3,1,-1], [3,2,1,4], [1,2,3,4], [0,2,3,3]])

    rank = np.linalg.matrix_rank(a)

    print('Matrix : ', a)
    print('Rank of the given Matrix : ',rank)


 # 8.4 завдання(системa лінійних рівняньза формулами Крамера)  
    from numpy import linalg
        
        A=[[7,3,-6],[7,9,-9],[2,-4,9]
        B=[-1,5,-28]
        C=[[7,3,-6],[7,9,-9],[2,-4,9]
        X=[]
        for i in range(0,len(B)):
            for j in range(0,len(B)):
                C[j][i]=B[j]
                if i>0:
                    C[j][i-1]=A[j][i-1]
        X.append(round(linalg.det(C)/linalg.det(A),1))
        
    print('x=%s'%X[0],'y=%s'%X[1],'z=%s'%X[2])

    # 9.5 завдання(матричний метод системи рівнянь)  
        import numpy as np

        A = np.array([[4, 1, 4],
        [1, 1, 2],
        [2, 1, 2]]) 

        B = np.array([-2, -1, 0]) 

        print "Solutions:\n",np.linalg.solve(A, B ) 
        
     # 10.2 завдання
        import pandas as pd
    
            data = [
                    (20, 16, 23),
                    (30, 34, 11),
                    (40, 34, 11),
                    (50, 35, 23),
                    (60, 40, 13)
                    ]
            

            df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd', 'e'],
                                columns = ['x', 'y', 'z'])
            
            minvalue_series = df.min()
            
            minvalue_series
        print "Solutions:\n", df.min()
    