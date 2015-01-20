'''
1.6
'''
#Creates a 10*10 matrix
Matrix = [[0 for x in range(10)] for x in range(10)]

def func(matrix):
    n = len(matrix)
    if n%2 == 0:
        matrix = func2(matrix,n)
    else:
        n = n - 1
        matrix = func2(matrix,n)            
    return matrix

def func2(matrix,n):
    for layer in range(n/2):
        first = layer
        last = n-1-layer
        for i in range(first,last):
            offset = i - first
            #save top
            top = matrix[first][i]
            #left->top
            matrix[first][i] = matrix[last-offset][first]
            #bottom->left
            matrix[last-offset][first] = matrix[last][last-offset]
            #right->bottom
            matrix[last][last-offset] = matrix[i][last]
            #top->right
            matrix[i][last] = top
    return matrix


