print("You are going to take your first dance classes.")
print("You choose:\n1. Salsa\n2. Bachata\n3. Zouk\n4. Kizomba")
dance = input("> ")

if dance == "1":
    print("You are get it hard to hear to the music but it seems to be easy. WHat you do next:\n1. Buy salsa shoes.\n2. Buy a new jacket.")
    salsa = input("> ")
    
    if salsa == "1":
        print("Sorry for you.")
    elif salsa == "2":
        print("You get sweaty and you dance new salsa jacket moves but at least you have a neat jacket.")
    else:
        print("Nor jacket or shoes? :<")
elif dance == "2":
    print("Hope you will manage to dance to such music and do not damage any girl while leading.")
elif dance == "3":
    motivation = input("Do you really like it are you motivated to learn it?\n> ")
    if motivation == "yes" or motivation == "Yes":
        print("Respect")
    else:
        print("You know it's not an easy dance...")
elif dance == "4":
    print("Well at least you will hug some girls ;p")
else:
    print("blasdafisgns snfgsif hhee")

fatum = int(input("Choose a number from 1 to 10.\n> "))
if fatum in range(1, 10):
    print("Was is a good choice?\nYou never nooo...")
else:
    print("Good, better stay and observe.")

