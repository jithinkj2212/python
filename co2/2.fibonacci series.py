num=int(input("Enter nth term :"))
a=0
b=1
print(a)
print(b)
for i in range (num-2):
    fib=a+b
    print(fib)
    a=b
    b=fib
