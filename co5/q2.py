
f1 = open('clubs.txt', 'r')


f2 = open('clubs1.txt', 'w')


content = f1.readlines()
print(content)
type(content)
for i in range(0, len(content)):
	if(i%2!=0):
		f2.write(content[i])
	else:
		pass

f2.close()

f2 = open('clubs1.txt', 'r')


cont1 = f2.read()


print(cont1)


f1.close()
f2.close()
