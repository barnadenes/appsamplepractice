import math
import cmath

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

diszkriminans = b**2-4*a*c

if diszkriminans < 0:
    print("This equation has no real solution")
elif diszkriminans == 0:
    x0 = (-b+math.sqrt(b**2-4*a*c))/2*a
    print("This equation has one solution: ", x0)
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print ("This equation has two solutions: ", x1, " or", x2)
