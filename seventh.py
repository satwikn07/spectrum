import math
num=int(input("Enter the number: "))
  
 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  

def isFibonacci(n): 
   return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
 
 
if (isFibonacci(num) == True): 
         print (num,"is a Fibonacci Number")
else: 
         print (num,"is a not Fibonacci Number ")
