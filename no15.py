
b=int(input("enter number"))
i=1
d=0
while b!=0:
    r=b%10
    b=b//10
    d=d+r*i
    i=i*2
print("decimal number is",d)