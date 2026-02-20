mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
trans = [[mat[j][i] for j in range(3)] for i in range(3)] 
 
print("Original:") 
for r in mat: print(r) 
print("Transpose:") 
for r in trans: print(r)