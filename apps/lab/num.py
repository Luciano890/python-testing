import numpy as np    
n = 0
matrix = np.zeros((4,6)) # Pre-allocate matrix
print(matrix)
while n < 4:
    try:
        matrix[n,:] = [*map(int, input().split())]
        n+=1
    except ValueError:
        print("error in input length.")
    
print(matrix)