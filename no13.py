a=int(input("enter number"))
i=2
s=0
sum=0
while i<=a:
    if i%2==0:
        s=s+i**2
        i=i+1
    else:
        sum=sum+i**2
        i=i+1
        c=s-sum
        print(c,end="")