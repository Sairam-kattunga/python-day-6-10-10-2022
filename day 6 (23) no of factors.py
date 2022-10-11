def getFactors(n):
    factors=[];
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors
a=str(input("N= "))
if a==int:
    n= (getFactors(a))
    print("no of factors for given number: ",len(n))
else:
    print("invalid")
