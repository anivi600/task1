lst1 = []
lst3=[]
n = int(input("Enter the number of elements in list 1: "))
for i in range(n):
    element = int(input("Enter element: "))
    lst1.append(element)
lst2=[]
m=int(input("Enter the number of elements in list 2: "))
for i in range(m):
    element2 = int(input("Enter element: "))
    lst2.append(element2)
for i in lst1[0:]:
    for j in lst2[0:]:
        if i==j:
            lst3.append(i)
print("final",lst3)