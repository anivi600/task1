num=int(input("enter num"))
flag=0
for i in range (2,num):
    if num%i==0:
        flag=1
    else:
        flag=0
if flag==1:
    print("number is prime")
else:
    print("number is composite")