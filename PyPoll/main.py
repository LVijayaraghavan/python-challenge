import csv
import operator
filename="C:/DataAnalytics/election_data.csv"
Candidate_list=[]
Candidate_votes={}
Candidate_percentage={}
election_results=[]

election_results.append("Election Results")
election_results.append("---------------------------------------")
with open(filename,newline="",mode="r",) as csvfile:
	lines =len(csvfile.readlines())-1
	election_results.append(f"Total Votes :{lines}")
	election_results.append("---------------------------------------")
	csvfile.seek(0,0)
	reader = csv.DictReader(csvfile, delimiter=",")

	for row in reader:

		if (row["Candidate"]) not in Candidate_list:
			Candidate_list.append(row["Candidate"])
			Candidate_votes[row["Candidate"]] = 1
		else:
			
			Candidate_votes[row["Candidate"]] += 1

	

for Candidate  in Candidate_list:
	Candidate_percentage[Candidate] =round((Candidate_votes.get(Candidate)/lines)* 100,2)

sorted_x =  sorted(Candidate_votes.items(),key=operator.itemgetter(1),reverse=True)
sorted_x_percentage = sorted(Candidate_percentage.items(),key=operator.itemgetter(1), reverse=True)

for i in range(len(sorted_x)):
      election_results.append(f"{sorted_x[i][0]} : {str(sorted_x_percentage[i][1])} % ({str(sorted_x[i][1])})")
election_results.append("--------------------------------------")
election_results.append(f"Winner is : {sorted_x[0][0]}")
election_results.append("---------------------------------------")

for i in range(len(election_results)) :
	print(election_results[i])

output_file = "C:/DataAnalytics/pypoll.txt"

with open(output_file,"w") as datafile:
	for i in range(len(election_results)):
		datafile.write(election_results[i]) 
		datafile.write("\r\n") 