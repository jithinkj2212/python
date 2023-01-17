import operator
d={1:8,3:5,4:3,2:7,0:1}
print("original dictionary:",d)
s_d=sorted(d.items(),key=operator.itemgetter(1))
print("dictionary in asending order by value:",s_d)
s_d=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("dictionary in descending order by value:",s_d)
