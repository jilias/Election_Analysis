#The Data we need to retrieve.
#1. Total Number of votes Cast
#2. a complete list of candidates who received votes
#3. total number of votes each candidate received
#4. percentage of votes each  candidate won
#5. the winner of the election based on popular vote
#6. The voter turnout for each county
#7. The percentage of botes from each county out of the toal count
#8. the county with the highest turnout

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_results.txt")
#Initialize a total vote counter.
total_votes = 0

#Candidate Options and candidate votes
candidate_options = []
#declare dictionary
candidate_votes = {}
#County list and county votes dictionary
county = []
county_votes = {}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Largest County and Country Voter Turnout Tracker
largest_county = ""
county_turnout = 0
county_percentage = 0
#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read the header row.
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes +=1
        # Get the candidate name from each row
        candidate_name = row[2]
        # Get the county name from each row
        county_name = row[1]
        #If the candidate does not match any existing candidate add it to the candidate list
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1
        #If statement for checking county matches
        if county_name not in county:
            #Add or append
            county.append(county_name)
            county_votes[county_name] = 0
            #Track County votes
            county_votes[county_name] +=1
    #Save the results to our text file
    with open(file_to_save, "w") as txt_file:
        election_results = (
                f"\nElection Results\n"
                f"-------------------\n"
                f"Total Votes {total_votes:,}\n"
                f"-------------------\n")
        print(election_results, end="")
        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #Write a loop to get the country dictionary for county_name in county_votes:
        for county_name in county_votes:
            #Retrieve county vote count and percentage
            votes=county_votes[county_name]
            vote_percentage = float(votes)/float(total_votes) *100
            #print county votes
            county_results =(f"{county_name}: {vote_percentage:.1f}% ({votes:,}\n")
        #Print County results
        print(county_results)
        #Save county to txt file


        #Determine Highest turnout county
        largest_county = county_name
        county_turnout = votes
        county_percentage = vote_percentage
        #Print the county with highest
        Highest_county_summary = (
        f"-------------------------\n"
        f"Largest County: {largest_county}\n"
        f"Most votes: {county_turnout:,}\n"
        f"Highest County Percentage: {county_percentage:.1f}%\n"
        f"-------------------------\n")
        print(Highest_county_summary)

        #Save the county into txt file
        txt_file.write(Highest_county_summary)

        for candidate_name in candidate_votes:
            # Retrieve vote count and percentage
            votes=candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            #Print each candidate, their voter count, and percentage to the
            #terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,}\n")
            #Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #Save the candidate results to our text file.
            txt_file.write(candidate_results)
            #Determing winning vote count, wnning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate_name
        #Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
            f"-------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage {winning_percentage:.1f}%\n"
            f"-------------------\n")

        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)
