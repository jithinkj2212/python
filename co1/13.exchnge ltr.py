string="python"
a=list(string)
temp=a[0]
a[0]=a[-1]
a[-1]=temp
print("".join(a))
