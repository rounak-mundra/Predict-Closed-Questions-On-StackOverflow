import csv,sys
import matplotlib.pyplot as plt

input_file = sys.argv[1]
reader = csv.reader( open( input_file ))


x0=[]
y0=[]
x1=[]
y1=[]
counter = 0	
for line in reader:
	if counter!=0:
		if line[0]=='0':
			y0.append(float(line[8]))
			x0.append(float(line[4]))
		else:
			y1.append(float(line[8]))
			x1.append(float(line[4]))
	counter+=1
plt.ylabel("OwnerUndeletedAnswerCountAtPostTime")
plt.xlabel("ReputationAtPostCreation")
plt.plot(x0,y0,'ro',x1,y1,'bo')
#plt.axis([1500,3000,0,15])
plt.show()