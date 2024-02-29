import sys
#Fatih Oter
#2210356119
#Assignment4
f5 = open("Battleship.out", "w") #This is the writing part
file = open(sys.argv[1], "r") #This is the reading part
player1List = []
for line in file:
    if line.endswith("\n"):
        line = line[:-1]
    data = line.split(";")
    data2 = []
    for i in range(len(data)):
        if data[i] == "":
            data2.append("-")
        else:
            data2.append(data[i])
    player1List.append(data2)

file2 = open(sys.argv[2], "r") #This is the reading part
player2List = []
for line in file2:
    if line.endswith("\n"):
        line = line[:-1]
    data = line.split(";")
    data2 = []
    for i in range(len(data)):
        if data[i] == "":
            data2.append("-")
        else:
            data2.append(data[i])
    player2List.append(data2)

file3 = open(sys.argv[3], "r") #This is the reading part
file4 = open(sys.argv[4], "r") #This is the reading part
player1Moves = file3.readline() #moves of players gets this line
player2Moves = file4.readline() #moves of players gets this line
numberOfCarrierPlayer1 = 1      
numberOfBattlshipPlayer1 = 2   #This part is the counter part
numberOfDestroyerPlayer1 = 1
numberOfSubmarinePlayer1 = 1
numberOfPetrolBoatPlayer1 = 4
numberOfCarrierPlayer2 = 1
numberOfBattlshipPlayer2 = 2
numberOfDestroyerPlayer2 = 1
numberOfSubmarinePlayer2 = 1
numberOfPetrolBoatPlayer2 = 4


def returnLocationOfChar(a):
    if a == 'A':
        return 0
    if a == 'B':
        return 1
    if a == 'C':
        return 2
    if a == 'D':
        return 3
    if a == 'E':
        return 4
    if a == 'F':
        return 5
    if a == 'G':
        return 6
    if a == 'H':
        return 7
    if a == 'I':
        return 8
    if a == 'J':
        return 9
def returnLocationOfInt(a):
    if a == 0:
        return "A"
    if a == 1:
        return "B"
    if a == 2:
        return "C"
    if a == 3:
        return "D"
    if a == 4:
        return "E"
    if a == 5:
        return "F"
    if a == 6:
        return "G"
    if a == 7:
        return "H"
    if a == 8:
        return "I"
    if a == 9:
        return "J"


def sunkShip(playerList, i, j):
    if i < 6:
        if i < 5:
            if playerList[i][j] == "CX" and playerList[i + 1][j] == "CX" and playerList[i + 2][j] == "CX" and \
                    playerList[i + 3][j] == "CX" and playerList[i + 4][j] == "CX" and playerList[i + 5][j] != "CX":
                playerList[i][j] = "CXF"
                playerList[i + 1][j] = "CXF"
                playerList[i + 2][j] = "CXF"
                playerList[i + 3][j] = "CXF"
                playerList[i + 4][j] = "CXF"
                return 1
        else:
            if playerList[i][j] == "CX" and playerList[i + 1][j] == "CX" and playerList[i + 2][j] == "CX" and \
                    playerList[i + 3][j] == "CX" and playerList[i + 4][j] == "CX":
                playerList[i][j] = "CXF"
                playerList[i + 1][j] = "CXF"
                playerList[i + 2][j] = "CXF"
                playerList[i + 3][j] = "CXF"
                playerList[i + 4][j] = "CXF"
                return 1
    if j < 6:
        if j < 5:
            if playerList[i][j] == "CX" and playerList[i][j + 1] == "CX" and playerList[i][j + 2] == "CX" and \
                    playerList[i][j + 3] == "CX" and playerList[i][j + 4] == "CX" and playerList[i][j + 5] != "CX":
                playerList[i][j] = "CXF"
                playerList[i][j + 1] = "CXF"
                playerList[i][j + 2] = "CXF"
                playerList[i][j + 3] = "CXF"
                playerList[i][j + 4] = "CXF"
                return 1
        else:
            if playerList[i][j] == "CX" and playerList[i][j + 1] == "CX" and playerList[i][j + 2] == "CX" and \
                    playerList[i][j + 3] == "CX" and playerList[i][j + 4] == "CX":
                playerList[i][j] = "CXF"
                playerList[i][j + 1] = "CXF"
                playerList[i][j + 2] = "CXF"
                playerList[i][j + 3] = "CXF"
                playerList[i][j + 4] = "CXF"
                return 1
    if j < 7:
        if j < 6:
            if playerList[i][j] == "BX" and playerList[i][j + 1] == "BX" and playerList[i][j + 2] == "BX" and \
                    playerList[i][j + 3] == "BX" and playerList[i][j + 4] != "BX":
                playerList[i][j] = "BXF"
                playerList[i][j + 1] = "BXF"
                playerList[i][j + 2] = "BXF"
                playerList[i][j + 3] = "BXF"
                return 2
        else:
            if playerList[i][j] == "BX" and playerList[i][j + 1] == "BX" and playerList[i][j + 2] == "BX" and \
                    playerList[i][j + 3] == "BX":
                playerList[i][j] = "BXF"
                playerList[i][j + 1] = "BXF"
                playerList[i][j + 2] = "BXF"
                playerList[i][j + 3] = "BXF"
                return 2
    if i < 7:
        if i < 6:
            if playerList[i][j] == "BX" and playerList[i + 1][j] == "BX" and playerList[i + 2][j] == "BX" and \
                    playerList[i + 3][j] == "BX" and playerList[i + 4][j] != "BX":
                playerList[i][j] = "BXF"
                playerList[i + 1][j] = "BXF"
                playerList[i + 2][j] = "BXF"
                playerList[i + 3][j] = "BXF"
                return 2
        else:
            if playerList[i][j] == "BX" and playerList[i + 1][j] == "BX" and playerList[i + 2][j] == "BX" and \
                    playerList[i + 3][j] == "BX":
                playerList[i][j] = "BXF"
                playerList[i + 1][j] = "BXF"
                playerList[i + 2][j] = "BXF"
                playerList[i + 3][j] = "BXF"
                return 2
    if i < 8:
        if i < 7:
            if playerList[i][j] == "DX" and playerList[i + 1][j] == "DX" and playerList[i + 2][j] == "DX" and \
                    playerList[i + 3][j] != "DX":
                playerList[i][j] = "DXF"
                playerList[i + 1][j] = "DXF"
                playerList[i + 2][j] = "DXF"
                return 3
        else:
            if playerList[i][j] == "DX" and playerList[i + 1][j] == "DX" and playerList[i + 2][j] == "DX":
                playerList[i][j] = "DXF"
                playerList[i + 1][j] = "DXF"
                playerList[i + 2][j] = "DXF"
                return 3
    if j < 8:
        if j < 7:
            if playerList[i][j] == "DX" and playerList[i][j + 1] == "DX" and playerList[i][j + 2] == "DX" and \
                    playerList[i][j + 3] != "DX":
                playerList[i][j] = "DXF"
                playerList[i][j + 1] = "DXF"
                playerList[i][j + 2] = "DXF"
                return 3
        else:
            if playerList[i][j] == "DX" and playerList[i][j + 1] == "DX" and playerList[i][j + 2] == "DX":
                playerList[i][j] = "DXF"
                playerList[i][j + 1] = "DXF"
                playerList[i][j + 2] = "DXF"
                return 3

    if i < 8:
        if i < 7:
            if playerList[i][j] == "SX" and playerList[i + 1][j] == "SX" and playerList[i + 2][j] == "SX" and \
                    playerList[i + 3][j] != "SX":
                playerList[i][j] = "SXF"
                playerList[i + 1][j] = "SXF"
                playerList[i + 2][j] = "SXF"
                return 4
        else:
            if playerList[i][j] == "SX" and playerList[i + 1][j] == "SX" and playerList[i + 2][j] == "SX":
                playerList[i][j] = "SXF"
                playerList[i + 1][j] = "SXF"
                playerList[i + 2][j] = "SXF"
                return 4
    if j < 8:
        if j < 7:
            if playerList[i][j] == "SX" and playerList[i][j + 1] == "SX" and playerList[i][j + 2] == "SX" and \
                    playerList[i][j + 3] != "SX":
                playerList[i][j] = "SXF"
                playerList[i][j + 1] = "SXF"
                playerList[i][j + 2] = "SXF"
                return 4
        else:
            if playerList[i][j] == "SX" and playerList[i][j + 1] == "SX" and playerList[i][j + 2] == "SX":
                playerList[i][j] = "SXF"
                playerList[i][j + 1] = "SXF"
                playerList[i][j + 2] = "SXF"
                return 4
    if i < 9:
        if i < 8:
            if playerList[i][j] == "PX" and playerList[i + 1][j] == "PX" and playerList[i + 2][j] != "PX":
                playerList[i][j] = "PXF"
                playerList[i + 1][j] = "PXF"
                return 5
        else:
            if playerList[i][j] == "PX" and playerList[i + 1][j] == "PX":
                playerList[i][j] = "PXF"
                playerList[i + 1][j] = "PXF"
                return 5
    if j < 9:
        if j < 8:
            if playerList[i][j] == "PX" and playerList[i][j + 1] == "PX" and playerList[i][j + 2] != "PX":
                playerList[i][j] = "PXF"
                playerList[i][j + 1] = "PXF"
                return 5
        else:
            if playerList[i][j] == "PX" and playerList[i][j + 1] == "PX":
                playerList[i][j] = "PXF"
                playerList[i][j + 1] = "PXF"
                return 5


sayi = 0
round = 0
f5.write("Battle of Ships Game\n\n")
while len(player1Moves) > 0 or len(player2Moves) > 0:   #The game starts this while loop
    round = round + 1
    sayi += 1
    if player1Moves.startswith("10"):
        player1NextMove = player1Moves[:4].split(",")
    else:
        player1NextMove = player1Moves[:3].split(",")
    if player2Moves.startswith("10"):
        player2NextMove = player2Moves[:4].split(",")
    else:
        player2NextMove = player2Moves[:3].split(",")
    player1NextMove[1] = returnLocationOfChar(player1NextMove[1])
    player1NextMove[0] = int(player1NextMove[0])
    player2NextMove[1] = returnLocationOfChar(player2NextMove[1])
    player2NextMove[0] = int(player2NextMove[0])
    f5.write("Player1's Move\n\n")               #The result starts to write on output file
    f5.write("Round: " + str(round))             #here shows the move of the player whose move order in each round is first
    f5.write("\t\t\t\t\t\t")
    f5.write("Grid Size: 10x10" + "\n\n")
    f5.write("Player1's Hidden Board" + "\t\t" + "Player2's Hidden Board" + "\n")
    f5.write(
        str("  A " + "B " + "C " + "D " + "E " + "F " + "G " + "H " + "I " + "J " + "\t\t" + "  A " + "B " + "C " + "D " + "E " +
            "F " + "G " + "H " + "I " + "J " + "\n"))

    for a in range(10):      
        f5.write(f"{str(a+1):2}")   
        for c in player1List[a]:    #in this for loop, the output writes for second player on first mover moves plays in a round
            if c == "CXF":
                c = "X"
            elif c == "PXF":
                c = "X"
            elif c == "BXF":
                c = "X"
            elif c == "DXF":
                c = "X"
            elif c == "SXF":
                c = "X"
            elif c == "BX":
                c = "X"
            elif c == "PX":
                c = "X"
            elif c == "DX":
                c = "X"
            elif c == "P":
                c = "-"
            elif c == "D":
                c = "-"
            elif c == "S":
                c = "-"
            elif c == "SX":
                c = "X"
            elif c == "B":
                c = "-"
            elif c == "C":
                c = "-"
            elif c == "CX":
                c = "X"
            f5.write(str(c) + " ")
        f5.write("\t\t")
        f5.write(f"{str(a+1):2}")            
        for c in player2List[a]:                #in this for loop, the output writes for second player on first mover moves plays in a round
            if c == "CXF":
                c = "X"
            elif c == "PXF":
                c = "X"
            elif c == "BXF":
                c = "X"
            elif c == "DXF":
                c = "X"
            elif c == "SXF":
                c = "X"
            elif c == "BX":
                c = "X"
            elif c == "PX":
                c = "X"
            elif c == "DX":
                c = "X"
            elif c == "P":
                c = "-"
            elif c == "D":
                c = "-"
            elif c == "S":
                c = "-"
            elif c == "SX":
                c = "X"
            elif c == "B":
                c = "-"
            elif c == "C":
                c = "-"
            elif c == "CX":
                c = "X"
            f5.write(str(c) + " ")
        f5.write("\n")
    f5.write(" " + " ")             #under this line file shows situation of two players's ships in each round
    f5.write("\n")                  
    f5.write("Carrier     " + "%-8s" %(str(int(1-numberOfCarrierPlayer1)* "X ") + str(int(numberOfCarrierPlayer1)* "- "))+"\t\t"+  "Carrier     " + "%-8s" %(str(int(1-numberOfCarrierPlayer2)* "X ") + str(int(numberOfCarrierPlayer2)* "- "))+"\n")
    f5.write("Battleship  " + "%-8s" %(str(int(2-numberOfBattlshipPlayer1)* "X ") + str(int(numberOfBattlshipPlayer1)* "- "))+"\t\t"+"Battleship  " + "%-8s" %(str(int(2-numberOfBattlshipPlayer2)* "X ") + str(int(numberOfBattlshipPlayer2)* "- "))+"\n")
    f5.write("Destroyer   " + "%-8s" %(str(int(1-numberOfDestroyerPlayer1)* "X ") + str(int(numberOfDestroyerPlayer1)* "- "))+"\t\t"+"Destroyer   " + "%-8s" %(str(int(1-numberOfDestroyerPlayer2)* "X ") + str(int(numberOfDestroyerPlayer2)* "- "))+"\n")
    f5.write("Submarine   " + "%-8s" %(str(int(1-numberOfSubmarinePlayer1)* "X ") + str(int(numberOfSubmarinePlayer1)* "- "))+"\t\t"+"Submarine   " + "%-8s" %(str(int(1-numberOfSubmarinePlayer2)* "X ") + str(int(numberOfSubmarinePlayer2)* "- "))+"\n")
    f5.write("Petrol Boat " + "%-8s" %(str(int(4-numberOfPetrolBoatPlayer1)* "X ") + str(int(numberOfPetrolBoatPlayer1)* "- "))+"\t\t"+"Petrol Boat " + "%-8s" %(str(int(4-numberOfPetrolBoatPlayer2)* "X ") + str(int(numberOfPetrolBoatPlayer2)* "- "))+"\n")
    f5.write("\n")
    f5.write("Enter your move: "+str(player1NextMove[0])+","+str(returnLocationOfInt(player1NextMove[1]))+"\n\n")

    if player2List[player1NextMove[0] - 1][player1NextMove[1]] == "-":
        player2List[player1NextMove[0] - 1][player1NextMove[1]] = "O"
    elif player2List[player1NextMove[0] - 1][player1NextMove[1]] == "C":
        player2List[player1NextMove[0] - 1][player1NextMove[1]] = "CX"
    elif player2List[player1NextMove[0] - 1][player1NextMove[1]] == "B":
        player2List[player1NextMove[0] - 1][player1NextMove[1]] = "BX"
    elif player2List[player1NextMove[0] - 1][player1NextMove[1]] == "D":
        player2List[player1NextMove[0] - 1][player1NextMove[1]] = "DX"
    elif player2List[player1NextMove[0] - 1][player1NextMove[1]] == "S":
        player2List[player1NextMove[0] - 1][player1NextMove[1]] = "SX"
    elif player2List[player1NextMove[0] - 1][player1NextMove[1]] == "P":
        player2List[player1NextMove[0] - 1][player1NextMove[1]] = "PX"

    for i in range(10):
        for j in range(10):
            if player2List[i][j] == "CX":
                a = sunkShip(player2List, i, j)
                if a == 1:
                    numberOfCarrierPlayer2 -= 1
            if player2List[i][j] == "BX":
                a = sunkShip(player2List, i, j)
                if a == 2:
                    numberOfBattlshipPlayer2 -= 1
            if player2List[i][j] == "DX":
                a = sunkShip(player2List, i, j)
                if a == 3:
                    numberOfDestroyerPlayer2 -= 1
            if player2List[i][j] == "SX":
                a = sunkShip(player2List, i, j)
                if a == 4:
                    numberOfSubmarinePlayer2 -= 1
            if player2List[i][j] == "PX":
                a = sunkShip(player2List, i, j)
                if a == 5:
                    numberOfPetrolBoatPlayer2 -= 1

    f5.write("Player2's Move\n\n")
    f5.write("Round: " + str(round))
    f5.write("\t\t\t\t\t\t")
    f5.write("Grid Size: 10x10" + "\n\n")
    f5.write("Player1's Hidden Board" + "\t\t" + "Player2's Hidden Board" + "\n")
    f5.write(
        str("  A " + "B " + "C " + "D " + "E " + "F " + "G " + "H " + "I " + "J " + "\t\t" + "  A " + "B " + "C " + "D " + "E " +
            "F " + "G " + "H " + "I " + "J " + "\n"))
    for a in range(10):
        f5.write(f"{str(a+1):2}")    
        for c in player1List[a]:     #in this for loop, the output writes for first player on first mover moves plays in a round
            if c == "CXF":
                c = "X"
            elif c == "PXF":
                c = "X"
            elif c == "BXF":
                c = "X"
            elif c == "DXF":
                c = "X"
            elif c == "SXF":
                c = "X"
            elif c == "BX":
                c = "X"
            elif c == "PX":
                c = "X"
            elif c == "DX":
                c = "X"
            elif c == "P":
                c = "-"
            elif c == "D":
                c = "-"
            elif c == "S":
                c = "-"
            elif c == "SX":
                c = "X"
            elif c == "B":
                c = "-"
            elif c == "C":
                c = "-"
            elif c == "CX":
                c = "X"
            f5.write(str(c) + " ")
        f5.write("\t\t")
        f5.write(f"{str(a+1):2}")
        for c in player2List[a]:           #in this for loop, the output writes for second player on second mover moves plays in a round
            if c == "CXF":
                c = "X"
            elif c == "PXF":
                c = "X"
            elif c == "BXF":
                c = "X"
            elif c == "DXF":
                c = "X"
            elif c == "SXF":
                c = "X"
            elif c == "BX":
                c = "X"
            elif c == "PX":
                c = "X"
            elif c == "DX":
                c = "X"
            elif c == "P":
                c = "-"
            elif c == "D":
                c = "-"
            elif c == "S":
                c = "-"
            elif c == "SX":
                c = "X"
            elif c == "B":
                c = "-"
            elif c == "C":
                c = "-"
            elif c == "CX":
                c = "X"
            f5.write(str(c) + " ")
        f5.write("\n")
    f5.write(" " + " ")
    f5.write("\n")
    f5.write("Carrier     " + "%-8s" %(str(int(1-numberOfCarrierPlayer1)* "X ") + str(int(numberOfCarrierPlayer1)* "- "))+"\t\t"+  "Carrier     " + "%-8s" %(str(int(1-numberOfCarrierPlayer2)* "X ") + str(int(numberOfCarrierPlayer2)* "- "))+"\n")
    f5.write("Battleship  " + "%-8s" %(str(int(2-numberOfBattlshipPlayer1)* "X ") + str(int(numberOfBattlshipPlayer1)* "- "))+"\t\t"+"Battleship  " + "%-8s" %(str(int(2-numberOfBattlshipPlayer2)* "X ") + str(int(numberOfBattlshipPlayer2)* "- "))+"\n")
    f5.write("Destroyer   " + "%-8s" %(str(int(1-numberOfDestroyerPlayer1)* "X ") + str(int(numberOfDestroyerPlayer1)* "- "))+"\t\t"+"Destroyer   " + "%-8s" %(str(int(1-numberOfDestroyerPlayer2)* "X ") + str(int(numberOfDestroyerPlayer2)* "- "))+"\n")
    f5.write("Submarine   " + "%-8s" %(str(int(1-numberOfSubmarinePlayer1)* "X ") + str(int(numberOfSubmarinePlayer1)* "- "))+"\t\t"+"Submarine   " + "%-8s" %(str(int(1-numberOfSubmarinePlayer2)* "X ") + str(int(numberOfSubmarinePlayer2)* "- "))+"\n")
    f5.write("Petrol Boat " + "%-8s" %(str(int(4-numberOfPetrolBoatPlayer1)* "X ") + str(int(numberOfPetrolBoatPlayer1)* "- "))+"\t\t"+"Petrol Boat " + "%-8s" %(str(int(4-numberOfPetrolBoatPlayer2)* "X ") + str(int(numberOfPetrolBoatPlayer2)* "- "))+"\n")
    f5.write("\n")
    f5.write("Enter your move: " + str(player2NextMove[0]) + "," + str(returnLocationOfInt(player2NextMove[1])) + "\n\n")




    if player1List[player2NextMove[0] - 1][player2NextMove[1]] == "-":
        player1List[player2NextMove[0] - 1][player2NextMove[1]] = "O"
    elif player1List[player2NextMove[0] - 1][player2NextMove[1]] == "C":
        player1List[player2NextMove[0] - 1][player2NextMove[1]] = "CX"
    elif player1List[player2NextMove[0] - 1][player2NextMove[1]] == "B":
        player1List[player2NextMove[0] - 1][player2NextMove[1]] = "BX"
    elif player1List[player2NextMove[0] - 1][player2NextMove[1]] == "D":
        player1List[player2NextMove[0] - 1][player2NextMove[1]] = "DX"
    elif player1List[player2NextMove[0] - 1][player2NextMove[1]] == "S":
        player1List[player2NextMove[0] - 1][player2NextMove[1]] = "SX"
    elif player1List[player2NextMove[0] - 1][player2NextMove[1]] == "P":
        player1List[player2NextMove[0] - 1][player2NextMove[1]] = "PX"

    for i in range(10):
        for j in range(10):
            if player1List[i][j] == "CX":
                a = sunkShip(player1List, i, j)
                if a == 1:
                    numberOfCarrierPlayer1 -= 1
            if player1List[i][j] == "BX":
                a = sunkShip(player1List, i, j)
                if a == 2:
                    numberOfBattlshipPlayer1 -= 1
            if player1List[i][j] == "DX":
                a = sunkShip(player1List, i, j)
                if a == 3:
                    numberOfDestroyerPlayer1 -= 1
            if player1List[i][j] == "SX":
                a = sunkShip(player1List, i, j)
                if a == 4:
                    numberOfSubmarinePlayer1 -= 1
            if player1List[i][j] == "PX":
                a = sunkShip(player1List, i, j)
                if a == 5:
                    numberOfPetrolBoatPlayer1 -= 1
    player1Won = 1
    player2Won = 1
    for i in range(10):
        for j in range(10):
            if player2List[i][j] == "C" or player2List[i][j] == "B" or player2List[i][j] == "D" or player2List[i][
                j] == "S" or player2List[i][j] == "P" \
                    or player2List[i][j] == "CX" or player2List[i][j] == "BX" or player2List[i][j] == "DX" or \
                    player2List[i][j] == "SX" or player2List[i][j] == "PX":
                player1Won = 0
    for i in range(10):
        for j in range(10):
            if player1List[i][j] == "C" or player1List[i][j] == "B" or player1List[i][j] == "D" or player1List[i][
                j] == "S" or player1List[i][j] == "P" \
                    or player1List[i][j] == "CX" or player1List[i][j] == "BX" or player1List[i][j] == "DX" or \
                    player1List[i][j] == "SX" or player1List[i][j] == "PX":
                player2Won = 0


    if player1Won == 1:
        f5.write("Player1 wins!" + "\n")
        player1Moves = ""
        player2Moves = ""
    if player2Won == 1:
        #f5.write(player1Moves + "\n")
        f5.write("Player2 wins!" + "\n")
        player1Moves = ""
        player2Moves = ""

    if player1Moves.startswith("10"):
        player1Moves = player1Moves[5:]
    else:
        player1Moves = player1Moves[4:]
    if player2Moves.startswith("10"):
        player2Moves = player2Moves[5:]
    else:
        player2Moves = player2Moves[4:]

f5.write("\n")
f5.write("Final Information" + "\n\n")
f5.write("Player1's Hidden Board" + "\t\t"+ "Player2's Hidden Board"+ "\n")
f5.write(str("  A " + "B " + "C " + "D " + "E " + "F " + "G " + "H " + "I " + "J " + "\t\t" + "  A " + "B " + "C " + "D " + "E " +
            "F " + "G " + "H " + "I " + "J " + "\n"))

for a in range(10):                   #in this for loop, the output writes for first player in final information
    for c in player1List[a]:
        if c == "CXF":
            c = "X"
        elif c == "PXF":
            c = "X"
        elif c == "BXF":
            c = "X"
        elif c == "DXF":
            c = "X"
        elif c == "SXF":
            c = "X"
        elif c == "BX":
            c = "X"
        elif c == "PX":
            c = "X"
        elif c == "DX":
            c = "X"
        elif c == "P":
            c = "P"
        elif c == "D":
            c = "D"
        elif c == "S":
            c = "S"
        elif c == "SX":
            c = "X"
        elif c == "B":
            c = "B"
        elif c == "C":
            c = "B"
        elif c == "CX":
            c = "X"
        f5.write(str(c) + " ")
    f5.write("\t\t")
    f5.write(f"{str(a+1):2}")
    for c in player2List[a]:             #in this for loop, the output writes for second player on final information
        if c == "CXF":
            c = "X"
        elif c == "PXF":
            c = "X"
        elif c == "BXF":
            c = "X"
        elif c == "DXF":
            c = "X"
        elif c == "SXF":
            c = "X"
        elif c == "BX":
            c = "X"
        elif c == "PX":
            c = "X"
        elif c == "DX":
            c = "X"
        elif c == "P":
            c = "P"
        elif c == "D":
            c = "D"
        elif c == "S":
            c = "S"
        elif c == "SX":
            c = "X"
        elif c == "B":
            c = "B"
        elif c == "C":
            c = "C"
        elif c == "CX":
            c = "X"
        f5.write(str(c) + " ")
    f5.write("\n")
f5.write(" " + " ")
f5.write("\n")
                                 #under this line file shows situation of two players's ships in final 
    
f5.write("Carrier     " + "%-8s" %(str(int(1-numberOfCarrierPlayer1)* "X ") + str(int(numberOfCarrierPlayer1)* "- "))+"\t\t"+  "Carrier     " + "%-8s" %(str(int(1-numberOfCarrierPlayer2)* "X ") + str(int(numberOfCarrierPlayer2)* "- "))+"\n")
f5.write("Battleship  " + "%-8s" %(str(int(2-numberOfBattlshipPlayer1)* "X ") + str(int(numberOfBattlshipPlayer1)* "- "))+"\t\t"+"Battleship  " + "%-8s" %(str(int(2-numberOfBattlshipPlayer2)* "X ") + str(int(numberOfBattlshipPlayer2)* "- "))+"\n")
f5.write("Destroyer   " + "%-8s" %(str(int(1-numberOfDestroyerPlayer1)* "X ") + str(int(numberOfDestroyerPlayer1)* "- "))+"\t\t"+"Destroyer   " + "%-8s" %(str(int(1-numberOfDestroyerPlayer2)* "X ") + str(int(numberOfDestroyerPlayer2)* "- "))+"\n")
f5.write("Submarine   " + "%-8s" %(str(int(1-numberOfSubmarinePlayer1)* "X ") + str(int(numberOfSubmarinePlayer1)* "- "))+"\t\t"+"Submarine   " + "%-8s" %(str(int(1-numberOfSubmarinePlayer2)* "X ") + str(int(numberOfSubmarinePlayer2)* "- "))+"\n")
f5.write("Petrol Boat " + "%-8s" %(str(int(4-numberOfPetrolBoatPlayer1)* "X ") + str(int(numberOfPetrolBoatPlayer1)* "- "))+"\t\t"+"Petrol Boat " + "%-8s" %(str(int(4-numberOfPetrolBoatPlayer2)* "X ") + str(int(numberOfPetrolBoatPlayer2)* "- "))+"\n")
f5.write("\n")



