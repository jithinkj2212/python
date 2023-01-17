str1="onion"
print("Before:"+str(str1))
word='$'
result=str1[0]+str1[1:].replace(str1[0],word)
print("After:"+str(result))
