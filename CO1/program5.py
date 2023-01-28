# Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead
mylist = []
n=int(input("Enter the Limit : "))
for x in range(n):
    x = int(input("enter the number:"))
    if(x<100):
        mylist.append(x)
    else:
        mylist.append("over")
print(mylist)
