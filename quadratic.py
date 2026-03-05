import math
a = int(input("Enter the value of  a: "))
b = int(input("Enter the value of  b: "))
c = int(input("Enter the value of  c: "))
q = b * b - (4 * a * c )
if q == 0:
   x1 = -b / (2 * a)
   print("Roots are real and equal")
   print("Root =", x1)
elif q < 0:
   x1 = -b / (2 * a)
   x2 = math.sqrt(-q) / (2 * a)
   print("Roots are imaginary")
   print(x1, "+ j", x2)
   print(x1, "- j", x2)
else:
   x1 = (-b + math.sqrt(q)) / (2 * a)
   x2 = (-b - math.sqrt(q)) / (2 * a)
   print("Roots are real and distinct")
   print("Root 1 =", x1)
   print("Root 2 =", x2)
