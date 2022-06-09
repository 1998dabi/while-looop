a=int(input("enter number"))
row=1
while row<=a:
    j=1
    while j<=a-row:
        print(" ",end="")
        j=j+1
    c=1
    while c<=row:
        print(c,end="")
        c=c+1
    print()
    row=row+1
