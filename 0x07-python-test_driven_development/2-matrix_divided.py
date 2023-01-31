def matrix_divided(matrix, div):
    if not isinstance(matrix , list):
        raise TypeError("atrix must be a matrix (list of lists) of integers/floats")
    print( isinstance(div , int) , isinstance(div , float))
    if not (isinstance(div , int) or isinstance(div , float)):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    n = 0
    for x in range(len(matrix)):
        if not isinstance(matrix[x] , list):
            raise TypeError("atrix must be a matrix (list of lists) of integers/floats")
        if x == 0:
            n = len(matrix[0])
        elif len(matrix[x]) != n:
            raise TypeError ("Each row of the matrix must have the same size")
        
        for j in range(len(matrix[x])):
            if not (isinstance(matrix[x][j] , int) or isinstance(matrix[x][j] , float)):
                raise TypeError("atrix must be a matrix (list of lists) of integers/floats")
            
            matrix[x][j]  = round(matrix[x][j] /div , 2)

    
    return matrix



