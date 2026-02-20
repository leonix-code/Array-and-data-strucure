scores = [[80, 75, 90, 85], [60, 70, 65, 80], [95, 88, 92, 90]] 
 
print(f"{'Student':<10} {'Total':<10} {'Average':<10}") 
for i, student in enumerate(scores): 
   t = sum(student) 
   print(f"{i+1:<10} {t:<10} {t/4:<10.2f}")