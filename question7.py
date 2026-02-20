data = [[[80, 90], [70, 75], [60, 65]], [[85, 95], [77, 88], [90, 92]]] 
 
all_marks = [] 
for i, cls in enumerate(data): 
   cls_marks = [m for std in cls for m in std] 
   print(f"Class {i+1} Average: {sum(cls_marks)/len(cls_marks):.2f}") 
   all_marks.extend(cls_marks) 
 
print(f"Overall Average: {sum(all_marks)/len(all_marks):.2f}")