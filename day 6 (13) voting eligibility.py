try:
    age=int(input("enter your age: "))
    lt=18-age
    if age>=18:
        print("Eligible for voting ")
    elif(age>0 and age<18):
        print("you are allowed to vote after",lt," years")
    else:
        print("invalid")
except ValueError:
    print("enter a valid input")
