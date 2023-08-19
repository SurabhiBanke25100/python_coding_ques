#program to reverse a string
a=input("enter a string=")
rev_str=" "
for i in range(len(a),0,-1):
    rev_str += a[i]
print("reverse string=",rev_str)    
