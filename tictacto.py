from functools import cache
import os
import time
import copy
import pathlib

def game():
    row = 3
    column = 3
    max = (column*row)

    print("\u001b[35m")
    def allignGrid(newgrid):
        maxLen = len(str(newgrid[-1][-1]))
        for row in newgrid:
            for elem in row: 
                print(elem, end=" ")
                if len(str(elem)) < maxLen and maxLen <= 2:
                    counter = maxLen - len(str(elem))
                    while counter < maxLen:
                        print("", end = " ")
                        counter += 1
                if maxLen > 2:
                    counter = maxLen - len(str(elem))
                    if maxLen == 3:
                        if len(str(elem)) == 1:
                            print(" ", end=" ")
                            counter += 1
                        elif len(str(elem)) == 2:
                            print("",end=" ")
                            counter += 1
            print("")
    gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
    length = len(gameField)
    print("\u001b[35;1m")
    #Winning combinations 
    #Horizontal
    l1 = [1,2,3]
    l2 = [4,5,6]
    l3 = [7,8,9]

    #Vertical

    l4 = [1,4,7]
    l5 = [2,5,8]
    l6 = [3,6,9]

    #Diagonal
    l7 = [1,5,9]
    l8 = [3,5,7]

    black = ("\u001b[30;1m")
    red = ("\u001b[31;1m")
    green = ("\u001b[32;1m")
    yellow = ("\u001b[33;1m")
    blue = ("\u001b[34;1m")
    magenta = ("\u001b[35;1m")
    cyan = ("\u001b[36;1m")
    white = ("\u001b[37;1m")
    foldername = "Tictactoe"
    listX = []
    listO = []
    count = 0
    round = 1
    tie = False
    win = False
    curplayer = "O"
    curplayertag = "A"
    curcolor = yellow
    addMove = True
    playagain= True
    next = False

    print("Welcome To Tic Tac Toe")
    welcome = input("Do you want to load a game or start a new game? (L,N) ")
    while welcome != "n" and welcome != "N" and welcome != "New" and welcome != "new" and welcome != "l" and welcome != "L" and welcome != "load" and welcome != "Load":
        print("Please enter a valid input")
        welcome = input("Do you want to load a game or start a new game? (L,N) ")
    if welcome == "n" or welcome == "N" or welcome == "New" or welcome == "new":
        listX = []
        listO = []
        count = 0
        round = 1
        tie = False
        win = False
        curplayer = "O"
        curplayertag = "A"
        curcolor = yellow
        addMove = True
        playagain= True
    if welcome == "l" or welcome == "L" or welcome == "Load" or welcome == "load":
        directory = os.getcwd()
        numberFiles = []
        next = False
        filenames = os.listdir(os.getcwd())
        for fname in filenames:
            if fname.endswith(".txt"):
                print('Saves: ' + fname)
                numberFiles.append(fname)
        if len(numberFiles) == 0:
            print("There are no saved games please start a new game")
            game()
        while next == False:
            if __name__ == '__main__':
                save = input("What save would u like to open?(include the suffix) ")
                pathcheck = pathlib.Path(save)
                if pathcheck.exists():
                    next = True
                    a_file = open(save, "r")
                    list_of_lists = [(line.strip()).split() for line in a_file]
                    count = list_of_lists[0]
                    strings = [str(integer) for integer in count]
                    a_string = "".join(strings)
                    count = int(a_string)
                    round = list_of_lists[1]
                    strings = [str(integer) for integer in round]
                    a_string = "".join(strings)
                    round = int(a_string)
                    curplayer = list_of_lists[2]
                    curplayer = (" ".join(curplayer))
                    curplayertag = list_of_lists[3]
                    curplayertag = (" ".join(curplayertag))
                    listO = list_of_lists[4]
                    listO = list(map(int, listO))
                    listX = list_of_lists[5]
                    listX = list(map(int, listX))

                    import linecache
                    particular_line = linecache.getline(save, 7)
                    gameField = particular_line
                    gameField = [x.strip('\"') for x in gameField.strip("[]").split(",")]
                    gameField = [s.replace("'", "") for s in gameField]
                    gameField = [s.replace("\n", "") for s in gameField]
                    gameField = [s.replace("]", "") for s in gameField]
                    gameField = [s.replace("]", "") for s in gameField]
                    gameField = [s.replace("[", "") for s in gameField]
                    gameField = [s.replace(" ", "") for s in gameField]
                    gameField = "".join(gameField)
                    index1 = (gameField[0])
                    index2 = (gameField[1])
                    index3 = (gameField[2])
                    index4 = (gameField[3])
                    index5 = (gameField[4])
                    index6 = (gameField[5])
                    index7 = (gameField[6])
                    index8 = (gameField[7])
                    index9 = (gameField[8])
                    gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                    gameField[0][0] = index1
                    gameField[0][1] = index2
                    gameField[0][2] = index3
                    gameField[1][0] = index4
                    gameField[1][1] = index5
                    gameField[1][2] = index6
                    gameField[2][0] = index7
                    gameField[2][1] = index8
                    gameField[2][2] = index9 
                
                    if curplayer == "O":
                        print(cyan)
                    else:
                        print("Round", red,round)
                        print(yellow)
                    allignGrid(gameField)
                    a_file.close()
                else:
                    print("File not found please enter a valid input")
                    next = False

    while playagain == True:
        while tie == False:
            while addMove == True:
                print("\u001b[37;1m")
                if curplayertag == "A":
                    curcolor = yellow
                if curplayertag == "B":
                    curcolor = cyan
                print("It is your turn player", curcolor, curplayertag)
                print("Round", red,round)
                print(yellow)
                allignGrid(gameField)
                print(white)
                numInput = input("Whats your move(q to quit) ")
                if numInput != "q":
                    print("Round", red,round)
                if numInput == "q" or numInput == "Q" or numInput == "quit" or numInput == "Quit":
                    playagain = False
                    addMove = False
                    quit = input("Do you want to save or discard? (s,d) ")
                    while quit != "d" and quit != "D" and quit != "discard" and quit != "Discard" and quit != "s" and quit != "S" and quit != "save" and quit != "Save":
                        print("Please enter a valid input")
                        quit = input("Do you want to save or discard? (s,d) ")
                    if quit == "d" or quit == "D" or quit == "discard" or quit == "Discard":
                        print (magenta)
                        print("Thank you for playing")
                        (exit)
                    if quit == "s" or quit == "S" or quit == "save" or quit == "Save":
                        name = input("Please enter the name of the file: ")
                        countstr = str(count)
                        roundstr = str(round)
                        curplayerstr = str(curplayer)
                        curplayertagstr = str(curplayertag)
                        listOstr = ' '.join([str(elem) for elem in listO])
                        listXstr = ' '.join([str(elem) for elem in listX])
                        gameFieldstr = str(gameField)
                        filename = "%s.txt" % name
                        with open(filename, 'w') as f:
                            f.write(countstr)
                            f.write("\n")
                            f.write(roundstr)
                            f.write("\n")
                            f.write(curplayerstr)
                            f.write("\n")
                            f.write(curplayertagstr)
                            f.write("\n")
                            f.write(listOstr)
                            f.write("\n")
                            f.write(listXstr)
                            f.write("\n")
                            f.write(gameFieldstr)
                        playagain = input("Do you want to play again?(y,n) ")
                        if playagain == ("y"):
                            playagain = True
                            game()
                        else:
                            playagain = False
                            addMove = False
                            print("Thank you for playing")
                            (exit)
                try:
                    if numInput =="q":
                        addMove = False
                        break
                    else:
                        numInput = int(numInput)
                        if numInput > 0 and numInput <= max:
                            colCalc = numInput % column - 1
                            if (numInput / column) % 1 == 0:
                                colCalc = column - 1
                            rowCalc = numInput // column
                            if (numInput / column) % 1 == 0:
                                rowCalc = numInput // column - 1
                            if gameField[rowCalc][colCalc] == "X" or gameField[rowCalc][colCalc] == "O":
                                print("This cell is already taken bozo")
                                print()
                            else:
                                count = count + 1
                                round = round + 1
                                if curplayer == "O":
                                    print(yellow)
                                if curplayer == "X":
                                    print(cyan)
                                gameField[rowCalc][colCalc] = curplayer
                                if curplayer == "O":
                                    listO.append(numInput)
                                listO.sort
                                if curplayer == "X":
                                    listX.append(numInput)
                                listX.sort
                                if curplayer == "O":
                                    curplayer = "X"
                                else: curplayer = "O"
                                if curplayertag == "A":
                                    curplayertag = "B"
                                else: curplayertag = "A"
            
                            if all((w in listO for w in l1)):
                                win = True
                                addMove = False
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                listX = []
                                listO = []
                                round = 1
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)
                            if all((w in listO for w in l2)):
                                win = True
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                round = 1
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                listX = []
                                listO = []
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)
                                    
                            if all((w in listO for w in l3)):
                                win = True
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listO for w in l4)):
                                win = True
                                addMove = False
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listO for w in l5)):
                                win = True
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listO for w in l6)):
                                win = True
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listO for w in l7)):
                                win = True
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False                                
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listO for w in l8)):
                                win = True
                                print(magenta)
                                print("Player A has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False                                
                                    print("Thank you for playing")
                                    (exit)


                            if all((w in listX for w in l1)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listX for w in l2)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listX for w in l3)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                tie = False
                                listX = []
                                listO = []
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listX for w in l4)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listX for w in l5)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    addMove = False                                
                                    playagain = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listX for w in l6)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    addMove = False
                                    game()
                                else:
                                    playagain = False
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listX for w in l7)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False                                
                                    print("Thank you for playing")
                                    (exit)

                            if all((w in listX for w in l8)):
                                win = True
                                print(magenta)
                                print("Player B has won the game!")
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                    playagain = True
                                    game()
                                else:
                                    playagain = False
                                    addMove = False
                                    print("Thank you for playing")
                                    (exit)

                            allignGrid(gameField)
                            print(white)
                            if count == 9 and win == False:
                                count = 0
                                round = 1
                                listX = []
                                listO = []
                                tie = False
                                win = False
                                curplayer = "O"
                                curplayertag = "A"
                                curcolor = yellow
                                addMove = True
                                playagain= True
                                gameField = [[(j+1)+column*i for j in range(column)] for i in range(row)]
                                playagain = input("Do you want to play again?(y,n) ")
                                if playagain == ("y"):
                                        playagain = True
                                        game()
                                else:
                                        playagain = False
                                        addMove = False
                                        print("Thank you for playing")
                                        (exit)                                
                        else:
                            print(red)
                            print("That number is out of range...")
                            print("Please try again and enter a valid input brain dead dummy")
                            print()
                except ValueError or numInput > 9:
                    print("Please try again and enter a valid input brain dead dummy")
                    print()
game()