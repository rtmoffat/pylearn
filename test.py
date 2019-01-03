import csv
csvfile=open ('restaurants.csv','r')
myreader=csv.reader(csvfile,delimiter='\t')
for row in myreader:
	print(row[0])
csvfile.close()