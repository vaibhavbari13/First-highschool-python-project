from csv import writer

f=open('exercise_uw.csv','a')
list1=["20 squats","30 pushups","20 pull ups","20 lunges","20 bench press","20 overhead press"]
dt=writer(f)
dt.writerow(list1)
f.close()
