num=int(input("enter number"))
onum=num
r=0
n=0
len=len(str(num))
i=0
while (i<len):
    r=num%10
    n=n*10+r
    num=num//10
    i=i+1
if onum==n:
    print("num is palidrom")
else:
    print("num is not palimdrame")