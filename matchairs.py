#Final Project for HMC CS5
#Name: Mehrin Khan
#Final Project Name: "Machairs"  [Numbermatch game]
#Project Type" Text based game 

import random

class NumberMatchGame:
    """A class to represent the Number Match game."""

    def __init__(self, rows, cols):
        """The constructor. Creates a game board with random numbers and pairs."""
        self.rows = rows
        self.cols = cols
        self.table = [[random.randint(0, 9) for j in range(cols)] for i in range(rows)] #creates 2D list of 0 to 9 
        self.displaytable=[['O' for j in range(cols)] for i in range(rows) ] #dispplays the table that users sees which is entirely "o" 
        self.previous_check = 0 #check the last sturn but nit doing anything
        self.user_score= 0
        self.ai_score= 0
        self.user_turn= True 
         
        
    

    def __repr__(self):
        """The representation function. Prints the board in a table format."""
        s = ' '
        for j in range(self.cols):
            s += f" {j}" #the f before string if for formatted string  and the string spaces out 0.1.2.3
        s += '\n'
        for i in range(self.rows):
            s += f"{chr(i+65)}" #creates the row labels  A to F and
            for j in range(self.cols):
                s += f" {self.displaytable[i][j]}" #shows only this to the user. So that they can keep 
            s += '\n'
        return s
    
    def select_cell(self, row, col):
        """Selects a cell and removes matching pairs from the board. Puts 'X' if it is a match and revert back 
        to 'o' if it is not a match. Inceremetns the score as well. """
        #if
        #value in range (self.table[row][col]):
        value = self.table[row][col]
        if self.user_turn:
            if self.displaytable[row][col] == 'X': # added this line to check if cell has already been matched
                print("You have already matched this cell!")
            if  self.previous_check== 0:  #checking the first item 
                print("checks the first item")
                self.displaytable[row][col]= self.table[row][col] #shows the choose row,col of the main number table
                print(self) #goes back to display table
                self.displaytable[row][col]= 'O'# 
                self.previous_check=(row,col) #stored value 
            elif self.previous_check == (row, col): #nEW line to check if cell has already been selected in this turn
                print("You have already selected this cell! cHOose another one")
            else:
                print("checks the second item")
                past_row,past_col= (self.previous_check[0],  self.previous_check[1]) #pasr_row and past_col stores the previous check of 0 and previous check of 1
                if  self.table[past_row][past_col] ==self.table[row][col]:  #number table previous input number=  n.table currect input number
                    
                    print("" + "\033[6;35;40m" + "It is a match WoHo!! 🤩 " + "\033[0m" + "")
                    print(self.table[row][col])
                    self.displaytable[row][col]='X'
                    self.table[row][col]= 'X'
                    self.displaytable[past_row][past_col]='X'
                    self.table[past_row][past_col]= 'X'
                    self.previous_check= 0
                    if  self.user_turn== True:
                        self.user_score+=1
                        print("The score is",self.user_score)
                    else: 
                        self.ai_score+=1 
                        print("your score is",self.ai_score)
                else: 
                    self.displaytable[row][col]= self.table[row][col] #shows the number 
                    print(self) #goes back to display table
                    self.displaytable[row][col]= 'O'# 
                    self.previous_check= 0    #stored value
                    
                    print("" + "\033[6;35;40m" + "Not a match. Bettler luck next time 😞" + "\033[0m" + "")
    


    def ai_select_cell(self):
        """ Make the computer choose its input. Like A0,B2"""
        conversion =['A','B','C','D','E','F']
        r= random.randint(0, (self.rows)-1)
        c= random.randint(0, (self.cols)-1)
        while self.displaytable[r][c] != 'O':
            r= random.randint(0, (self.rows)-1)
            c= random.randint(0, (self.cols))

        return conversion[r] + str(c)
    

    def is_game_over(self):
        """Checks if the game is over."""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.displaytable[i][j] == 'O':
                    return False
        print("Game over!")
        print("User score:", self.user_score)
        print("AI score:", self.ai_score)
        if self.user_score > self.ai_score:
            print("Congratulations, you win!")
        elif self.ai_score > self.user_score:
            print("Better luck next time, the AI wins!")
        else:
            print("It's a tie!")
        return True

  

    def play(self):
        """Plays the game."""
        print(self)
        score = 0
        while not self.is_game_over():
            cell = input("Select first cell (e.g. A2): ")
            #ifcell 
            row = ord(cell[0].upper()) - ord('A') #capitalizes 
            col = int(cell[1])
            
            if row < 0 or row > 7 or col < 0 or col > 7:
                print("Error! Select a cell from A0 to F6.")
                continue
            value = self.select_cell(row, col)
            print(self)
            cell1 = input("Select another  cell (e.g. A2) to make it a match: ")
            row1 = ord(cell1[0].upper()) - ord('A') #capitalizes 
            col1 = int(cell1[1])
            value1 = self.select_cell(row1, col1)
            print(self)
            print("Ai picks its input")
            if isinstance(value, tuple): #The tuple check the number pairs and the after cutting makes it ','
                score += 10
            
            cell_ai = self.ai_select_cell()
            row_ai = ord(cell_ai[0].upper()) - ord('A') #capitalizes 
            col_ai= int(cell_ai[1])
            print("AI PICKED: " +  str(row_ai) + ", " + str(col_ai))
            value_ai = self.select_cell(row_ai, col_ai)
            

            print(self)
            print("AI picks its input")
            cell_ai1 = self.ai_select_cell()
            row_ai1 = ord(cell_ai1[0].upper()) - ord('A') #capitalizes 
            col_ai1 = int(cell_ai1[1])
            print("AI PICKED: " + str(row_ai1) + ", " + str(col_ai1))
            value_ai1 = self.select_cell(row_ai1, col_ai1)
            print(self)
        print("Score: {score}")

        # Create a game object and play the game

game = NumberMatchGame(6, 7)
game.play()
