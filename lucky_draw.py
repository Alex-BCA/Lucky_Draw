import random
print("**Lucky Draw**")
participants=[]
winners=[]
while True:
    print("1.Add participant")
    print("2.View participants")
    print("3.Draw winner")
    print("4.Draw multiple winners")
    print("5.Remove winner after draw")
    print("6.View winners")
    print("7.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        print("Add participants:")
        participant=input("Enter participant name:")
        participants.append(participant)
    elif choice=="2":
        print("View participants:")
        print(participants)
    elif choice=="3":
        print("Draw winner:")
        if len(participants)==0:
            print("No participants available!")
        else:
            winner=random.choice(participants)
            winners.append(winner)
            print("The winner is:",winner)
    elif choice=="4":
        print("Draw Multiple Winners:")
        if len(participants)==0:
            print("No participants avaolable!")
        else:
            winner=random.sample(participants,3)
            winners.extend(winner)
            print("The winners is:",winner)
    elif choice=="5":
        print("Remove winners after draw:")
        if len(winners)>0:
            participants.remove(winners[-1])
            print("Winners removed from participants!")
        else:
            print("No winners available!")
    elif choice=="6":
        print("View winners:")
        if len(winners)==0:
            print("No winners available!")
        else:
            print("Winners is",winners)
    elif choice=="7":
        break
    else:
        print("In-valid syntax!")
