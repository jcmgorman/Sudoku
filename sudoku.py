import random
import turtle
import ctypes
boarddim = 750
# CLASS FOR BOARD _____________________________________
class board:
    def __init__(self):
        self.dimension =  boarddim
        self.values = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #goes row by col
        '''[0,0,0,0]
           [0,0,0,0]
           [0,0,0,0]
           [0,0,0,0]'''
    def __init__(self,nums):
        self.dimension = boarddim
        self.values = nums[:]
    def drawsquare(self, dim):
        for x in range(4):
            turtle.forward(dim)
            turtle.right(90)
    def drawlitsquare(self,x,y,dim):    #draw the squares inside the larger squares
        turtle.width(2)
        xpos = x
        turtle.penup()
        turtle.goto(xpos,y)
        turtle.pendown()
        for r in range(4):
            self.drawsquare(dim)
            xpos = xpos + dim
            turtle.goto(xpos,y)
    def drawoutsquare(self,x,y, dim):   #draw the thick outline squares
        turtle.width(5)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        self.drawsquare(dim)
    def labelrows(self,x,y,dim):
        nums = ["A","B","C","D"]    #list of letters for ease of printing
        xpos = x - (dim//2)
        ypos = y - (dim//2)
        turtle.penup()
        turtle.goto(xpos ,ypos)
        for r in range(4):
             turtle.write(nums[r], move=False, align="left", font=("Arial", 28, "normal"))
             ypos = ypos - dim
             turtle.goto(xpos,ypos)
    def labelcolums(self,x,y,dim):
        nums = ["1","2","3","4"]    #list of numbers for ease of printing
        xpos = x + (dim//2)
        ypos = y + (dim//4)
        turtle.penup()
        turtle.goto(xpos ,ypos)
        for c in range(4):
             turtle.write(nums[c], move=False, align="left", font=("Arial", 28, "normal"))
             xpos = xpos + dim
             turtle.goto(xpos,ypos)
    def drawnums(self,x,y,dim):
        step = dim
        for ypos in range(4):   # go down through columns
            row = ypos
            for xpos in range(4):   #go down through rows
                colum = xpos
                turtle.goto((x + xpos * step)+dim//3, (y - ypos * step)- dim//2)
                if(self.values[row][colum] == 0):
                    turtle.write(" ", move=False, align="left", font=("Arial", 28, "normal"))  #if numbers is zero then don't print anything
                else:
                    turtle.write(self.values[row][colum], move=False, align="left", font=("Arial", 28, "normal"))


    def drawboard(self):    #Draw the board with lines, labes, and numbers
        turtle.clearscreen()
        turtle.ht()
        turtle.delay(0)
        turtle.speed(200)
        #draw the thick lines
        sqrdim = self.dimension//4
        xpos = self.dimension//4
        ypos = self.dimension//4
        self.drawoutsquare((-1 *xpos), ypos, sqrdim) #Draw Top Left Square
        self.drawoutsquare(0,ypos,sqrdim) # Draw Top Right Square
        self.drawoutsquare((-1 *xpos ), 0, sqrdim) # Draw Bottom Left Square
        self.drawoutsquare(0,0,sqrdim)  # Draw Bottom Right Square
        self.drawlitsquare((-1 * xpos),ypos,sqrdim//2)  # Draw top row
        self.drawlitsquare((-1 * xpos),(ypos//2),sqrdim//2)     # Draw middle top Row
        self.drawlitsquare((-1 * xpos),0,sqrdim//2)     #Draw middle bot Row
        self.drawlitsquare((-1 * xpos),(-1*(ypos//2)),sqrdim//2)    #Draw Bot Row
        self.labelrows((-1 * xpos),ypos,sqrdim//2)  # Label the rows with A - D
        self.labelcolums((-1 * xpos),ypos,sqrdim//2)    #Lable the colums with 1 - 4
        self.drawnums((-1 * xpos),ypos,sqrdim//2)
        
    def convertrow(self, r):
        if(r =='a'):
            return 0
        elif(r =='b'):
            return 1
        elif(r =='c'):
            return 2
        elif(r =='d'):
            return 3
        else: return -1
    def convertcol(self,c):
        if(c =='1'):
            return 0
        elif(c =='2'):
            return 1
        elif(c =='3'):
            return 2
        elif(c =='4'):
            return 3
        else: return -1
    def convertguess(self,guess):
        if(guess =='0'): return 0
        elif(guess == '1'): return 1
        elif(guess == '2'): return 2
        elif(guess == '3'): return 3
        elif(guess == '4'): return 4
        else: return -1
        
    def enternum(self): #How the user enters in the number
        validinput = False  #The flag that will be triggered when the input is not valid
        while(validinput == False):
            validinput = True   #Set the flag to true and if there is invalid input then the flag will be triggered.
            row = input("Enter in the Letter of the row: ")
            row = row.lower()
            row = self.convertrow(row)
            if row == - 1: validinput = False
            col = input("Enter in the Number of the column: ")
            col = self.convertcol(col)
            if col == -1: validinput = False
            num = input("Enter in the Guess: ")
            num = self.convertguess(num)
            if num == -1: validinput = False
            if validinput == False: print("INVALID INPUT")
        self.values[row][col] = num
    def fullboard(self):    # Checks to see if the board is full.
        for row in range(4):
            for col in range(4):
                if(self.values[row][col] == 0): return False
        return True
    def checkcol(self): # Go down each collum of the board and determine if the col has all unique values.
        for col in range(4):
            for test in range(1,5):
                ctr = 0
                for row in range(4):
                    if(self.values[col][row] == test): ctr+=1
                    if ctr > 1:
                        return False
        return True
    def checkrow(self):# Go down each row of the board and determine if the row has all unique values.
        for row in range(4):
            for test in range(1,5):
                ctr = 0
                for col in range(4):
                    if(self.values[row][col] == test): ctr+=1
                    if ctr > 1:
                        return False
        return True
    def checkbox(self): # Check each large box to make sure each value is unique
        for boxR in range (0,3,2):
            for boxC in range(0,3,2):
                for test in range(1,5):
                    ctr = 0
                    for row in range(2):
                        for col in range(2):
                            if(self.values[boxR + row][boxC + col] == test): ctr+=1
                            if ctr > 1:
                               return False
        return True
    def checkboard(self):
        if self.checkcol() == False: return False
        if self.checkrow() == False: return False
        if self.checkbox() == False: return False
        return True
        

    
        
#____________________________________________________________________________________________________

def submit():
    submit = input("Would you like to submit your puzzel? Enter Y or N. " )
    submit = submit.lower()
    if(submit == 'y'):
        submit = input("Are you sure? Enter Y or N. ")
        if(submit == 'y'): return True
        else: return False
    else: return False
def continueplay():
    cont = input("Would you like to play again? Enter Y or N. ")
    cont = cont.lower()
    if cont == 'y': return True
    else: return False
def main():
    instructions = "Welcome to Sudoku! The goal of the game is to fill up each column, row, and thick outlined box with numbers from 1 to 4 with no duplicates. To enter your guess, enter the row, then the column, and finally your guess. To erase a box, enter in a 0. You do not need to erase a box to change the value. If an invalid input is entered you will receive and error. "
    ctypes.windll.user32.MessageBoxW(0, instructions, "Welcome to Sudoku!", 0)
    play = True # Are you playing the game
    winner = False # Are you the winner of this puzzel
    cont = False
    board1 = [[3,4,1,2],[0,0,0,0],[0,0,0,0],[4,2,3,1]]
    '''[3,4,1,2]
       [0,0,0,0]
       [0,0,0,0]
       [4,3,2,1]'''
    board2 = [[4,0,0,1],[0,1,3,0],[0,4,1,0],[1,0,0,3]]
    '''[4,0,0,1]
       [0,1,3,0]
       [0,4,1,0]
       [1,0,0,3]'''
    board3 = [[0,0,0,0],[2,3,4,1],[3,4,1,2],[0,0,0,0]]
    '''[0,0,0,0]
       [2,3,4,1]
       [3,4,1,2]
       [0,0,0,0]'''
    board4 = [[0,2,4,0],[1,0,0,3],[4,0,0,2],[0,1,3,0]]
    '''[0,2,4,0]
       [1,0,0,3]
       [4,0,0,2]
       [0,1,3,0]'''
    board5 = [[0,0,4,0],[1,0,0,3],[2,0,0,4],[0,1,0,0]]
    '''[0,0,4,0]
       [1,0,0,3]
       [2,0,0,4]
       [0,1,0,0]'''
    while(play == True):
        boardbook = [board1,board2,board3,board4,board5]    #Book (list) of the puzzles
        pagenumber = random.randint(0,4)    #Picks the radom puzzle
        test = board(boardbook[pagenumber])
        winner = False
        while(winner == False):
            test.drawboard()
            test.enternum()
            test.drawboard()
            sub = False
            if(test.fullboard() == True): sub = submit()  #Checks to see if player wishes to submit puzzel for checking
            if sub == True:
                test.checkboard()
                che = False
                che = test.checkboard()   #Check and sees if puzzel is correct
                if che == True: #Player has won
                    winner = True
                    print("WINNER!")
                    cont = continueplay()   #Checks to see if player wishes to play again
                else: print("Incorrect.")
        if cont == True and winner == True:
            winner = False
        elif cont == False:
            print("Thank You For Playing.")
            play = False
#________________________________________________________________
if __name__ == "__main__":
    main()
