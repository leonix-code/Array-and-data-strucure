A = [[1, 2], [3, 4]] 
B = [[5, 6], [7, 8]] 
res = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)] 
 
print("Resulting Matrix:") 
for row in res: print(row)