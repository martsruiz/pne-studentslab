import json
import termcolor
from pathlib import Path

# Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)

# Iterate over each person
for person in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\tType: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\tNumber: ", 'red', end='')
        print(dictnum['number'])
