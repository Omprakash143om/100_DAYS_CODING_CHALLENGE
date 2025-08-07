string1=input("Enter a string: ")
dict1={}
for i in string1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for i in dict1:
    if dict1[i] > 1:
        print(f"Character '{i}' is duplicated {dict1[i]} times.")