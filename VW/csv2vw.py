'convert from CSV to txt format'

import sys, csv, re

def get_label( status ):
	statuses = ['not a real question', 'not constructive', 'off topic', 'open', 'too localized']
	label = statuses.index( status ) + 1
	return label

input_file = sys.argv[1]
output_file = sys.argv[2]

reader = csv.reader( open( input_file ))
o = open( output_file, 'wb' )

counter = 0	
for line in reader:

	counter += 1

	post_id = line[0]
	status = line[14]
	reputation = line[2]
	good_posts = line[3]
	words = line[4]
	tags = line[5:10]
	tags = " ".join( tags ).strip()
	
	body = line[10]
	
	if status == 'open':
		label = 1	
	else:
		label = 0		# test set
		
	output_line = "%s,%s,%s,%s,%s,%s,%s,%s" % ( label, 1, post_id,reputation,good_posts,words,tags,body ) 	# weight is 1
	output_line += "\n"

	o.write( output_line )

	if counter % 100000 == 0:
		print counter