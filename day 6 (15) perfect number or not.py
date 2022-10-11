try:
    num=int(input("Enter the number: "))  
    sum_v=0  
    for i in range(1,num):  
        if (num%i==0):  
            sum_v=sum_v+i  
    if(sum_v==num):  
        print("Its a perfect number")  
    else:  
        print("Its not a perfect number")  
except ValueError:
    print("invalid")
