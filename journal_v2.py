import random, os

# step 1: Need to read the lines
# step 2: Need to figure how many lines of text are in files & assign to var
# step 3: Pick a random number from the lines variables
# step 4: Out print the var to terminal

# Step 1 & 2, reading the files and finding how many lines are in the text file
with open(r'noun.txt', 'r') as fileNoun:
    for count, line in enumerate(fileNoun):
        nounNum = count

with open(r'city_names.txt', 'r') as fileCity:
    for count, line in enumerate(fileCity):
        cityNum = count
        

with open(r'people.txt', encoding="ISO-8859-1") as filePeople:
    for count, line in enumerate(filePeople):
        peopleNum = count
        

with open(r'verb.txt', 'r') as fileVerb:
    for count, line in enumerate(fileVerb):
        verbNum = count

# step 3, Picking a random number
nounINT = int(random.randrange(0, nounNum))
cityINT = int(random.randrange(0, cityNum))
peopleINT = int(random.randrange(0, peopleNum))
verbINT = int(random.randrange(0, verbNum))


with open("noun.txt", 'r') as nounFile:
	noun = nounFile.readlines()
	
	
with open("city_names.txt", 'r') as cityFile:
	city = cityFile.readlines()
	

with open("people.txt", encoding="ISO-8859-1") as peopleFile:
	people = peopleFile.readlines()
	
	
with open("verb.txt", 'r') as verbFile:
	verb = verbFile.readlines()

# step 4, print out to terminal  
print("Journal Idea Generator")
print("\n\n")
print("Noun: " + str(noun[nounINT]))
print("City: " + str(city[cityINT]))
print("Person: " + str(people[peopleINT]))
print("Verb: " + str(verb[verbINT]))





