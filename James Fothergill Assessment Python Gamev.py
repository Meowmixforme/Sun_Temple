# Python Assessment game Sun Temple
# James Fothergill 09/11/2018

import random

# basic initialise vars #
along = 5
down = 8
line="|"
dots="---"
cells = "."*3
numberofplayers = 2
playerno = 1
track = []
gamrun = True
playerlist = []
nowpossition = 0
nextpossition = 0
chitlist = [0,1,2,3,4,5,6,1,2,3,4,5,6]
thismove = -1
tally = [0,0]
goodysack = [[],[]]
 

# functions #

def rulelist():
    print(""" SUN TEMPLE \n \n Here are the rules...\n \n This is a two player game in which players must traverse the board of 40 spaces
 Starting at the first space players will alternate turns and using a single counter \n Players can use any move in the available set \n The board is seeded randomly with gems and glass beads \n
 There are 7 of each:\n Rubies \n Emeralds \n Diamonds \n Sapphires \n and 11 Glass beads \n Gems will sum as Gem type / 2 * (Gem type + 1) and Glass beads will be -1 \n
 The game ends when the player counter leaves the board. \n \n Available moves are: 0,1,2,3,4,5,6,1,2,3,4,5,6 \n \n
 Game On....\n \n""")

def getplayers(num):
    playerlist = []
    playerlist.append(input("Enter your name Player1: "))
    playerlist.append(input("Enter your name Player2: "))
    return playerlist

    
def whatisboardarray(track):
    stones = "rrrrrrreeeeeeedddddddsssssssggggggggggg"
    for i in range(len(stones)):
        track.append(stones[i])
    random.shuffle(track)
    track.insert(0,"X")
    print(track)
    return track

def gameboard(board, nalong, ndown):
 for row in range(along):
    outline = ""
    inside = ""
    for col in range(down):
        outline = outline + line + dots
        cells = row * down + col
        inside = inside + line + " " + track[cells] + " "
    outline += line
    inside += line
    print(outline)
    print(inside)
 print(outline)
    

def activemove(playerlist):
    flag = False
    while not flag:
        if playerno == 1:
            entry = input(playerlist[1] + " Please choose a number from the available move list displayed: ")
            try:
                thismove = int(entry)
                flag = playermovevalid(thismove)
            except:
                print("Invalid entry - Please choose a move from: ", chitlist)
        else:
            entry = input(playerlist[0] + " Please choose a number from the available move list displayed: ")
            try:
                thismove = int(entry)
                flag = playermovevalid(thismove)
            except:
                print("Invalid entry - Please choose a move from: ", chitlist)           

    return thismove

def playermovevalid(thismove):
    
    if thismove in chitlist:
        chitlist .remove(thismove)
        print(chitlist)
        return True
    else:
        print("This is not a valid move. Please choose a move from: ", chitlist)
        return False

def updatevariables(nowpossition, goodysack):
    
    nextpossition = min(nowpossition + activeplayermove,len(track)-1)
    track[nowpossition] = " "
    nowpossition += 1
    print("updatevariables(): ", activeplayermove, nowpossition, nextpossition)
    while nowpossition <= nextpossition:    
        
        goodysack[playerno].append(track[nowpossition])
        
        track[nowpossition] = " "
        nowpossition += 1
    track[nextpossition] = "*"
    print(goodysack)
    
   

    return " updated"


    
def gameover(nowpossition):
    if nowpossition >= 39:
        return False
    else:
        return True
    

def finalscores(goodysack, tally):
    print(goodysack)
    print("\nGame Over")
    print("The winner is...")
    for i in range(2):
        rubies = goodysack[i].count("r")
        emeralds = goodysack[i].count("e")
        diamonds = goodysack[i].count("d")
        sapphires = goodysack[i].count("s")
        glassbeads = goodysack[i].count("g")
        rubies = rubies / 2 * (rubies + 1)
        emeralds = emeralds / 2 * (emeralds + 1)
        diamonds = diamonds / 2 * (diamonds + 1)
        sapphires = sapphires / 2 * (sapphires +1)
        glassbeads = glassbeads / 2 * (glassbeads + 1)
        tally[i] += rubies + emeralds + diamonds + sapphires - glassbeads
    print(tally)
    
    if tally[0] == tally[1]:
        print("Draw")
    if tally[0] > tally[1]:
        print(playerlist[0],"Wins")
    else: print(playerlist[1],"Wins")
    
# main program #
rulelist()
playerlist = getplayers(numberofplayers)
track = whatisboardarray(track)
gameboard(track, along, down)
print("Let us play...")



gamrun = True
while gamrun:
        
        # determine active player
        playerno = (playerno + 1) % numberofplayers
        print("\nIt is ", playerlist[playerno] + "'s turn")
        print("-" * 20)

        # now get a valid player move
        activeplayermove = activemove(playerlist)
        print("You chose to move", activeplayermove, "Spaces")

        
        nextpossition = nowpossition + activeplayermove

        
        
        

        variables = updatevariables(nowpossition, goodysack)
        print(variables)

        
        gameboard(track, along, down)

        print("Player Gems are: ","\n" ,playerlist[0],goodysack[0], "\n" ,playerlist[1],goodysack[1])        


        nowpossition = nextpossition

        
      
  
        gamrun = gameover(nowpossition)
    
    
        
finalscores(goodysack,tally)
    

    

    


