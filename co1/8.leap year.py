start_year=int(input("enter the starting year"))
end_year=int(input("enter the last year"))
print("the first year is",start_year,"the last year is",end_year)
print("list of leap years")
for item in range(start_year,end_year):
    if(item%4==0)and (item%100!=0)or(item%400==0)and(item%100==0):
        print(item,"is a leap year")
