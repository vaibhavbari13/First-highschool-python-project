from csv import writer
from csv import reader

f=open("diet_ow.csv",'a',newline='\n')
day=input('Enter Day: ')
diet=input("Enter diet: ")
list1=[day,diet]
dt=writer(f)
dt.writerow(list1)
f.close()
