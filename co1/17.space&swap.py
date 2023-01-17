n1=input("enter string1\n")
n2=input("enter string2\n")
a=n1[0:1]
n1=n1.replace(n1[0:1],n2[0:1])
n2=n2.replace(n2[0:1],a)
print(f"{n1} { n2}")
