string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

string1 = string1.lower()
string2 = string2.lower()   
sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)
if sorted_string1 == sorted_string2:
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.") 