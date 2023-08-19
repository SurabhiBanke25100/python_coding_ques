#program to find sum of digits
a=int(input("enter no="))
sum=0
while a>0:
    t=a%10
    sum+=t
    a//=10
print("sum=",sum)    
    