a=int(input("enter first number"))
i=1
while i<=5:
    b=int(input("enter second numter"))
    if a==b:
        print("your givess is currect")
    elif a<b:
        print("you givess smoller")
    elif a>b:
        print("entered is greater")
        i=i+1
        break
    else:
        print("wrong")
