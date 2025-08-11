s=input("Enter a string: ").split()
l1=[]
for i in s:
    if i.isalnum():
        l1.append(i.lower())
l1=''.join(l1)
print(l1[::-1]==l1)
