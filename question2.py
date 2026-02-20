arr = [12, 45, 7, 23, 56, 89, 34, 10] 
print("Array:", arr) 
search = int(input("Enter number to search: ")) 
 
if search in arr: 
   print(f"Number exists at index: {arr.index(search)}") 
else: 
   print("Number does not exist in array.")