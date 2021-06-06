#The Data we need to retrieve.
#1. Total Number of votes Cast
#2. a complete list of candidates who received votes
#3. total number of votes each candidate received
#4. percentage of votes each  candidate won
#5. the winner of the election based on popular vote

#Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now=datetime.datetime.now()
#Print the present time.
print("The time right now is ", now)

#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load=os.path.join("Resources", "election_results.csv")
#create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and rad the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader=csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

