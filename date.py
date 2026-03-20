d=input("enter a the date of birth")
if " " in d:
    print("space is not allowed")
a=d.split("/")
print("your date of birth is the day of  "+a[0] + ",on the month of  "+a[1]+",in the year  "+a[2])