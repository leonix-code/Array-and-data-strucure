import random 
temps = [[[random.randint(20, 30) for r in range(2)] for t in range(3)] for d in range(7)] 
 
flat = [t for d in temps for ti in d for t in ti] 
print(f"Highest Temperature: {max(flat)}°C") 
print(f"Lowest Temperature:  {min(flat)}°C")