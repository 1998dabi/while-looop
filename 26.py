a=int(input("enter number"))
pru=1
while pru<=a:
    b=a%10
    pru=pru*b
    a=a//10
print(pru)