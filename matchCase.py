#this program is about match case statement which is same as switch-case satatement in C
x=int(input("enter value of x "))
match x:
    case 0:
        print("value of x is 0")
    case 1:
        print("value of x is 1")
    case 2:
        print("value of x is 2") 

    case _ if x>10:
        print("the value of x is 3")
        
    case _:  #same as default case
        print(x)