names=[]
scores={}
def take_input():
    while True:
            temp_name=input("enter the name of the student:\n").title()  
            if temp_name=='Done':
                break
            else:
                names.append(temp_name)
                marks=input('Enter Marks seprated by space').split()
                marks=list(map(int,marks))

            #dictionary  score[key]=value
                scores[temp_name]=marks

def avg_cal(scores):
    return sum(scores)/len(scores)

def grade(avg):
    if 90< avg<=100:
        return 'A'
    elif 70<avg<=90:
        return 'B'
    else:
        return 'FAIL'
def output():
    for name in names:
        avg=avg_cal(scores[name])
        grade1=grade(avg)
        print(f'the garde of {name} is {grade1}')

take_input()
output()