l=[]
n=4
print("enter the numbers")
for i in range(n):
    num=int(input("no"))
    l.append(num)
print(l)
for i in range(len(l)):
    if(l[i]>100):
        l[i]="over"
print(l)
