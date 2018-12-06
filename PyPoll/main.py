import csv
import operator
filename="C:/DataAnalytics/election_data.csv"
Candidate_votes={}
election_results=[]

election_results.append("Election Results")
election_results.append("---------------------------------------")
# Open file and read 
with open(filename,newline="",mode="r",) as csvfile:
	#Get total number of votes
	lines =len(csvfile.readlines())-1
	election_results.append(f"Total Votes :{lines}")
	election_results.append("---------------------------------------")
	csvfile.seek(0,0)
	# read file using Dictreader
	reader = csv.DictReader(csvfile, delimiter=",")

# Count votes for each candidate
	for row in reader:

		if (row["Candidate"]) not in Candidate_votes:
			Candidate_votes[row["Candidate"]] = 1
		else:
			
			Candidate_votes[row["Candidate"]] += 1

# Store Candidate votes and percentage in a dictionary
	for k,v in Candidate_votes.items() :
		Candidate_votes[k]=[v,round (((v/lines)* 100),2)]
# Sort the results by votes
sorted_x =  sorted(Candidate_votes.items(),key=operator.itemgetter(1),reverse=True)
#Gather the output in the list to print to terminal and send to output file
for i in range(len(sorted_x)):
      election_results.append(f"{sorted_x[i][0]} : {str(sorted_x[i][1][1])} % ({str(sorted_x[i][1][0])})")
election_results.append("--------------------------------------")
election_results.append(f"Winner is : {sorted_x[0][0]}")
election_results.append("---------------------------------------")
#Print to termina
for i in range(len(election_results)) :
	print(election_results[i])
#Print to output file
output_file = "C:/DataAnalytics/pypoll.txt"

with open(output_file,"w") as datafile:
	for i in range(len(election_results)):
		datafile.write(election_results[i]) 
		datafile.write("\r\n") 