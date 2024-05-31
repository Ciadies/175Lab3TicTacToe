#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: Sebastian
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           
        divider = "-" * 11
        print("  0   1   2 ") #Column Headers
        for i in range(3): #iterates through all 3 rows
            rows = [] #Create a list to track the specific values of the row
            for j in range(3): #iterates through the 3 columns of the row
                if self.squareIsEmpty(i,j): #removes all the 0s from the list
                    rows.append(" ") 
                else :
                    rows.append(self.board[i][j]) #Adds the integer value to the row list
            print(f"{i}  {rows[0]} | {rows[1]} | {rows[2]} ")
            if i != 2 : #doesn't print divider for last row
                print(f"  {divider}")


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        if self.board[row][col] > 0:
            return False
        else:
            return True
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True
        else :
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.squareIsEmpty(i,j) :
                    return False
        return True
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        for row in self.board: #checks all rows
            sumOf = 0
            for tile in row: #checks each tile in the row
                if tile == 0:
                    break #not a full line -> not a win
                else:
                    sumOf = sumOf + tile        
            if sumOf == 15:
                return True    #win the game
            
        for j in range(len(self.board)): #check columns, goes over 0 1 2 (column indexes)
            for row in self.board: #
                if row[j] == 0: #not a full line -> not a win
                    break
                else:
                    sumOf = sumOf + row[j]
            if sumOf == 15:
                return True #win the game
            
        diaSum = 0# can't put in the for loop otherwise it resets each time
        for i in range(len(self.board)): #checks 0,0 1,1 2,2
            if self.board[i][i] == 0:
                break
            else:
                diaSum = diaSum + self.board[i][i]
            if diaSum == 15:
                return True
            
        diaSum = 0 #same reason as above
        for i in range(len(self.board)): #checks the other diagonal
            j = (len(self.board) - 1) - i #gets the column since need to check 0,2 1,1 2,0 or (0, 2-0) (1, 2-1) (2, 2-2). -1 makes it so it works as an index
            if self.board[i][j] == 0:
                break
            else:
                diaSum = diaSum + self.board[i][j]
            if diaSum == 15:
                return True
        
        return False #if no other case is True returns False
        
if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)
    
    # does the empty board display properly?
    myBoard.drawBoard()

    # assign a number to an empty square and display
    myBoard.board[1][1] = 1
    myBoard.drawBoard()
    # try to assign a number to a non-empty square. What happens?
    myBoard.update(1, 1, 3)
    myBoard.drawBoard()
    # check if the board has a winner. Should there be a winner after only 1 entry?
    print(myBoard.isWinner())
    # check if the board is full. Should it be full after only 1 entry?
    print(myBoard.boardFull())
    # add values to the board so that any line adds up to 15. Display
    myBoard.update(0,2,9)
    myBoard.update(2,0,5) #each individual case can also be tested by changing the values in update
    myBoard.drawBoard()
    # check if the board has a winner
    print(myBoard.isWinner())
    # check if the board is full
    print(myBoard.boardFull())
    # write additional tests, as needed
    #tests the isFull function
    for i in range(3): 
        for j in range(3):
            myBoard.board[i][j] = 1
    print(myBoard.boardFull())
    