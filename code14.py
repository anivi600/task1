n=eval(input("enter number of elements"))
lst=[]
for i in range(n):
    element=int(input("enter element: "))
    lst.append(element)
print("list is:",lst)
m=int(input(" number of elements you want to delete"))
for i in range(m):
    element1=int(input("enter element"))
    lst.pop(element1)

print(lst)