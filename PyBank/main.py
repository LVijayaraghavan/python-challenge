import csv
import operator
filename="C:/DataAnalytics/Assignments/budget_data.csv"
total=0
linecnt=0
prof={}
total_line=0
diffvalue=0
populate_output=[]
maxpair=[]
minpair=[]
minpair_yr=[]
maxpair_yr=[]


with open(filename,newline="",mode="r",) as csvfile:
	#Get the Total count of lines in the File including the header
	rowcnt=sum(1 for row in csvfile)
	# No of Data line in the file exluding header
	total_line=rowcnt-1
	populate_output.append("Financial Analysis") 
	populate_output.append("----------------------------")
	populate_output.append("Total months =" + str(total_line))
	
	csvfile.seek(0,0)
	reader = csv.DictReader(csvfile, delimiter=",")
	
	for row in reader :
		# Get the opening profit in the first month and get the total
		 if (linecnt==0):
		 	openingbal=int(row['Profit/Losses'])
		 	diffvalue = int(row['Profit/Losses'])
		 	linecnt += 1
		 	total= total+int(row['Profit/Losses'])
		 else:
		 	#store the difference in profit/loss between 2 successive months in a dictinary with the date to get the Greatest increase in profits and decrease in profits
		 	linecnt += 1
		 	#print(linecnt)
		 	total=total+int(row['Profit/Losses'])
		 	prof[row['Date']]=int(row['Profit/Losses']) - diffvalue
		 	diffvalue=int(row['Profit/Losses'])
		 	#if last record get the  last profit and loss  . That divided by (number of months-1) will give the average change
		 	if (linecnt==total_line):
		 		closingbal=int(row['Profit/Losses'])
	
	averagechange=round(((closingbal-openingbal)/(total_line-1)),2)
	populate_output.append("Total:"+"$"+ str(total))
	populate_output.append("Average Change : $"+ str(averagechange))
	
	# sort the dictionary by value	
	sorted_x =  sorted(prof.items(),key=operator.itemgetter(1))
	# the 1st item in the list gives the least profit and the last item in the list gives the gre

	minpair=list((sorted_x[0]))
	minpair_yr=minpair[0].split("-")
	
	maxpair=list((sorted_x[(len(sorted_x)-1)]))
	maxpair_yr=maxpair[0].split("-")
	populate_output.append(f"Greatest Increase in Profits:  {maxpair_yr[0]}-20{maxpair_yr[1]}  ($  {str(maxpair[1])} )" )
	populate_output.append(f"Greatest Decrease in Profits:  {minpair_yr[0]}-20{minpair_yr[1]}  ($  {str(minpair[1])})")
	for i in range(len(populate_output)):
		print(populate_output[i])
		#print("\r\n")

output_file = "C:/DataAnalytics/pybank.txt"

with open(output_file,"w") as datafile:

	#writer=csv.writer(datafile)
	#writer.writerow(header)
	#writer.writerows(populate_output)
	for i in range(len(populate_output)):
		datafile.write(populate_output[i]) 
		datafile.write("\r\n") 
