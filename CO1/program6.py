# Store a list of first names. Count the occurrences of ‘a’ within the list

li = []
c = 0
n=int(input("Enter Limit : "))
for i in range(n):
    x = input("enter names:")
    li.append(x)
for i in li:
    for j in i:
        if 'a' in j:
            c = c + 1
print("number of a is:", c)