rows=int(input("enter number of rows:"))
for i in range(1,rows+1):
    for j in range(0,i):
        print("*",end="")
    print() # this will print a new line after each row of stars