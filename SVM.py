from sklearn.svm import SVC
from numpy import genfromtxt, savetxt
import numpy as np
import csv

def main():
    #create the training & test sets, skipping the header row with [1:]
    dataset = genfromtxt(open('original.csv','r'), delimiter=',', dtype='f8')[1:]  #traindata  
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('test20000.csv','r'), delimiter=',', dtype='f8')[1:]	#testdata
    xtest = [x[1:] for x in test]

    rf=SVC()
    rf=rf.fit(train,target)

    savetxt('submission2.csv', rf.predict(xtest), delimiter=',', fmt='%f')
    sub = csv.reader(open("submission2.csv"))
    tes = csv.reader(open("test20000.csv"))
    l = list(sub)
    k=[]
    m = list(tes)

    for i in range(len(m)):
        if i!=0:
            k.append(m[i][0])
    correct=0
    TN=0.0
    FN=0.0
    TP=0.0
    FP=0.0
    for i in range(len(l)):
        if int(float(l[i][0]))==int(float(k[i][0])):
            if int(float(l[i][0]))==0:
                TN+=1
            else:
                TP+=1
            correct+=1
        else:
            if int(float(l[i][0]))==0:
                FN+=1
            else:
                FP+=1

    count=len(l)
    accuracy=(float(correct)/float(count))*100
    try:
        precision= TP/(TP+FP)
    except ZeroDivisionError:
        precision=0
    try:
        recall= TP/(TP+FN)
    except ZeroDivisionError:
        recall=0
    try:
        f1score=2*((precision*recall)/(precision+recall))
    except ZeroDivisionError:
        f1score=0

    print "Accuracy     %f" % accuracy
    print "Precision    %f" % precision
    print "Recall       %f" % recall
    print "F1 Score     %f" % f1score
if __name__=="__main__":
    main()
