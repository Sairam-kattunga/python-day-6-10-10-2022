try:
    n =int(input("Enter the number of rows:"))
    if n>0:
        for r in range(1, n+1):
            for m in range(r, 0,-1):
                print(m, end=' ')
            print("")
    else:
        print("Invalid")
except ValueError:
    print("Enter valid input")
