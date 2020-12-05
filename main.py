import random

names = str(input("Player names? (Separate with ',' Example: Joe, Bob, Doug, Jeffy, Cool kid, Rick Astley)\n>>> "))

#amount = len(names) < To allow for more than 6 players
name = names.split(",")

# Right now it'll only support 6 people, I'll add mode later
# also only prints in console, might add emails or discord message or something
mafiar = random.randint(1,6)
mafia = [name[mafiar]]

docr = random.randint(1,6)
while docr == mafiar:
    docr = random.randint(1,6)

doc = [name[docr]]

mafia_and_doctor = mafia + doc

playerr = random.randint(1,6)
while playerr == mafiar or playerr == docr: # keep remaking to prevent doubles
    playerr = random.randint(1,6)

pt = []
for i in name:
    player = i
    pt.append(player)

for i in pt:
    if i in mafia_and_doctor: # Removing doubles
        pt.remove(i)

print("=== Mafia ===")
print(mafia)
print("=== Doctor ===")
print(doc)
print("=== Player ===")
print(pt)

# This was like a 20 minute project, so it's not perfect ofc