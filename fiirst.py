knowledge = []
cheats = []

def first_day(turns_left):
  while turns_left > 0:
    message = (f"Cheat or study?\n(You have {turns_left} turns left)\n>")
    for keypress in message:
      keypress = input(message)
      if keypress.lower() == "study":
        subject = input("What sublect? (English, Science, Math, Social)\n>")
        if subject.lower() in knowledge:
          print(f"You've already studied for {subject}")
          continue
        if subject.lower() == "english" or subject.lower() == "science" or subject.lower() == "social" or subject.lower() == "math":
          turns_left -= 1
          knowledge.append(subject)
          print(f"You studied for {subject}")
          break
        else:
          print("That isn't a subject")
          continue
      if keypress.lower() == "cheat":
        subject = input("What sublect? (English, Science, Math, Social)\n> ")
        if subject.lower() in cheats:
          print(f"You've already cheated on {subject}")
        if subject.lower() == "english" or subject.lower() == "science" or subject.lower() == "social" or subject.lower() == "math":
          cheats.append(subject)
          turns_left -= 1
          print(f"You cheated for {subject}")
          break
        else:
          print("That isn't a subject")
          continue
      if keypress.lower() == "done":
        turns_left = 0
        break
      else:
        print("I don't know what you mean")

