set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

common_elements = []

for element in set1:
    if element in set2:
        common_elements.append(element)

print("Common elements:",common_elements)