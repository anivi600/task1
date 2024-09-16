my_list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)
print("list 1 is:",my_list)
lst1=[]
for i in range(n):
    element2= input("enter element")
    lst1.append(element2)
print("list 2 is:",lst1)
dict={}
for i in range(n):
    dict[my_list[i]] = lst1[i]
print("dictionary is:", dict)