print("Enter the no. of lectures attended")
a=int(input())
print("Enter the no. of total lectures")
b=int(input())
cp=(a/b)*100
print("Current attendance is {} %".format(cp))
print("enter the lectures to be attended")
l=int(input())
nl =a+l
print("in number of days")
d=int(input())
total=b+(6*d)
cp1=(nl/total)*100
print("The tentative attendance will be {} %".format(cp1))
