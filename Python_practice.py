print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")



#Counties
counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El paso is not the list of counties")
if "Arapahoe" in counties and "El Paso" in counties: 
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties")


#for loop
for county in counties:
    print(county)


#Range
numbers=[0, 1, 2 , 3, 4]
for num in numbers:
    print(num)

#Range with For Loop
for num in range(5):    
    print(num)

for i in range(len(counties)):
    print(counties[i])



#Dictionary
counties_dict={"Arapahoe": 422829, "Denver":463353, "Jefferson":432438}
for county in counties_dict:
    print(county)

voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])  

for county in counties_dict:
    print(counties_dict.get(county))

#Key-Value Pairs of a dictionary
for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters":463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data)):
    print(voting_data[county]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict['registered_voters'])
for county_dict in voting_data:
    print(county_dict['county'])


#F-Strings: Formatted String Literals
my_votes=int(input("How many votes did you get in the election?"))
total_votes=int(input("What is the total votes in the election"))
print(f"I received {my_votes/total_votes*100}% of the total votes.")

counties_dict={"Arapahoe": 369237, "Denver": 413229, "Jefferson":390222}
for county, voters in counties_dict.items():
    print(county+"county has"+str(voters)+"registered voters.")
#versus f string version of above
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


#Multiline F-Strings
candidate_votes=int(input("how many votes did  the candidate get in the election?"))
total_votes=int(input("What is the total number of votes in the election?"))
message_to_candidate=(
    f"You received{candidate_votes} number of votes."
    f"the total number of votes in the election was {total_votes}."
    f"you received {candidate_votes/total_votes * 100}% of the total votes.")

print(message_to_candidate)

#format floating-point decimals
#f'{value:{width}.{precision}}'

