
#import native Python libraries
import threading
import _thread
import time
from random import randint

while True: #Main Program
    
    #Assigning Local Variables
    space=" "*9
    num="1234567890"
    line="\n"+"_"*63
    wloop1=0
    quit=False
    bsflist=[]
    alrship=[]
    bsmap=[]
    for i in range(1200):
        bsmap.append("#")
    
    #Single Player Variables
    att=0
    desship=0
    boom=15
    endships=[]
    endloc=[]

    #Two Player Variables
    att1=0
    att2=0
    desship1=0
    desship2=0
    boom1=15
    boom2=15
    turn=2
    endships1=[]
    endships2=[]
    endloc1=[]
    endloc2=[]

    #Defining Functions
    
    def elapsedtime(): #To determine duration of game.
        global elapsed
        elapsed=int(time.time()-start_time)

    def tablen(): #To determine number of tabs to print in boomsleft2().
        if namelen>10:
            if namelen>14:
                if namelen>18:
                    if namelen<=23:
                        tab="\t"
                    else:
                        tab=""
                else:
                    tab="\t     "
            else:
                tab="\t\t"
        else:
            tab="\t\t\t"
        return tab

    def boomsleft(): #To print how many booms are left for Single Player Game Mode.
        print(line)
        print("\n\t\t\t",boom,"booms left\n")

    def boomsleft2(): #To print how many booms are left for Two Players Game Mode.
        print(line)
        print("\n",player1,":",boom1,"booms left"+tab,player2,":",boom2,"booms left","\n")

    def printmap(): #To print battleship map.
        print("   ",space,"1",space,"2",space,"3",space,"4",space,"5",space,"6\n",sep="",end="")
        print("  ",num*6,"\n",end="")
        a=0
        i=1
        print(" "+str(i)+" ",sep="",end="")
        i+=1
        for j in bsmap:
            if a==60:
                a=0
                if i <10:
                    print("\n",str(i),j,end="")
                else:
                    print("\n"+str(i),j,end="")
                i+=1
            elif a<60:
                print(j,end="")
            a+=1
        print()

    def userGuess(): #To prompt player's choice of location to boom.
        while True: #To validate the coordinates entered by player.
            try:
                row, col=map(int,input("\nEnter location to boom (row, col) [eg. 20 60]: ").split())
                if row<=0 or row>20 or col<=0 or col>60:
                    print("\nYou have entered an invalid location, please enter again.")
                else:
                    break
            except ValueError:
                print("\nYou have entered an invalid input, please enter (row, col) to boom.")
        guess=(((row-1)*60)+col-1)
        return guess

    def victory(): #To execute when a single player game is won.
        global totalscore
        boomsleft()
        printmap()
        print("\nCongrats! You've destroyed 5 ships.")
        print("\nTotal attempts:",att, "\n")
        if att>9:
            if att>12:
                print('You are a novice!')
            else:
                print('Not too bad!')
        else:
            print('You have the talent!')
        bestscore=10000 #Best Score Possible to get
        score=bestscore*(0.9**(att-5))
        besttscore=5000 #Best Time Score Possible to get
        tscore=besttscore*(0.9**elapsed)
        totalscore=int(score+tscore) #Player's Final Score
        print("\nYour total score is: ",totalscore)

    def victory2(): #To execute when a two players game is won.
        boomsleft2()
        printmap()
        #The winner is assigned as playerw
        print("\n",playerw,"has won!") 
        print("\nCongrats!",playerw,"has destroyed 5 ships first!")
        print("\nTotal attempts by",playerw,":",attw,"\n")
        if att1>9:
            if att1>12:
                print(playerw,"is a novice!")
            else:
                print(playerw,"is not too bad!")
        else:
            print(playerw,"has the talent!")

    def victory3(): #To execute when a time limit game is won.
        printmap()
        print("\nCongrats! You've destroyed 5 ships in",elapsed,"seconds!")
        print("You have",60-elapsed,"seconds left!")
        if elapsed>20:
            if elapsed>40:
                print("You are a novice!")
            else:
                print("Not too bad!")
        else:
            print("You have the talent!")

    def endTA(): #To execute when a time attack game ends.
        printmap()
        print("\nCongrats! You've destroyed",desship,"ships in",totalTime,"seconds!")
        #Different game difficulties' ending messages
        if gdiff==1:
            if desship<60:
                if  desship<20:
                    print("You are a novice!")
                else:
                    print("Not too bad!")
            else:
                print("You have the talent!")
        elif gdiff==2:
            if desship<34:
                if desship<17:
                    print("You are a novice!")
                else:
                    print("Not too bad!")
            else:
                print("You have the talent!")
        else:
            if desship<14:
                if desship<7:
                    print("You are a novice!")
                else:
                    print("Not too bad!")
            else:
                print("You have the talent!")
                    
    def showships(): #To unmask all the battleships.
        s=0
        for z in range(len(bsmap)):
            for p in alrship:
                if s==p and bsmap[s]=="#":
                    bsmap[s]="O"
            s+=1

    def savescore(): #To save the high scores of single player game.
        namelist=[]
        scorelist=[]
        f=open('savefile.txt', 'r')
        contents = f.readlines()
        f.close
        for i in contents:
            item=i.split("\t")
            name=item[0]
            score=int(item[1].strip("\n"))
            namelist.append(name)
            scorelist.append(score)
        for x in scorelist:
            if totalscore>x:
                contents.insert(scorelist.index(x), playerName+Diff+"\t"+str(totalscore)+"\n")
                break
            else:
                pass
        f=open("savefile.txt","w")
        if len(contents)>=11: #To ensure there are only 10 highest scores.
            del contents[10]
        for i in contents:
            f.write(i)
        f.close

    def scoreboard(): #To print the high score board.
        namelist=[]
        scorelist=[]
        f=open('savefile.txt', 'r')
        contents = f.readlines()
        for i in contents:
            item=i.split("\t")
            name=item[0]
            score=int(item[1].strip("\n"))
            namelist.append(name)
            scorelist.append(score)
        print("\n(B)= Beginner, (I)= Intermediate, (A)= Advance")
        print("   Name\t\t\tScores")
        for i in range(len(namelist)):
            if i<9:
                print (i+1,". ",namelist[i],"\t\t",scorelist[i],sep="")
            else:
                print(i+1,".",namelist[i],"\t\t",scorelist[i],sep="")
        f.close

    #Game Start

    print ("\nWelcome to the Battleship Game!") #Welcome Message

    while True: #Main Menu
        while True: 
            try:
                print("\n<--MAIN MENU-->")
                print("\n1. New Game\n2. Extra Game Modes\n3. High Scores\n4. Exit Game\n")
                mode=int(input(""))
                break
            except ValueError:
                print("\nYou have entered an invalid input, please enter a valid number.")
        if mode==1: #New Game
            break
        elif mode==2: #Extra Game Modes
            while True: #Choose Extra Game Modes
                while True:
                    try:
                        print("\n1. Two Player Game Mode\n2. Timer Game Mode\n3. Time Attack Game Mode\n")
                        exmode=int(input(""))
                        break
                    except ValueError:
                        print("\nYou have entered an invalid input, please enter a valid number.")
                if exmode<1 or exmode>3:
                    print("\nYou have entered an invalid number, please enter again.")
                else:
                    break
            break
        elif mode==3: #High Scores
            scoreboard()
            mainmenu=input("\nEnter any key to go back to the main menu.\n")
        elif mode==4: #Exit Game
            quit=True
            break
        else:
            print("\nYou have entered an invalid number, please enter again.")
    
    if quit==True: #Exit from main program
        print("Thanks for playing, Good Bye.")
        break
    
    while True: #Choose Game Difficulty
        while True:
            try:
                print("\nGame difficulty stages:\n\n~Beginner: 80 ships\n~Intermediate: 50 ships\n~Advance:20 ships\n")
                gdiff=int(input("Enter 1 for Beginner, 2 for Intermediate, and 3 for Advance: "))
                break
            except ValueError:
                print("\nYou have entered an invalid input, please enter a valid number.")
        if gdiff==1: #Beginner
            shipnum=80
            Diff="(B)"
            break
        elif gdiff==2: #Intermediate
            shipnum=50
            Diff="(I)"
            break
        elif gdiff==3: #Advance
            shipnum=20
            Diff="(A)"
            break
        else:
            print("\nYou have entered an invalid number, please enter again.")

    while wloop1<shipnum:#Randomize location of each battleship
        bs=randint(0,1199)
        bsmode=randint(0,1) #0 = Horizontal, 1 = Vertical
        bs2=bs
        bsx=[]
        #To ensure 5 locations of battleships are all within the map.
        if bsmode==0: #Horizontal
            while bs2>=60: 
                bs2-=60
            if bs2==0 or bs2==1:
                a=0
                for b in range(5):
                    bsx.append(bs+a)
                    a+=1
            elif bs2==58 or bs2==59:
                a=0
                for b  in range(5):
                    bsx.append(bs-a)
                    a+=1
            else:
                a=-2
                for b in range(5):
                    bsx.append(bs+a)
                    a+=1
                    
        elif bsmode==1: #Vertical
            if bs<120:
                a=0
                for b in range(5):
                    bsx.append(bs+a),
                    a+=60
            elif bs>1079:
                a=0
                for b in range(5):
                    bsx.append(bs-a)
                    a+=60
            else:
                a=-120
                for b in range(5):
                    bsx.append(bs+a)
                    a+=60

        if len(bsflist)>=1:
            if len(set(alrship)&set(bsx))==0: #To ensure battleships do not overlap.
                bsflist.append(bsx)
                for loc in bsx:
                    alrship.append(loc)
                wloop1+=1
        else:
            bsflist.append(bsx)
            for loc in bsx:
                alrship.append(loc)
            wloop1+=1

    if mode==1: #New Game/Single Player Game Mode
        print("\nStarting a New Game...")
        playerName=input('\nEnter your name: ')
        playerName=playerName[:4] #To shorten player's name so that it fits into the high score board.
        start_time=time.time()

        while att<=15: #Main Game
            if desship>=5: #Game won if 5 ships are destroyed by player.
                boomsleft()
                elapsedtime()
                victory()
                savescore()
                break
            elif att==15: #If 5 ships are not destroyed within 15 attempts.
                break
            else: #Ongoing game
                boomsleft()
                printmap()
                guess=userGuess()
                #To validate if user has already boomed the ship or location.
                if guess in endships:
                    print ("\nYou have already boomed this ship, please enter another location to bomb.")
                elif guess in endloc:
                    print ("\nYou have already boomed this location, please enter another location to bomb.")
                else:
                    guessship=[]
                    for ship in bsflist:
                        if guess in ship: #If a ship is hit
                            print  ("\nYou have hit a ship, unmasking ship now.")
                            boom-=1
                            att+=1
                            desship+=1
                            for coor in ship:
                                guessship.append(coor)
                                endships.append(coor)
                            miss=False
                            #Unmasking boomed ship
                            s=0
                            for z in bsmap:
                                for l in guessship:
                                    if s==l:
                                        bsmap[s] = "O"
                                s+=1
                            break
                        else:
                            miss=True
                    if miss==True: #If player does not hit a ship
                        boom-=1
                        att+=1
                        endloc.append(guess)
                        print ("\nYou missed. Please try again. You have",boom,"booms left.")
                        #Unmasking boomed location
                        s=0
                        for z in bsmap:
                            if s==guess:
                                bsmap[s]= " "
                            s+=1


        if desship<5: #Game lost
            elapsedtime()
            boomsleft()
            printmap()
            print("\nYou've no luck today, try again.")
            if desship==0:
                print("You've not hit a ship in 15 attempts!")
            else:
                print("You've only hit",desship,"ships in 15 attempts.")

        while True: #Option to unmask all the ships
            unmask=input("\nDo you want to unmask all the ships?(Y/N)").lower()
            if unmask=="y":
                showships()
                boomsleft()
                printmap()
                break
            elif unmask=="n":
                break
            else:
                print ("You have entered an invalid input, please enter Y or N.")

    elif mode==2 and exmode==1: #Two Players Game Mode
        print("\nTwo Player game mode chosen\nStarting a Two Player Game...\n")
        player1=input("Enter Player 1 name: ")
        player2=input("Enter Player 2 name: ")
        i1=player1[0]
        i2=player2[0]
        namelen=len(player1)+len(player2)
        tab=tablen()
        print(line)
        #Instructions
        print("\nTwo players will compete on the same map, the player that destroys 5 ships first will win the game.")
        print("If both players used up all their 15 attempts, the player with the most number of ships destroyed wins.\n")
        
        #To mark using 1 and 2 if both players have the same initial.
        if i1==i2:
            i1=1
            i2=2
            print("\nSame initials have been detected.")
            
        print("Ships hit by ",player1," will be marked[",i1,"]",sep="")
        print("Ships hit by ",player2," will be marked[",i2,"]",sep="")

        #Delay for players to read instructions
        print("\nGame will start in 5 seconds.")
        time.sleep(5)

        print("\nGame Start!")
        while att1<=15 or att2<=15: #Main Game
            if att2==att1 and (desship1>=5 or desship2>=5):
                if desship1>desship2:
                    playerw=player1 #Player 1 is assigned as the winner
                    attw=att1
                    victory2()
                    break
                elif desship2>desship1:
                    playerw=player2 #Player 2 is assigned as the winner
                    attw=att2
                    victory2()
                    break
                else: #Both players destroyed 5 ships at the same attempt
                    print("It's a draw!")
                    print("\n",player1," and ",player2," destroyed 5 ships with the same attempts!",sep="")
                    print("\nTotal attempts by each player: ",att2,"\n")
                    if att2>9:
                        if att2>12:
                            print("Both of you are novices!")
                        else:
                            print("Both of you are not too bad!")
                    else:
                        print("Both of you have the talent!")
                    break
            elif att1==15 and att2==15: #If none of the players destroyed 5 ships within 15 attempts
                break
            else: #Ongoing game
                boomsleft2()
                printmap()
                if turn%2==0: #Player 1's Turn
                    print("\nIt is ", player1, "'s turn!",sep="")
                    guess=userGuess()
                    if guess in endships1:
                        print("\nYou have already boomed this ship, please enter another location to boom.")
                    elif guess in endships2:
                        print("\n",player2," has already boomed this ship, please enter another location to boom.",sep="")    
                    elif guess in endloc1:
                        print("\nYou have already boomed this location, please enter another location to boom.")
                    elif guess in endloc2:
                        print("\n",player2," has already boomed this location, please enter another location to bomb.",sep="")
                    else:
                        guessship=[]
                        for ship in bsflist:
                            if guess in ship:
                                print  ("\nYou have hit a ship, unmasking ship now.")
                                boom1-=1##
                                att1+=1
                                desship1+=1
                                for coor in ship:
                                    guessship.append(coor)
                                    endships1.append(coor)
                                miss=False
                                s=0
                                for z in bsmap:
                                    for l in guessship:
                                        if s==l:
                                            bsmap[s]=i1 
                                    s+=1
                                break
                            else:
                                miss=True
                        if miss==True:
                            boom1-=1
                            att1+=1
                            endloc1.append(guess)
                            print("\nYou missed. Please try again. You have",boom1,"booms left.")
                            s=0
                            for z in range(len(bsmap)):
                                if s==guess:
                                    bsmap[s]= " "
                                s+=1
                        turn+=1
                elif turn%2==1: #Player 2's Turn
                    print("\nIt is ", player2, "'s turn!",sep="")
                    guess=userGuess()
                    if guess in endships2:
                        print("\nYou have already boomed this ship, please enter another location to boom.")
                    elif guess in endships1:
                        print("\n",player1," has already boomed this ship, please enter another location to boom.",sep="")    
                    elif guess in endloc2:
                        print("\nYou have already boomed this location, please enter another location to boom.")
                    elif guess in endloc1:
                        print("\n",player1," has already boomed this location, please enter another location to bomb.",sep="")
                    else:
                        guessship=[]
                        for ship in bsflist:
                            if guess in ship:
                                print("\nYou have hit a ship, unmasking ship now.")
                                boom2-=1
                                att2+=1
                                desship2+=1
                                for coor in ship:
                                    guessship.append(coor)
                                    endships2.append(coor)
                                miss=False
                                s=0
                                for z in bsmap:
                                    for l in guessship:
                                        if s==l:
                                            bsmap[s]=i2 
                                    s+=1
                                break
                            else:
                                miss=True
                        if miss==True:
                            boom2-=1
                            att2+=1
                            endloc2.append(guess)
                            print("\nYou missed. Please try again. You have",boom2,"booms left.")
                            s=0
                            for z in bsmap:
                                if s==guess:
                                    bsmap[s]= " "
                                s+=1
                        turn+=1

        if desship1<5 and desship2<5: #Both players exhausted all their booms and neither has hit 5 ships
            print("\nBoth players have used up all attempts and did not hit 5 ships!\n")
            print(player1, "hit", desship1, "ships with total attempts of", att1)
            print(player2, "hit", desship2, "ships with total attempts of", att2,"\n")
            if desship1==0 and desship2==0:
                print("Both of you have not hit a ship within 15 attempts!")
            elif desship1>desship2:
                print(player1,"won by number of ships destroyed!") 
            elif desship2>desship1:
                print(player2,"won by number of ships destroyed!")

        while True: #Option to unmask all the ships
            unmask=input("\nDo you want to unmask all the ships?(Y/N)").lower()
            if unmask=="y":
                showships()
                boomsleft2()
                printmap()
                break
            elif unmask=="n":
                break
            else:
                print ("You have entered an invalid input, please enter Y or N.")

    elif mode==2 and exmode==2:#Timer Game Mode
        print("\nStarting a Timer Game...")
        print(line)
        #Instructions
        print("\nThis is a single player game mode, you have to destroy 5 ships within 60 seconds with no limit on attempts.")
        #Delay for player to read instructions
        print("\nGame will start in 5 seconds.")
        time.sleep(5)
        timer = threading.Timer(60.0 , _thread.interrupt_main) #Countdown to end game after 60 seconds
        timer.start()
        start_time=time.time()
        try:
            print("\nGame Start!\n")
            while True: #Main Game
                if desship>=5: #Game won by destroying 5 ships within 60 seconds
                    elapsedtime()
                    victory3()
                    timer.cancel()
                    break
                else: #Ongoing game
                    printmap()
                    elapsedtime()
                    print("\nYou have",60-elapsed,"seconds left.") #To update player on remaining time
                    guess=userGuess()
                    if guess in endships:
                        print ("\nYou have already boomed this ship, please enter another location to bomb.")
                    elif guess in endloc:
                        print ("\nYou have already boomed this location, please enter another location to bomb.")
                    else:
                        guessship=[]
                        for ship in bsflist:
                            if guess in ship:
                                print  ("\nYou have hit a ship, unmasking ship now.\n")
                                desship+=1
                                for coor in ship:
                                    guessship.append(coor)
                                    endships.append(coor)
                                miss=False
                                s=0
                                for z in bsmap:
                                    for l in guessship:
                                        if s==l:
                                            bsmap[s] = "O"
                                    s+=1
                                break
                            else:
                                miss=True
                        if miss==True:
                            endloc.append(guess)
                            print ("\nYou missed. Please try again.\n")
                            s=0
                            for z in bsmap:
                                if s==guess:
                                    bsmap[s]= " "
                                s+=1

        except KeyboardInterrupt: #Game stopped by countdown timer
            print(line)
            print("\nTime\'s up!")

        if desship<5: #Game lost by not hitting 5 ships within 60 seconds
            elapsed=60
            printmap()
            print("\nYou've no luck today, try again.")
            if desship==0:
                print("You've not hit a ship within the time limit!")
            else:
                print("You've only hit",desship,"ship(s).")

        while True: #Option to unmask all the ships
            unmask=input("\nDo you want to unmask all the ships?(Y/N)").lower()
            if unmask=="y":
                showships()
                printmap()
                break
            elif unmask=="n":
                break
            else:
                print ("You have entered an invalid input, please enter Y or N.")

    elif mode==2 and exmode==3:#Time Attack Game Mode
        totalTime=0
        print("\nStarting a Time Attack Game...")
        print(line)
        #Instructions
        print("\nThis is a single player game mode. You have 10 seconds to destroy a ship.")
        print("10 seconds will refresh each time you hit a ship. The game ends when time runs out.")
        #Delay for player to read the instructions
        print("\nGame will start in 5 seconds.\n")
        time.sleep(5)
        timer = threading.Timer(10.0 , _thread.interrupt_main) #Countdown to end game if player do not hit a ship in 10 seconds
        timer.start()
        start_time=time.time()
        try:
            print("\nGame Start!")
            while True: #Main Game
                printmap()
                elapsedtime()
                print("\nYou have",10-elapsed,"seconds left to hit a ship.") #To update player on remaining time
                guess=userGuess()
                if guess in endships:
                    print ("\nYou have already boomed this ship, please enter another location to bomb.")
                elif guess in endloc:
                    print ("\nYou have already boomed this location, please enter another location to bomb.")
                else:
                    guessship=[]
                    for ship in bsflist:
                        if guess in ship: #If a ship is hit
                            elapsedtime()
                            totalTime+=elapsed
                            timer.cancel() #To stop countdown timer to be reset later on
                            print  ("\nYou have hit a ship, unmasking ship now.\n")
                            desship+=1
                            for coor in ship:
                                guessship.append(coor)
                                endships.append(coor)
                            miss=False
                            s=0
                            for z in bsmap:
                                for l in guessship:
                                    if s==l:
                                        bsmap[s] = "O"
                                s+=1
                            timer = threading.Timer(10.0 , _thread.interrupt_main) #To reset the 10 seconds countdown timer
                            timer.start()
                            start_time=time.time()
                            break
                        else:
                            miss=True
                    if miss==True:
                        endloc.append(guess)
                        print ("\nYou missed. Please try again.\n")
                        s=0
                        for z in bsmap:
                            if s==guess:
                                bsmap[s]= " "
                            s+=1
        except KeyboardInterrupt: #Game stops if player do not hit a ship within 10 seconds
                totalTime+=15
                print(line)
                print("\nTime\'s up!")
                endTA()

        while True: #Option to unmask all the ships
            unmask=input("\nDo you want to unmask all the ships?(Y/N)").lower()
            if unmask=="y":
                showships()
                printmap()
                break
            elif unmask=="n":
                break
            else:
                print ("\nYou have entered an invalid input, please enter Y or N.")
    
    print("\nEnter ""R"" to return to main menu.") #Option to return to main menu
    print("Enter any other value to exit the game.") #Exit the main program by entering any other value
    restart=input("").lower()
    if restart!="r": #End Game, Exits the main program.
        print("Thanks for playing, Good Bye.")
        break
