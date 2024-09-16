lst = []
newstr=''
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = str(input("Enter element: "))
    lst.append(element)
for i in range (n):
    newstr=newstr+lst[i]
print("final string:",newstr)