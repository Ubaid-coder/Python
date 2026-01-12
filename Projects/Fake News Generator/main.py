#1 - import the random module
import random

#2- create subjects
subjects = [
    "Elon musk",
    "Bilgates",
    "Mukesh Ambani",
    "Salman Khan",
    "Shahrauk Khan",
    "A group of monkeys",
    "Goats",
    "Messi",
    "Ronaldo",
    "Babar Azam",
    "Virat Kohli",
    "Ubaid",
    "Imran Khan",
    "Modi",
    "Trump"
]

actions = [
"Achieve",
"Analyze",
"Build",
"Communicate",
"Coordinate",
"Create",
"Develop",
"Establish",
"Facilitate",
"Implement",
"Lead",
"Manage",
"Organize",
"Plan",
"Solve",
"Eats",
"Celebrates",
]

places = [
    "India",
    "Pakistan",
    "Plate",
    "Mountain",
    "Cricket Stadium",
    "Space",
    "Cricket Pitch",
    "House",
    "Bathroom"
    
]

#3 start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    
    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)
    
    userInput = input("\nDo you want another headline: ").strip().lower()
    if userInput == 'no':
        break

#print good bye message
print("\nThanks for using the False News Generator. Have a fun day")