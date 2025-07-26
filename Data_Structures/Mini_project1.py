"""Create a dictionary that contains a list of people 
and one interesting fact about each of them.
Display each person and his or her interesting fact to the screen. 
Next, change a fact about one of the people. Also add an additional person and corresponding fact.
Display the new list of people and facts. Run the program multiple times and notice if the order changes."""

#code

people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}
for person, fact in people_facts.items():
    print(f"{person}: {fact}")
print()
people_facts["Jeff"] = "Is afraid of heights."

people_facts["Jill"] = "Can hula dance."

for person, fact in people_facts.items():
    print(f"{person}: {fact}")
