
a=int(input("enter number"))
i=0
sum=0
while i<=a:
    b=int(input("enter number"))
    sum=sum+a
    i=i+1
total_sum=sum
avg=total_sum//a
print(avg)
if avg%5==0:
    print("avg it is multiple by 5")
else:
    print("avg it is not multiple by 5")
