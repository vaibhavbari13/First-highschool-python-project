from csv import writer

f=open('exercise_ow.csv','w')
list1=["burpees","squats,lunges","pushh ups","planks","low box running"]
dt=writer(f)
dt.writerow(list1)
f.close()

