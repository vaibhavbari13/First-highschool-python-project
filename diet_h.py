from csv import writer

data=['1. Base yo;ur meals on higher fiber starchy carbohydrates... ','2. Eat lots of fruit and veg...',' 3.eat more fis, including a portion of oily fish....',' 4. Cut downon saturated fat and suger.... ','5. Eat less salt no more than6g a day for adults...',' 6. Get active and be a healthy weight...',' 7 Do not get thirsty....',' 8. Do not skip breakfast...']
f=open("diet_h.csv",'w')
dt=writer(f)
dt.writerow(data)
f.close()
