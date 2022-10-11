c=str(input("enter the character to be printed: "))
rows = int(input("Max no of time printed: "))
if rows>0:
    for i in range(rows):
        for j in range(i+1):
            print(c, end="")
        print("\n")
else:
    print("invalid")
