def name():
    print("enter the name: ")
    n=input()
    return n
def marks():
    print("enter the mark of the student")
    english=int(input("enter the mark of eng"))
    hindi=int(input("enter the mark of hindi"))
    math=int(input("enter the mark of maths"))
    science=int(input("enter the mark of science"))
    total=(english+hindi+math+science)/4
    total=total*100
    return total

def desplay():
    grade=marks()
    if(grade>90):
       print("first devision")
    elif(garde>70):
       print("second devivion")
    elif(grade>50):
       print("third devision")
    else:
        print("fail")

name()
marks()
desplay()

