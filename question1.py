marks = [] 
for i in range(10): 
   m = float(input(f"Enter mark for student {i+1}: ")) 
   marks.append(m) 
 
total = sum(marks) 
avg = total / 10 
 
print("\n--- Results ---") 
print(f"Total Marks: {total}") 
print(f"Average Mark: {avg:.2f}") 
print(f"Highest Mark: {max(marks)}") 
print(f"Lowest Mark: {min(marks)}") 
 