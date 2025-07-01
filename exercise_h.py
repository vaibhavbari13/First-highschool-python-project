from csv import writer

f=open('execise_h.csv','w')
list1=['standing overhead 10 pound dumbbell presses','10 pound dumbbell rows','single leg deadlifts','Burpees','side planks','planks','glute bridge']
dt=writer(f)
dt.writerow(list1)
f.close()
