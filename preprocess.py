'convert from CSV to txt format'

import sys, csv, re
import datetime,time
import nltk
import string
from collections import Counter
from stop_words import get_stop_words
from nltk.stem.porter import *



input_file = sys.argv[1]
output_file = sys.argv[2]


def diffdate(postdate):
	x=postdate[0:2]+postdate[3:5]+postdate[6:10]+postdate[11:13]+postdate[14:16]+postdate[17:19]
	try:
		d=datetime.datetime.strptime(x,"%m%d%Y%H%M%S").date()
	except ValueError:
		d=datetime.datetime.now().date()
	cd=datetime.datetime.now().date()
	delta=cd-d
	return delta.days

reader = csv.reader( open( input_file ))
o = open( output_file, 'wb' )
en_stop = get_stop_words('en')

counter = 0	
for line in reader:

	if counter == 0:
		output_line="Status,Post_Id,TitleLength,BodyLength,ReputationAtPostCreation,DateDifferenceQues,TagsNo,UserAge,OwnerUndeletedAnswerCountAtPostTime,LinksCount\n"
		o.write(output_line)
	else:
		dayDiffQues=diffdate(line[1])-(3*365)
		userAge=diffdate(line[3])-(3*365)
		OwnerUndelAnsCountAtPostTime=line[5]
		b_lower=line[7].strip().lower()
		t_lower=line[6].strip().lower()
		b_no_punctuation = b_lower.translate(None, string.punctuation)
		t_no_punctuation = t_lower.translate(None, string.punctuation)
		b_tokens = nltk.word_tokenize(b_no_punctuation)
		t_tokens = nltk.word_tokenize(t_no_punctuation)
		b_filtered = [w for w in b_tokens if not w in en_stop]
		t_filtered = [w for w in t_tokens if not w in en_stop]
		bodylength=len(b_filtered)
		titlelength=len(t_filtered)
		reputationAtPostCreation=line[4]
		tags=line[8:13]
		status=line[14]
		TagsNo=5
		for t in tags:
			if t == "": 
				TagsNo-=1
		linksCount = len(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line[7]))
		if status == 'open':
			label = 0	
		else:
			label = 1		# test set
		
		output_line = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (label,str(counter),titlelength,bodylength,reputationAtPostCreation,dayDiffQues,TagsNo,userAge,OwnerUndelAnsCountAtPostTime,linksCount) 	

		o.write( output_line )
	counter+=1
