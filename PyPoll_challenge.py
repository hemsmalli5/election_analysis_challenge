# Add dependencies

import csv
import os

# Add varialble from load from path
file_to_load = os.path.join("Resources", "election_results.csv")

#test file retrieval
#print(file_to_load)

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total votes
total_votes = 0

# create a list of Candidate options and a dictionary of candidate votes
candidate_options = []
candidate_votes = {}

# Find county (county_option) with county votes 
county_names = []
county_votes = {}

# Track vote count and percentage for winning candidate 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Track the largest county voter and percentage
largest_county_turnout = ""
largest_county_votes = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    print(reader)

    # read headers from file
    header = next(reader)
    
    # loop each row in csv file
    for row in reader:

        # Add total vote count
        total_votes = total_votes + 1

        # Get candidate name from each row
        candidate_name = row[2]

        # Get county name from each row
        county_name = row[1]

        # extract data if candidate doesn't match 
        # add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #track new candidate voter count
            candidate_votes[candidate_name] = 0

        # add vote count to the candidate 
        candidate_votes[candidate_name] += 1

        # if county name is not in the list, add it
        if county_name not in county_names:
            county_names.append(county_name)

            #track county votes
            county_votes[county_name] = 0

        #add county votes 
        county_votes[county_name] += 1

#print(candidate_options)
#print(candidate_votes)
#print(county_votes)

# Save the results into text file
with open(file_to_save, "w") as txt_file:

    #print vote count 
    election_results = (
        f"\nElection Results\n"
        f"--------------------"
        f"\nTotal Votes: {total_votes:,}\n"
        f"---------------------"
        f"\nCounty Votes:\n"
    )
    print(election_results, end="")
    txt_file.write(election_results)

    #save final county votes
    for county in county_votes:

        #retrive vote count and percentage
        county_vote = county_votes[county]
        county_percent = int(county_vote)/int(total_votes)*100

        county_recults = (
            f"{county}:{county_percent:.1f}% ({county_vote:,})\n"
        )
        print(county_recults, end="")
        txt_file.write(county_recults)

        #determine the winner
        if (county_vote > largest_county_votes):
            largest_county_votes = county_vote
            largest_county_turnout = county
        
    #print county with the largets turnout
    largest_county_turnout = (
        f"\n----------------\n"
        f"Largest County Turnout {largest_county_turnout}\n"
        f"\n-----------------\n"

    )
    print(largest_county_turnout)
    txt_file.write(largest_county_turnout)

    #Save the final candidate vote count to text file
    for candidate in candidate_votes:

        #retriev vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = int(votes)/ int(total_votes) * 100
        
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    
    winning_candidate_summary = (
        f"\n-------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"--------------------\n"

    )
    print(winning_candidate_summary)

    #save winning candidat name to text file
    txt_file.write(winning_candidate_summary)


        








