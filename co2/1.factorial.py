s=int(input("enter the number"))
fact=1
if(s==0):
   print("the factorial is 1")
else:
    for i in range(1,s+1):
        fact=fact*i
print("Factorial of",s,"is",fact)
