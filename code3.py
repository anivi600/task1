lst = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter element: "))
    lst.append(element)
maxi=lst[0]
for i in range(0,n):
    if lst[i]>maxi:
        maxi=lst[i]
print("max is", maxi)