'''
1 for snake 
-1 for water
0 for gun
'''
import random
j=-1
yourscore=0
computerscore=0
while(j==-1):
    computer=random.choice([-1, 0, 1])
    youstr=input("Enter your choice ")
    youdict={
        "s":1,
        "w":-1,
        "g":0
    }
    reversedict={1: "Snake", -1: "Water", 0: "Gun",}
    you=youdict[youstr]

    print(f"Computer choose: {reversedict[computer]}")
    print(f"You choose: {reversedict[you]}")
    if(computer==you):
        print("draw")
    else:
        if(computer ==-1 and you==1):
            print("You win")
            yourscore+=1
        elif(computer ==-1 and you==0):
            print("You loss")
            computerscore+=1
        elif(computer==1 and you==-1):
            print("You loss")
            computerscore+=1

        elif(computer==1 and you==0):
            print("You win")
            yourscore+=1
        elif(computer==0 and you==1):
            print("YOu loss")
            computerscore+=1

        elif(computer==0 and you==-1):
            print("You win")
            yourscore+=1
        else:
            print("Something went wrong")
            
    press=int(input("Press 1 to exit and 2 to continue"))
    if(press==1):
        if(yourscore>computerscore):
            print(f"You win the game,\nYour score= {yourscore}\nComputer score= {computerscore}")
        elif(computerscore>yourscore):
            print(f"You lose the game,\nYour score= {yourscore}\nComputer score= {computerscore} ")
        elif(yourscore==computerscore):
            print("Game draw,\nYour score= {yourscore}\nComputer score= {computerscore}")
        exit(0)
    elif(press==2):
        continue