try:
    def factorial(n):
        return 1 if (n==1 or n==0) else n * factorial(n - 1);
    num = int(input("enter the number: "));

    if (num>0):
        print("Factorial of",num,"is",
        factorial(num))
    else:
        print("invalid")
except ValueError:
    print("invalid")

    
