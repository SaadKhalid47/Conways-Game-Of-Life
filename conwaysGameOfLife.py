from PIL import Image, ImageDraw
import copy
import os
import glob
directory = os.getcwd()
gen = 0
flag = True
while flag == True:
    try:
        row = int(input("Please enter the dimesnsions of the grid: "))
        if row <= 0:
         raise ValueError
    except (ValueError):
        flag == True
        print("Brain dead dummy")
    else:
        flag = False

column = row

max = (column*row)

indexvalues = []
maxpixel = row * 100
im = Image.new('RGB', (maxpixel,maxpixel), (255,255,255))
dr = ImageDraw.Draw(im)
for i in range(0,row):
    for j in range(0,row):
        list = ([(0+j*100,0+i*100),(100+j*100,100+i*100)])
        indexvalues.append(list)
        dr.rectangle([(0+i*100,0+j*100),(100+i*100,100+j*100)], fill="lightgray", outline = "black")


#Initializes the grid and alligns the place values
def allignGrid(grid):
    newgrid = grid.copy()
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
allignGrid(gameField)
underPop = []
overPop = []
breed = []
justRight = []
#Adds live cells
addLive = True
while addLive == True:
    numInput = input("What number would you like to make alive(q to quit adding: ")
    try:
        if numInput =="q":
            addLive = False
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
                if gameField[rowCalc][colCalc] == "@":
                    print("This cell is already live bozo")
                    print()
                else:
                    gameField[rowCalc][colCalc] = "@"
                    '''
                    for x in range(len(gameField)):
                        for y in range(len(gameField[x])):
                            print(gameField[x][y])
                            '''
                    allignGrid(gameField)
                    gameFieldcopy = gameField
                    new_list = []
                    for i in gameFieldcopy:
                        for gameFieldcopy in i:
                            new_list.append(gameFieldcopy)
                    index = int(numInput)
                    index = index-1        
                    numInput = int(numInput)
                    dr.rectangle((indexvalues[index]), fill = "black")
            if numInput > max or numInput < 1:
                print("Out of range even shawn can count better...")
                print()
    except ValueError:
        print("Please try again brain dead dummy")
        print()
#Rules
'''
Underpopulation Any live cell with fewer than two neigbours dies
Just Right Any live cell with 2 or 3 neighbours will live on to the next generation
Overpopulation Any live cell with more than three live neighbours will die
Breeding Any dead cell with exactly 3 neighbours will come to life'''
width = row
height = column
gen = 1
gencount = 0
cont = True
nextGen = (int(input("How many generations do you want to see? ")))
for x in range(nextGen):
    while cont == True:
        print("\n\nGeneration ", gen)
        print("\n")
        allignGrid(gameField)
        currentCell = copy.deepcopy(gameField)
        print('\n')
        gen = gen + 1
        gencount = gencount + 1
        for x in range(width):
            for y in range(height):
                livingCell = 0
                leftCoordinate = x - 1
                rightCoordinate = x + 1
                upperCoordinate = y - 1
                lowerCoordinate = y + 1
                if leftCoordinate > -1 and currentCell[leftCoordinate][y] == "@":
                    livingCell = livingCell + 1
                if rightCoordinate < width and currentCell[rightCoordinate][y] == "@":
                    livingCell = livingCell + 1
                if upperCoordinate > -1 and currentCell[x][upperCoordinate] == "@":
                    livingCell = livingCell + 1
                if lowerCoordinate < height and currentCell[x][lowerCoordinate] == "@":
                    livingCell = livingCell + 1
                if leftCoordinate > -1 and upperCoordinate > -1 and currentCell[leftCoordinate][upperCoordinate] == "@":
                    livingCell = livingCell + 1
                if rightCoordinate < width and upperCoordinate > -1 and currentCell[rightCoordinate][upperCoordinate] == "@":
                    livingCell = livingCell + 1
                if rightCoordinate < width and lowerCoordinate < height and currentCell[rightCoordinate][lowerCoordinate] == "@":
                    livingCell = livingCell + 1
                if leftCoordinate > -1 and lowerCoordinate < height and currentCell[leftCoordinate][lowerCoordinate] == "@":
                    livingCell = livingCell + 1
                if currentCell[x][y] == "@" and (livingCell == 2 or livingCell == 3):
                    gameField[x][y] = "@"
                    justRight.append((column * x) + y + 1)
                elif currentCell[x][y] == "@" and (livingCell < 2 or livingCell > 3):
                    gameField[x][y] = (column * x) + y + 1
                    if (livingCell < 2):
                        underPop.append((column * x) + y + 1)
                    else:
                        overPop.append((column * x) + y + 1)
                elif (currentCell[x][y] != "@") and livingCell == 3:
                    gameField[x][y] = "@"
                    breed.append((column * x) + y + 1)
                else:
                    gameField[x][y] = gameField[x][y]
        print("Underpopulation: ", end = "")
        for x in underPop:
            print(x, end = " ")
        if (len(underPop) == 0):
            print ("none")
        else:
            print ("die")
        print("Overpopulation: ", end = "")
        for x in (overPop):
            print(x, end = " ")
        if (len(overPop) == 0):
            print ("none")
        else:
            print ("die")
        print("Just Right ", end = "")
        for x in (justRight):
            print(x, end = " ")
        if (len(justRight) == 0):
            print ("none")
        else:
            print ("stay alive")
        print("Breed: ", end = "")
        for x in (breed):
            print(x, end = " ")
        if (len(breed) == 0):
            print ("none")
        else:
            print ("come alive")
        underPop.clear()
        overPop.clear()
        justRight.clear()
        breed.clear()  
        gameFieldcopy = currentCell
        new_list = []
        liveCellIndexes = []
        otherCells = []

        for i in gameFieldcopy:
            for gameFieldcopy in i:
                new_list.append(gameFieldcopy)
        if '@' in new_list:
            livecellinlist = True

        if livecellinlist == True:
            for i in range(len(new_list)):
                if new_list[i] == "@":
                    liveCellIndexes.append(i)
            indexcount = 0
            for i in range(len(liveCellIndexes)):
                index = liveCellIndexes[indexcount]
                dr.rectangle((indexvalues[index]), fill = "black")
                indexcount +=1

            for i in range(len(new_list)):
                if new_list[i] != "@":
                    otherCells.append(i)
            indexcount = 0
            for i in range(len(otherCells)):
                index = otherCells[indexcount]
                dr.rectangle((indexvalues[index]), fill = "lightgray")
                indexcount +=1

        if livecellinlist == False:
            index = 0
            for i in range(max):
                dr.rectangle((indexvalues[index]), fill = "lightgray")
                index +=1
        nextGenString = str(gencount)
        saves = []
        saveFile = nextGenString + "text.png"
        saves.append(saveFile)
        im.save(saveFile)
        if gencount == nextGen:
            cont = False
        im.show()   
frames = []
imgs = glob.glob("*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)
 
frames[0].save('png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)

#saves[0].save('Conwaysgameoflife/GIF.gif', save_all=True, append_images=saves[1:], optimize = False, duration = 250, loop = 0)