from csv import writer
from csv import reader
import random
print("      ...WELCOME TO DIGITAL GYM...")

def diet_ow():
    day=input('Enter day: ')
    f=open('diet_ow.csv','r')
    dt=reader(f)
    data=list(dt)
    f.close()
    for i in data:
        if i[0]==day:
            print(i)
def diet_h():
    f=open('diet_h.csv','r')
    dt=reader(f)
    data=list(dt)
    f.close()
    print('---------------------------------------------------------------')
    for  i in range(0,8):
        print(data[0][i])
    print('---------------------------------------------------------------')

def diet_uw():
    day=input('Enter day: ')
    f=open('diet_uw.csv','r')
    dt=reader(f)
    data=list(dt)
    f.close()
    print('---------------------------------------------------------------')
    for i in data:
        if i[0]==day:
            print(i)
    print('---------------------------------------------------------------')

def exercise_uw():
    f=open('exercise_uw.csv','r')
    dt=reader(f)
    data=list(dt)
    f.close()
    print('---------------------------------------------------------------')
    print('.................Lets Begain...............')
    print('.................Start With................')
    for i in range(0,6):
        print('        ',data[0][i])
        go=input('Press Enter For Next Exercise')
        if i<5:
            print('Then,')
    print('...........GOOD JOB.........')
    print('---------------------------------------------------------------')

def exercise_h():
    f=open('exercise_h.csv','r')
    dt=reader(f)
    data=list(dt)
    f.close()
    print('.................Lets Begain...............')
    print('.................Start With................')
    for i in range(0,7):
        print('        ',data[0][i])
        go=input('Press Enter For Next Exercise')
        if i<6:
            print('Then,')
    print('...........GOOD JOB.........')
    print('---------------------------------------------------------------')

def exercise_ow():
    f=open('exercise_ow.csv','r')
    dt=reader(f)
    data=list(dt)
    f.close()
    print('.................Lets Begain...............')
    print('.................Start With................')
    for i in range(0,5):
        print('        ',data[0][i])
        go=input('Press Enter For Next Exercise')
        if i<4:
            print('Then,')
    print('.........GOOD JOB..........')
    print('---------------------------------------------------------------')

def signup():
    f=open('digitalgym.csv','a',newline='\n')
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    height=float(input("Enter your Height in meter: "))
    weight=float(input("Enter your Weight in KG: "))
    id1=random.randint(100000,999999)
    bmi=weight/(height**2)
    list1=[id1,name,age,height,weight]
    dt=writer(f)
    dt.writerow(list1)
    f.close()
    if bmi<20:
        print('...YOU ARE UNDERWEIGHT...')
    elif bmi>=20 and bmi<=25:
        print('...YOU HAVE A GOOD BODY RATIO...')
    else:
        print('... YOU ARE OVERWEIGHT...')
    print('Your ID no. is',id1)
    print('   ...Now you are ready to go...')
    print('---------------------------------------------------------------')

def signin():
    f=open('digitalgym.csv','r')
    id1=input('Enter your id no.: ')
    dt=reader(f)
    data=list(dt)
    f.close()
    for i in data:
        if id1==i[0]:
            print('hello',i[1])
            sl=int(input("Select 1 for check diet or select 2 for to do some exercse: "))
            if sl==1:
                bmi=(float(i[4]))/((float(i[3]))**2)
                if bmi<20:
                    diet_uw()
                elif bmi>=20 and bmi<=25:
                    diet_h()
                else:
                    diet_ow()
                ach=int(input("Click 1 for continue or 2 for exiit: "))
                if ach==1:
                    signin()
                elif ach==2:
                    pass
                else:
                    print("invalid choice")
            elif sl==2:
                bmi=(float(i[4]))/((float(i[3]))**2)
                if bmi<20:
                    exercise_uw()
                elif bmi>=20 and bmi<=25:
                    exercise_h()
                else:
                    exercise_ow()
                ach=int(input("Click 1 for continue or 2 for exiit: "))
                if ach==1:
                    signin()
                elif ach==2:
                    pass
                else:
                    print("invalid choice")
        else:
            pass

ch=1
while ch==1:
    choice=input("signup or signin or exit: ")
    if choice=="signup":
        signup()
    elif choice=="signin":
        signin()
    elif choice=='exit':
        ch=2
    else:
        print('...Invaild Choice...')
