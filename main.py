# Joseph Woodward
# CS 30
# Finals game (continuous game play assignment)
# Oct. 10 2020

# Lsits and dicts
knowledge = []
cheats = []
items = {}

# Message functions
# Message for look path
message_1 = ("You look around your room and see your desk and bookshelf\n"
             "Look in one of these or leave? \n>")

# Message for bookshelf path
message_2 = ("You see a French English dictionary and a History textbook,\n"
             "these might help you, take them?\n>")

# Message for desk path
message_3 = ("You see a calculator and a pencil, take them?\n>")

# Message for cheat/study path
subject_message = ("What sublect? (English, Science, Math, Social)\n>")


# Functions for adding items
def add_pencil():
    items['Pencil'] = {"description": "A pencil usefull for writing essays",
                       "helps with": "English"
                       }


def add_calculator():
    items['Calculator'] = {"description": "A scientific calculator for"
                                          " all you math needs",
                           "helps with": "Math"
                           }


def add_dictionary():
    items['Dictionary'] = {"description": "Paperback Google Translate",
                           "helps with": "English"
                           }


def add_textbook():
    items['Textbook'] = {"description": "A history textbook",
                         "helps with": "History"
                         }


# Main function
# Turns left is how many study/cheat actions the player can take
# desk and bookshlef should be set to True
def first_day(turns_left, bookshelf, desk):
    while turns_left > 0:
        message = (f"Cheat, study or look around?\n"
                   f"(You have {turns_left} hours left)\n>")
        for keypress in message:
            keypress = input(message)
            # Study path
            if keypress.lower() == "study":
                subject = input(subject_message)
                if subject.lower() in knowledge:
                    print(f"You've already studied for {subject}")
                    continue
                if subject.lower() == "english" or \
                   subject.lower() == "science"\
                   or subject.lower() == "social" or subject.lower() == "math":
                        turns_left -= 1
                        knowledge.append(subject)
                        print(f"You studied for {subject}")
                        break
                else:
                    print("That isn't a subject")
                    continue
            # Cheat path
            if keypress.lower() == "cheat":
                subject = input(subject_message)
                if subject.lower() in cheats:
                    print(f"You've already cheated on {subject}")
                    break
                if subject.lower() == "english" or \
                   subject.lower() == "science"\
                   or subject.lower() == "social" or subject.lower() == "math":
                        cheats.append(subject)
                        turns_left -= 1
                        print(f"You cheated for {subject}")
                        break
                else:
                    print("That isn't a subject")
                    continue
            # Look path
            if keypress.lower() == "look":
                active = True
                while active == True:
                    action = input(message_1)
                    if action == "look":
                        choice = input("Desk or bookshelf\n>")
                        # Bookshelf path
                        if choice.lower() == "bookshelf" and \
                           bookshelf == True:
                            item = input(message_2)
                            if item.lower() == "yes":
                                add_dictionary()
                                add_textbook()
                                bookshelf = False
                                continue
                            if item.lower() == "no":
                                continue
                        if choice.lower() == "bookshelf" and \
                           bookshelf == False:
                            print("You've already looked in there")
                            continue
                        # Desk path
                        if choice.lower() == "desk" and \
                           desk == True:
                            item = input(message_3)
                            if item.lower() == "yes":
                                add_pencil()
                                add_calculator()
                                desk = False
                                continue
                            if item.lower() == "no":
                                continue
                        if choice.lower() == "desk" and \
                           desk == False:
                            print("You've already looked there")
                    # Leave path
                    if action.lower() == "leave":
                        active = False
                        break
                continue
            # Inventory check path
            if keypress.lower() == "inventory":
                for item, desc in items.items():
                    print(f"Item: {item}")
                    print(f"\tDescription: {desc['description']}")
                    print(f"\tHelps with: {desc['helps with']}")
                    print()
                continue
            # Done path
            if keypress.lower() == "done":
                turns_left = 0
                break
            # Unknown input
            else:
                print("I don't know what you mean")
                continue


print("Type 'done' to skip the rest of your turns")
print("Type 'inventory' to check inventory")
print()
first_day(4, True, True)
