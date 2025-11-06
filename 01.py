# making KBC game using free mind ( i will use if else )
mm="Welcome to KBC"
print(mm.center(70))
q=int(input("enter quesion number(1-4) = "))

l1=["1:sagarmatha","2:machhapuchhre","3:makalu","4:kanchanjunga"]
if(q==1):
    print("which is the highest peak in the world ? \n",l1)
    ans=int(input("enter correct answer number : "))
    if(ans==1):
        q1=4000
        print("correct answer")
        print("you won 4000")
    else:
        q1=0
        print("false answer ! ,","true answer is",l1[0])

l2=["1:bleach","one piece","3:naruto","4:HxH"]
if(q==2):
 print("which is not the member of big 3? \n",l2)
 ani=int(input("enter correct answer number : "))
 if(ani==4):
    q2=3000
    print("correct answer")
    print("you won 3000")
 else:
    q2=0
    print("false answer ! ,","true answer is",l2[3])


l3=["1:sprite","miranda","3:coca-cola","4:appi"]
if(q==3):
 print("which is not the coca-cola product? \n",l3)
 ani=int(input("enter correct answer number : "))
 if(ani==4):
    q3=5000
    print("correct answer")
    print("you won 5000")
 else:
    print("false answer ! ,","true answer is",l3[3])

l4=["1:2019 (December(second week))","2:2019(december(first week))","3:2019(december(last week))","4:2019(december(third week))"]
if(q==4):
 print("In which date was covid 19 first identified?\n",l4)
 ani=int(input("enter correct answer number : "))
 if(ani==3):
    q3=5000
    print("correct answer")
    print("you won 5000")
 else:
    print("false answer ! ,","true answer is",l4[2])