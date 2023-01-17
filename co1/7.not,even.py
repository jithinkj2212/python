l=[]
oddl=[]
n=6
print("enter he numbers")
for i in range(n):
    num=int(input("no"))
    l.append(num)
print("entered list is",l)
for item in l:
    if(item%2!=0):
        oddl.append(item)
print("new list is",oddl)
