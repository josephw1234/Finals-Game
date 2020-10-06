# Joseph Woodward
# Cs 30 Q1 P1
# September 28 2020
# Dictionaries for items, characters and locations in game

# Dictionary of items
items_info = {
  "Pencil": {"description": "A pencil usefull for writing essays",
             "helps with": "English"
             },
  "Calculator": {"description": "A scientific calculator for"
                 "all you math needs",
                 "helps with": "Math"
                 },
  "Textbook": {"description": "A history textbook",
               "helps with": "History"
               },
  "French-English dictionary": {"description": "Like"
                                "Google translate in book form",
                                "helps with": "French"
                                }
}

# Dictionary of locations
locations = {
  "Math class": {"teacher": "Mr.Belle"
                 },
  "French class": {"teacher": "Mr.Potvin"
                   },
  "Science class": {"teacher": "Mme.Sexon"
                    },
  "English class": {"teacher": "Mrs.Repski"
                    }
}

# Dictionary of characters
characters = {"Mr.Belle": "math teacher",
              "Mr.Potvin": "french teacher",
              "Mme.Sexon": "science teacher",
              "Mrs.Repski": "english teacher"
}

# Descriptions for items
for item, info in items_info.items():
    print(f"\nItem name: {item}")
    print(f"\tDescription: {info['description']}")
    print(f"\tHelps with: {info['helps with']}")

# Descriptions for locations
for place, person in locations.items():
    print(f"\nClass: {place}")
    print(f"\tTeacher: {person['teacher']}")

# Descriptions for characters
for character, info in characters.items():
    print(f"\n{character} is the {info}")
