   
--------------------------------------------------------------------------------------------------------------
# ID: *******
# Milestone 3 Icebreaker Documentaton (ReadMe) Completed Game
#-------------------------------------------------------------------------------------------------------------

# Importing all the neccessary components (GraphWin, Rectangle, Point, Text) that will be used throughout many of the classes and functions (if not all) from the graphics library 

from graphics import GraphWin, Rectangle, Point, Text, Circle

# The Icebreaker Class will setup the game board and implement the game logic; meaning that that the functionality and playment of the actual game is controlled / done mainly by the Icebreaker Class as it will setup the game board and implement the game logic to have the game working, running, functioning and playing properly

class Icebreaker:
"""
Purpose:
etup the game board and implement the game logic; meaning that that the functionality and playment of the actual game is controlled / done mainly by the Icebreaker Class as it will setup the game board and implement the game logic to have the game working, running, functioning and playing properly

Paramater: None
Results: None
"""

    
    def __init__(self, width, height):
    """
    Purpose: Initalizes the game attributes like board dimesnions, the GraphWin Object, Buttons and Messages, Score Tracker, Current Player,Mouse Status, Player Status, etc.
    
    Paramater: Int - the width of the gameboard and the height of the gameboard is taken as a parameter as an inetger
    
    Results: None - (except all of the game functionality and attributes created) 
    """
        self.width = width                             # Initalizes the width of the gameboard
        self.height = height                           # Initalizes the height of the game 
        self.win = GraphWin("Vickrams Icebreaker Game- Version 1.0 - March-03-26", 550, 775)    # Initalizes the GraphWin window for the game interference
        self.player0_score = 0                          # Initalizes the score of Player 1 
        self.player1_score = 0                          # Initalizes the score for Player 1
        #self.mouse = Text(Point(100, 615), "Mouse")    
        #self.mouse.setSize(21)
        #self.mouse.setOutline("Orange")
        #self.mouse.draw(self.win)
        self.board= Board(self.win, width, height)        # Initalizes the gameboard using the Board Class
        self.player0, self.player1 = self.player_creations()  # Initalizes both players (Player0 and Player1) using the player_creations method 
        self.current_player = self.player0      # This will setup Player0 as the starting player / current player                       
        self.button_creations()     # This calls the button_creations function/method that creates the buttons for the game (the RESET buttons and QUIT button)
        
        self.player_action = "Move"    # Sets the inital action / task of the player to "Move" where the player will then move as they're told to move their peice/player.
       
        # Initalizes the text object for the mouse status, which will display the mouse click status message showing the Board Coordinates of a valid board click, or the text "NOT VALID". Or when the QUIT and RESET button are clciked it will display their messages accordingly too. (which will also be seen / later implemented in the play function of the Icebreaker Class) 
        
        self.mouse_status = Text(Point(100,665), "")  
        self.mouse_status.setSize(16)
        self.mouse_status.setOutline("Pink")
        self.mouse_status.draw(self.win)
        
        
        # Initalizes the text object for the Player Status, which will display / inform the users who's turn it is, and what their next task is (move or break ice). It will also display their current postion / coordinates on the gameboard, and will also display the Winning Player once a winner has been determined (which will also later be seen / later implemented in the play function of the Icebreaker Class)
        
        self.player_status = Text(Point(100, 610), f"Player 0: (0,0)\nMove")
        self.player_status.setSize(16)
        self.player_status.setOutline("Pink")
        self.player_status.draw(self.win)
       
    def button_creations(self):
    """
    Purpose: To create the neccessary buttons (QUIT buttons and RESET button) for the game interface
    Parameters: None
    Results: None
    """
        self.quit_button = Rectangle(Point(225,680), Point(325,640))    # Creating the QUIT button
        self.quit_button.setFill("Red")                                # Setting the color of the QUIT button
        self.quit_button.draw(self.win)                # Drawing the QUIT button onto the window / interface
        
        self.quit_button_text = Text(Point(275,660), "QUIT")    # Displaying/Creating the "QUIT" text in the button (and centered in the middle of the button)
        self.quit_button_text.setSize(24)           # Setting the size of the font/text
        self.quit_button_text.draw(self.win)    # Drawing / Displaying the text onto the window / interface
        
        self.reset_button = Rectangle(Point(225,630), Point(325,590))   # Creating the RESET button
        self.reset_button.setFill("Blue")                           # Setting the color of the RESET button
        self.reset_button.draw(self.win)               # Drawing the QUIT button onto the window / interface
        
        self.reset_button_text = Text(Point(275,610), "RESET") # Displaying/Creating the "RESET" text in the button (and centered in the middle of the button)
        self.reset_button_text.setSize(24)              # Setting the size of the font/text
        self.reset_button_text.draw(self.win)  # Drawing / Displaying the text onto the window / interface   
        
    def quit_game(self):
    """
    Purpose: This function will quit the game when the QUIT button is clicked, will also update the Mouse Status, then wait for a mouseclick and will then close the entire game completely
    """
        self.mouse_status.setText("BYE BYE !!")     # This will update the text of the mouse status to "BYE BYE!!" once the button has been clicked
        self.mouse_status.setSize(21)           # Setting the text of the font/text
        self.win.getMouse()                     # Waiting for mouse click
        self.win.close()                     # Once a mouse click has been detected, it will close the window
        
    def reset_game_board(self):
    """
    Purpose: Resets the gameboard; as well as the Player Position back to their origininal starting positions and as well as the Player Statuses. 
    
    Parameter: None
    Results: None
    """
        self.board.reset_board()                # Will call the rest_board function
        self.mouse_status.setText("RESET")      # Updates the text of the mouse status to "RESET" once its been clicked
        self.mouse_status.setSize(21)           # Setting the size of the font/text
        
        #self.player0.position_player_reset_org(Point(45,45))
        #self.player1.position_player_reset_org(Point(495,495))
        
       # Moves Player0 back to it's original starting position on the gameboard (Position 0,0), and moves Player1 back to its original starting position on the gameboard (Position 5,5)
       
        self.player0.move_player(0,0)       
        #self.player1.move_player(5,5)
        self.player1.move_player(self.width -1 , self.height - 1)   # This makes sure that Player1 is moved back to its orignal spot (5,5) as the gameboard dimesnions are 6x6, so one less in width and height will ensure it moves back to spot (5,5) - its oringinal spot
        
        self.current_player = self.player0                      # Sets Player0 as the current player
        self.player_status.setText(f"Player 0: (0,0)\nMove")    # Updates the player status text to display and indicate the player (Player 0), it's location on the board, which initally will be its tarting position (0,0) then its task, which will also initially be "Move"
        
        self.player_action = "Move"          # Sets the players action / task to "MOVE"
            
    def switch_players(self):
    """
    Purpose: To switch the current player (because later once one player has Moved and Broken Ice, it will be the next players turn, so we have to switch the current player in order for them to be able to perform their neccessary tasks"
    
    Parameter: None
    Results: None
    """
        if self.current_player == self.player0:
            self.current_player = self.player1
        else:
            self.current_player = self.player0
            
        
    def is_ice_block_occupied(self, column, row, point_clicked):
    """
    Purpose: This method will check to see if the iceblock at the specific point clicked (column,row) or coordinate, is occupied by a player, or has already been broken. Or simply, just checking whether the ice_block is occupied in any way (either broken or player present on it)
    
    Parameters:
    int - In this case it will be the column index value of the iceblock and row index value of the iceblock which of both are integer values 
    
    Point - This is the point_clicked as this is where the mouse is clicked on the gameboard (and later is turned into index values / coordinates seen later in the code)
    
    Returns: bool - THis function will return True if either the iceblock has already been broken, or even if the iceblock is currently occupied by a player, indicating that the iceblock is currently occupied. It will return False if neither of these are true. 
    """
    
    # Calculates the x_coord (column) index value of the iceblock clicked, and as well as the y_coord (row_ index value of the iceblock clicked 
    
        x_coord = int(point_clicked.getX() // 90)
        y_coord = int(point_clicked.getY() // 90)
    
    # Retreives the colour of the ice_block at the specific iceblock clicked
        ice_block_colour = self.board.ice_blocks[row][column].config["fill"]
    
    # If the colour of the iceblock is not Grey, that means that the iceblock is occupied (broken)   
        if ice_block_colour != "Grey": 
            return True
            
    # Calculating the x_coord index value of Player0 based on it current position, and calculating the y_coord index value of Player0 based on its current position   
    
        x_coord_p0 = int(self.player0.player_symbol.p1.getX() // 90)
        y_coord_p0 = int(self.player0.player_symbol.p1.getY() // 90)
    
    # Calculating the x_coord index value of Player1 based on it current position, and calculating the y_coord index value of Player1 based on its current position
    
        x_coord_p1 = int(self.player1.player_symbol.p1.getX() // 90)
        y_coord_p1 = int(self.player1.player_symbol.p1.getY() // 90)
    
    # This will check to see if the current position of Player0 is equal to the point clicked, if it is, it will return True indicatng that the point clicked is indeed occupied by a player (in this case to check for Player0)
    
        if x_coord_p0 == x_coord and y_coord_p0 == y_coord:
            return True 
            
    # This will check to see if the current position of Player0 is equal to the point clicked, if it is, it will return True indicatng that the point clicked is indeed occupied by a player (in this case to check for Player1)   
    
        if x_coord_p1 == x_coord and y_coord_p1 == y_coord:
            return True
            
     # Else we return False if the iceblock is neither broken or occupied by a player    
        return False
             
    
    def play(self):
    """
    Purpose: This function/ method implements the entire game logic and functionality of the game; and is also called to start the game itself. It will deterine whether certain buttons have been clicked and display their according message, will also display the Mouse Status and Player Status as the game runs accordingly. It will determine the winner, switch the players, etc. As mentioned, it implements the entire game logic and functioanlity to able to proeprly play/run the game. 
    
    Paramter: None
    Results: None
    """
        
        while True:
            
            # Storing the current players position as a variable
            position = self.current_player.position
            
            
            
        
            point_clicked = self.win.getMouse()          # This stores a mouse click as a variable
            row = int(point_clicked.getY() // 90)        # Calculates the row index of the ice_block based off of the Y-coordinate of the point clicked (and is turned into a coordinate/index value by //90)
            column = int(point_clicked.getX() // 90)    # Calculates the row index of the ice_block based off of the Y-coordinate of the point clicked (and is turned into a coordinate/index value by //90)
            
            
            # This if statement will check if the quit button is clicked, and will call the quit_game function/emthod
            
            if 225 <= point_clicked.getX() <= 325 and 640 <= point_clicked.getY() <= 680:
                self.quit_game()
                return
            
            
            # This if statement will check if the reset button is clicked, if it is it will call the reset_game_board function/method
            
            elif 225 <= point_clicked.getX() <= 325 and 590 <= point_clicked.getY() <= 630:
                self.reset_game_board()
            
            # This checks to see if the point that is clicked is within the Game Board dimesnions (not the window, but the gameboard, because anything clicked outside of game board bourndires is invalid aside from the quit and reset button)
            
            elif self.is_click_in_grid(point_clicked):
                is_occupied = self.is_ice_block_occupied(column,row, point_clicked) # Checks to see whether the iceblock is occupied, and we store the bool answer as a variable
                
            # This will obtain the row index of the current players position
            
                p_row = int(self.current_player.position.getY() // 90)
                
            # This will obtain the column index of the current players position
                p_column = int(self.current_player.position.getX() // 90)
                
            # This checks to see whether the spot that player wants to move / point that is clicked is adjacent to the current players position
            
                is_adj = self.board.move_validity_checker(column, row, (p_column, p_row))
                
            # This if  statement will check if the spot that the player wnats to move to is not occupied, and is adjecent to the player (when their current action / task is to Move 
            
                if self.player_action == "Move" and not is_occupied and is_adj:
                    if self.board.ice_blocks[row][column].config["fill"] != "White":    # This checks if the clicked ice block is not broken, if it is not, it will proceed to move the player to the desired and valid spot 
                        
                        # Moves the current player to the clicked position after validation
                        self.current_player.move_player(row, column)
                        
                        # Now the players task becomes "Break Ice"
                        self.player_action = "Break Ice"
                        
           # These few if, and else statements will update the Player Status text and mouse status text accodingly 
                    
                        if self.current_player == self.player0:
                            self.player_status.setText(f"Player 0: [{column},{row}]\n{self.player_action}")
                        else:
                            self.player_status.setText(f"Player 1: [{column},{row}]\n{self.player_action}")
                        
                        self.mouse_status.setText(f"({column}, {row})")
                    else:
                        self.mouse_status.setText("NOT VALID")
                    #self.status_message_updated("BREAK ICE", self.current_player.position, "")
                    
                
            # This will check to see when the Players Current Action / Task is to Break Ice, and the ice block that is clicked is NOT occupied, it will execute accordingly
            
                elif self.player_action == "Break Ice" and not is_occupied:
                    self.board.break_ice(column, row)         # Breaks the Ice at the clicked position
                    self.switch_players()   # Will now switch the player after the current player has Moved and Broken an Ice Block
                    self.player_action = "Move"     # After switching players, the players current action is now to move again
                    
                    
                    p_row = int(self.current_player.position.getY() // 90)  # Will grab the row index value of the current position of the player 
                    p_column = int(self.current_player.position.getX() // 90)   # Will grab the column index value of the current position of the player
                    
                    
                    # This will update the player status and mouse status accordingly
                    
                    if self.current_player == self.player0:
                        self.player_status.setText(f"Player 0: [{p_column},{p_row}]\n{self.player_action}")
                    else:
                        self.player_status.setText(f"Player 1: [{p_column},{p_row}]\n{self.player_action}")
                    
                       
                    self.mouse_status.setText(f"({column}, {row})")
                    
                    
                else:
                    self.mouse_status.setText("NOT VALID")
            else:
                self.mouse_status.setText("NOT VALID")
                
            # This will now start to determine the winner of the Game. We call the determine_winner function/method to dtermine the winner, and store the value of the returned winner.
            
            game_winner = self.determine_winner()
            
            # If there is a winner of the game, this will execute, and will display the text "GAME OVER!! {whichever play has won, determined from the determine_winner function} HAS WON". This will just display the winner and the message in the mouse status, that the game is over and which player has won
            
            if game_winner:
                self.mouse_status.setText(f"GAME OVER !!\n {game_winner} HAS WON")
                #self.score_screen_creation(game_winner)
                
                # This will call the score_screen_creation method (window) after the game is completed and handle the players choice, and the returned player choice is stored as a varibale that will determine what the next process is after the game is completed
                
                game_results = self.score_screen_creation(game_winner)
                
                # If the returned user's choice was to "Restart Game' it will call the restart_game_board function and restart the game/board so that we can start playing again
                
                if game_results == "Restart Game":
                    self.reset_game_board()
                    
                # If the returned user's choice was "No Thanks", it will call the quit_game function that will close the window and game 
                
                elif game_results == "No Thanks":
                    self.quit_game()
                
                
    
    def player_creations(self):
    """
    Purpose: This will create the player objects for each player (game piece/ player piece / player board piece)
    
    Paramater: None
    Results: None
    """
        block_size = 90   # This is the size of each iceblock in pixels, and we store that value in a variable
        
        position_of_p0 = Point(45,45)       # This will store the initali position of Player0 in a variable,  and will also set the initial position of Player0
        
        # We call the Player Class to help draw/create the player (will create an instance of Player for Player0). It will display the specific properties. (Name, Colour, Position) of each Player. Each player will have a specific Name, Colour that Assosciates to the Player, and the Position of that player.
        
        player0 = Player(self.win, 'Player 0 ', 'Green', position_of_p0)
        #player0.draw
        
        # We call the Player Class to help draw/create the player (will create an instance of Player for Player1). It will display the specific properties: (Name, Colour, Position) of the player. Each player has a specific Name, Colour that Assosciates to the Player, and the Position of that player.
        
        position_of_p1 = Point(495, 495)
        player1 = Player(self.win, "Player 1", "Yellow", position_of_p1)
        #player1.draw()
        
        # Returns the instances of Player 0 and Player 1
        return player0, player1
    
    def is_click_in_grid(self, click_location):
    """
    Purpose: The purpose of this function/method is to idenitfy whether a mouseclick is within the gameboard boundries (within the actual gameboard and not outside of it)
    
    Parameter: Point - the click_location which is the location of the mouse click
    Returns: bool - This will retun True if the mouse click is within the game board boundries. Otherwise False
    """
        
        return 0 <= click_location.getX() <= 540 and 0 <= click_location.getY() <= 540
    
    def determine_winner(self):
    """
    Purpose: This purpose of this function is to determine the winner of the game based on whether the player make a valid move. A winner is decided when the opposing player is surrounded or enclosed and not able to make a valid move
    
    Paramter: None
    Results: str - returns the name of the Player that has won! 
    """
    
    # This for loop will iterate through each player in the game
        for player in [self.player0, self.player1]:
            if not player.can_move(self.board):     # Checks to see if the player can make a valid move
                if player == self.player0:      # If the player that cannot make the move is Player 0, Player 1 is determined the winner. 
                    #self.player1_score += 1
                    return self.player1.name
                else:                           # Else we return Player 0 as the winner
                    #self.player0_score += 1
                    return self.player0.name
              
    def score_screen_creation (self, game_winner):
    """
    Purpose: The purpose of this is that when a game round ends, a score screen should be displayed that shows the current total score of each player, and prompts the users to either terminante the game completely or start another round
    
    Paramter: str - This is the game_winner; which is the name of the player who has won the current round/game
    """
    
    # This will create a seperate the GraphWin obect Window after the game has ended. The window will have these specific attributes. The Name of the GraphWin, how big the display / window will be, the Backround of the screen customized to our liking and then the buttons and text.
    
        self.score_screen_win = GraphWin("Icebreaker Game Score", 400, 300)
        self.score_screen_win.setBackground("Cyan")
        
    # Creating a counter for each player, so that everytime a game/round has ended, the player than has won will gain a point everytime, and the total accumalated wins will keep displaying for each player. 
    
        if game_winner == self.player0.name:        # If Player 0 wins, add one win to his counter each time
            self.player0_score += 1 
        else:
            self.player1_score += 1                 # if Player 1 Wins, add one win to his counter each time
        
        # This will display the game score for both players on the score screen at the end. The format our our end screen should be as the Following. A Title that says "Game Score" then underneath it will display the score for each player
        
        game_score_txt = Text(Point(200,70), "Game Score:") # Displaying the text "Game Score" at the top 
        player0_text = Text(Point(200, 90), f"Player 0: {self.player0_score}")  # Displaying the Player, then their associated score. In this case it will be Player 0: {Player 0's Score}. Just undernearth the "Game Score" text
        
        player0_text.draw(self.score_screen_win)     # Draw the Player 0 text onto the window to display it
        game_score_txt.draw(self.score_screen_win) # Draw the "Game Score" text onto the window to display it 
        
        # Same process that was done for Player0 is done for Player1, and the text for Player1 is located just underneath the Player 0 text.
        
        player1_text = Text(Point(200, 120), f"Player 1: {self.player1_score}")
        player1_text.draw(self.score_screen_win)
        
        # Creating the "Next Round" Button
        next_round_button = Rectangle(Point(100,170), Point(180,220))   # Creating the button onject via Rectangle object
        next_round_button.setFill("Pink")   # Setting the colour of the button to our liking
        next_round_button.draw(self.score_screen_win)   # Drawing the button onto the window to display it
        
        # Creating the text "Next Round" which is located in the middle of the button to indicate that its that specific button. Then drawing it to display it onto the window
        
        next_round_button_txt = Text(Point(140,195), "Next Round")
        next_round_button_txt.draw(self.score_screen_win)
        
        # Same process done for the 'Next Round' button done for the 'No Thanks' Button
        no_thanks_button = Rectangle(Point(220,170), Point(300,220))
        no_thanks_button.setFill("Purple")
        no_thanks_button.draw(self.score_screen_win)
        
        no_thanks_button_txt = Text(Point(260,195), "No Thanks")
        no_thanks_button_txt.setSize(16)
        no_thanks_button_txt.draw(self.score_screen_win)
    
    # This will handle the user choice if they'd like to start another round, or if they'd like to quit the game completely
    
        while True:
            point_clicked = self.score_screen_win.getMouse()    
            
            # If the "Next Round" button is clicked it will return 'Restart Game' which then will be used in the play() function when after the game has ended and a winner has been determined it will pop up this score screen window, if the user's choice is to Play another round of the Game it will return 'Restart Game", and if the return value is "Restart Game" it will completely start the game (as its called in the play() function in Icebreaker at the end)
            
            if 100 <= point_clicked.getX() <= 180 and 170 <= point_clicked.getY() <= 220:
                self.score_screen_win.close()
                return "Restart Game"
                
            # If the "No Thanks" button is clicked it will return 'No Thanks' which then will be used in the play() function when after the game has ended and a winner has been determined it will pop up this score screen window, if the user's choice is to stop playing the Game it will return "No Thanks", and if the return value is "No Thanks" it will completely quit the game (as its called in the play() function in Icebreaker at the end)
            
            elif 220 <= point_clicked.getX() <= 300 and 170 <= point_clicked.getY() <= 220:
                self.score_screen_win.close()
                return "No Thanks"            
    
class Board:
"""
Purpose: This class contains the game board: a two dimensionsal list of list of board squares. 
Parameter: None
Return: None
"""
    
    def __init__ (self, win, width, height):
    '''
    Purpose: Initalize the board attributes, including a two-dimesnional list of list of board squares, and pretty much initalizes an instance of the Board class.
    
    Parameters:
    > win - the GraphWin object neccessary for displaying the iceblcoks, and game window, and all shape creations, etc.
    > int - the Width and Height of the board neccessary to create the actual X*Y board (Ex. 6x6 board 5x7 Board, etc. In this case our board game is a 6x6)
    
    Return: None
    '''
    
        self.width = width          # Initalizes the width of the gameboard
        self.height = height        # Initalizes the height of the gameboaard
        self.win = win               
        self.draw_board()   # Initalizes the draw_board method / calls the method to draw the iceblocks/gameboard
    
    def draw_board(self):
    '''
    Purpose: This method will create the iceblocks, to create the gameboard, then once that is done, this will draw the game board with consists of iceblocks
    
    Paramater: None
    Returns: None
    '''
    
        block_size = 90     # The size of each iceblock is 90 pixels, and storing that as a variable
        self.ice_blocks = []    # Creating an empty outer-list so that it Initalizes the two-dimensional list to store the ice_blocks (so it can become a list of lists)
        
        # For loop to iterate through each row in the game board
        for row in range(self.height):
            inner_list = []
            for column in range(self.width): # Iterates through each column in the gameboard
            
            # This will calculate the coordinate for each of the iceblocks, and then create the sqaure shape / ice-block shape via the Rectangle object
            
                x1 = column * block_size 
                y1 = row * block_size
                x2 = x1 + block_size
                y2 = y1 + block_size
                ice_block = Rectangle(Point(x1,y1), Point(x2,y2))
                
                # Appending the ice blocks that have been created to the inner_list
                inner_list.append(ice_block)
               
                # Drawing the ice blocks onto the game window
                ice_block.draw(self.win)
                ice_block.setFill("Grey")       # Setting the color of the Iceblocks
                ice_block.setOutline("Black")   # Setting the border/outline of the blocks to black for visability
                
            self.ice_blocks.append(inner_list)  # Appends the inner list of the ice blocks to main/outer list (to fully create the two-dim list / list of list)
        
    def break_ice(self, column, row):
    '''
    Purpose: To simply the break the ice block at the given coordinates 
    Paramater: int - The Column Index and Row Index (integers) of the given coordinates of the block that wants to be broken 
    Returns: None
    '''
        
        # This will change the colour (filling the colour) of the iceblock at the given coordinates to white, indicating that the block of ice has been broken.
        
        self.ice_blocks[row][column].setFill("White")
        
            
    def reset_board(self):
    '''
    Purpose: This will reset the entire game board, to how it initally was, clearing all broken ice blocks, and reseeting them to be filled again / reset
    
    Parameter: None
    Results: None
    '''
        
        block_size = 90                     # The size of each block 
        
        # This will iterate through each row in the gameboard
        for row in range(self.height):
            for column in range(self.width):       # This will iterate through each column in the gameboard
                self.ice_blocks[row][column].setFill("Grey")   # This will set all of the iceblocks to the colour grey by filling all of the iceblocks to make sure the board has been completely reset
                
        #self.draw_board()
        
        
    def move_validity_checker(self, column, row, current_position):
    '''
    Purpose: This function will check the validity, and determine if the movement to a specificed position on the game board is valid - this mainly checks to see if the wanted movement is adjacent to the current position of the player
    
    Paramater:
    int - The column index value of the target position / coordinate / ice block, and as well as the row index value of the target position / coordinate / ice block. 
    tuple - The current_position of the player is a Tuple (coordinate) - Ex. (1,2), (1,3), etc... or (current_x, current_y)
    
    Returns: bool - If the move to the wanted spot is valid, it will return true, otherwise will return False
    '''
        # This grabs the according x_coord and y_coord by taking the first index position of the current position (which should be a tuple) which associates the x-coord then the second index position which associates to the y_coord
        
        current_x, current_y = current_position[0], current_position[1]
        
        # This if statement checks to see if the spot that the player wants to move to, is the same as the current position the player is on, if it is, it would return False as thats not a valid move
        
        if row == current_y and column == current_x:
            return False
            
    # This will check to see if target position is within the boundries of the gameboard
        if 0 <= row < self.height and 0 <= column < self.width:
        
    # Simple calculations to checks to see if the spot that the player wants to move to is adjecent to the current position it's currently at
    
            if -1 <= abs(row - current_y) <= 1 and -1 <= abs(column - current_x) <= 1:
                return True 
                ##return (row, column) not in self.ice_blocks
        return False
                                                            
                                                            
                                                                     
class Player:
"""
Purpose: This class contains the information for one of the players (which can then be used for both players), in which is determines it determines whether a mouse click is on the player, actually moving the player itself, and ressetiing players to their original spot. So in simple terms, it just contains the informtation regarding player attributes

Paramter: None
Results: None
"""

    
    def __init__(self, win, name, colour, position):
    '''
    Purpose: Initalizes the player attributes (game piece, position, player composition, player movements etc) - and just initalizing an instance of the Player class. 
    
    Parameter:
    GraphWin (win) - This is the window, which is neccessary for displaying player symbols and such
    str - The name of the Player, and as well as the colour of the Player
    Point - Which is the initial position of the player's game piece 
    
    Return: None
    '''
        self.win = win
        self.position = position
        self.name = name
        self.colour = colour
        #self.draw()
        
        # This creates and draws the player's game piece as a circle, with it's specific attributes (colour, position (initial position) and radius)
        
        self.player_symbol = Circle(self.position, 30)
        self.player_symbol.setFill(self.colour)
        self.player_symbol.draw(self.win)        
        
        
    def player_clicked (self, point):
    '''
    Purpose: Determines whether a mouse click is on the player 
    Parameter: point - the coordinates of the point clicked
    Results: bool - will return True if the players symbol si clciked, and False if it is not
    '''
    
    # This retrieves the coordinates of the current position of the players symbol, and as well as the coordinates of the position / point that is clicked 
    
        player_center_x_coord = self.position.getX()
        player_center_y_coord = self.position.getY()
        mouse_click_x_coord = point.getX()
        mouse_click_y_coord = point.getY()
        
        # This will calculate the boundries of the player's symbol
        center_to_right_side_circle = player_center_x_coord + 30
        left_side_to_circle_center = player_center_x_coord - 30
        
        top_portion_of_circle = player_center_y_coord - 30
        bottom_portion_of_circle = player_center_y_coord + 30
        
        # Now that we created the players boundries with the radius of the circle and determinaing the overall boundry of the circle (players symbol) we can go through to check if the point that is clciked lies within the players boundry, if it lies within the players boundry it would return True indicating that the point clicked is on the player as its within its boundry, if notm would return False
        
        if left_side_to_circle_center <= mouse_click_x_coord <= center_to_right_side_circle and top_portion_of_circle <= mouse_click_y_coord <= bottom_portion_of_circle:
            return True
        else:
            return False
    
    def move_player(self, row, column):
    '''
    Purpose: Moves the player to the given board coordinates
    
    Parameters: int - Both the row index value and the column index value (integers) of the target position / ice block that the player is wanting to move to.
    
    Returns: bool - Returns True if the player's game piece is successfully moved to the target position, otherwise it would return False
    '''
        
        # This simple calculation, calculates the chnage in x and y coordinates based on the difference (delta/chnage in) the target position (spot that the player wants to move to) and the current position of the player's game piece / symbol
        
        change_in_x = int(column - self.position.getX() // 90) * 90
        change_in_y = int(row - self.position.getY() // 90) * 90
        
        # Moves the player's game piece / symbol with the caclulated / delta coordinates (chnage in x and y coords)
        
        self.player_symbol.move(change_in_x, change_in_y)
        self.position = self.player_symbol.getCenter()          # This updates the position of players game piece / symbolt to the new position that the player has moved to 
        
        return True 
            
        
    def can_move(self, board):
    '''
    Purpose: Determines whether a player can make a valid move. This method is also used to determine when a player has lost (which is implemneted and constructed in the play() function in the Icebreaker class)
    
    Paramater: Board - The Board object representing the game board. Uses the instance of the Board Class to help in determining if a player can make a valid move / determine when a player has lost and if they can make a valid move
    
    Returns: bool - Returns True if the player can make a valid move to any adjacent position, otherwise False
    '''
        
    # This retreives the x and y coordinate of the player's current position
        xcoord_player, ycoord_player = int(self.position.getX() // 90), int(self.position.getY() // 90)
        
        # FOr loop to iterate throuhg the adjacent positions around the player's current position
        for x_adj_positions in range (-1,2):
            for y_adj_positions in range (-1,2):
                
    # This will calculate the coordinaates of the adjacent position
                adj_x_coord , adj_y_coord = xcoord_player + x_adj_positions, ycoord_player + y_adj_positions
    
    # This will just skip the current position 
    
                if adj_x_coord == xcoord_player and adj_y_coord == ycoord_player:
                    continue
    # This checks to see if the adjacent position is within the game board boundries
                if 0 <= adj_x_coord < board.width and 0 <= adj_y_coord < board.height:
    # This checks to see if the ice block at the adjacent position is not "White" (which means that it has not been broken yet)
                    if board.ice_blocks[adj_y_coord][adj_x_coord].config["fill"] != "White":
                        return True
                       
        return False
    
    def position_player_reset_org(self, position):
    """
    Purpose: The function of this method is to simply reset the players back to its original position on the gameboard 
    
    Parameter: Point - the "position" is the point where the player' symbol / game piece should move to once its been reset
    
    Returns: None
    """
    
        self.position.undraw()          # Undraws the current position of the player's game piece/symbol
        self.position = position        
        self.draw()                     # Redraws the player's symbol at the new position (to the original/initial)
        
    
def splash_screen_creation():
'''
Purpose: When the game starts, a splashscreen should be dispayed, showing the Games Title, Name, and some additional information about the game in general. There's also two bottons present called "Play Game" and "No Thanks" that when clicked will execute their according functionality, either to start the game if "Play Game" is clicked and to "Quit" or "Close" the window if "No Thanks" is clicked

Paramater: None
Results: None
'''

# Creating the GraphWin object / window for the splashscreen, and customizing the backround colour to our liking
    splash_screen_win = GraphWin("Vickram's Icebreaker - Splashscreen", 400, 300)
    
    splash_screen_win.setBackground("LightCyan")
    
    # This Displays the introductory text, where the Game's Title is Mentioned, Name, and some additional information. 
    
    splash_screen_intro_text = Text(Point(200,70), "Welcome to the Icebreaker Game.\nThis game is written in part by Vickram Gill\nfor CMPT 103, Winter Session 2024")
    
    
    splash_screen_intro_text.setSize(17)                # Setting the size of the font/text
    splash_screen_intro_text.draw(splash_screen_win)    # Drawing the text onto the window
    
    want_to_play_txt = Text(Point(200,140), "Do you want to play?") # Prompting a message "do you want to play? So that then the player can either proceed to play the game or not"
    
    want_to_play_txt.setSize(17)            # Setting the size of the font/text
    want_to_play_txt.setStyle("bold")       # Setting the style to "Bold" so the text appears bolded just for visual appearance / visability
    want_to_play_txt.draw(splash_screen_win)    # Drawing the text onto to the graphwin / window
    
    # Creating the "Play Game" Button and displaying the text for the button 
    play_game_button = Rectangle(Point(100,170), Point(180,220))
    play_game_button.setFill("LightGreen")      
    play_game_button.draw(splash_screen_win)
    
    play_game_button_txt = Text(Point(140,195), "Play Game")
    play_game_button_txt.setSize(16)
    play_game_button_txt.draw(splash_screen_win)
    
    # Creating the "No Thanks" Button and displaying the text for the button
    no_thanks_button = Rectangle(Point(220,170), Point(300,220))
    no_thanks_button.setFill("LightCoral")
    no_thanks_button.draw(splash_screen_win)
    
    no_thanks_button_txt = Text(Point(260,195), "No Thanks")
    no_thanks_button_txt.setSize(16)
    no_thanks_button_txt.draw(splash_screen_win) 
    
    # While Loop to check / wait for a user click / interaction; that also determines whether the 'Play Game" button was clicked or the "No Thanks" button was clicked, and will excute accordingly to the button that is clicked
    
    while True:
        point_clicked = splash_screen_win.getMouse()
        
        # If the user's mouse click / point that is clicked is within the boundries of the "Play Game" button (or simply if the Play Game button is clicked) it will excute to close the splashscreen, and return "Play Game". This returned value is then used within the main() function where if the returned value is "Play Game" it will start the game, by calling the Icebreaker class (seen in the main() function )
        
        if 100 <= point_clicked.getX() <= 180 and 170 <= point_clicked.getY() <= 220:
            splash_screen_win.close()
            return "Play Game"
        
        # If the user's mouse click / point that is clicked is within the boundries of the "No Thanks" button (or simply if the Play Game button is clicked) it will excute to close the splashscreen, and return "No Thanks". This returned value is then used within the main() function where if the returned value is "No Thanks" it will return none, and just simply close the splashscreen.
        
        elif 220 <= point_clicked.getX() <= 300 and 170 <= point_clicked.getY() <= 220:
            splash_screen_win.close()
            return "No Thanks" 
    
    
# Testing Function to start the game / run the code via Main Function          
def main():
    
    player_choice = splash_screen_creation()
    
    if player_choice == "Play Game":
        game = Icebreaker(6, 6) 
        game.play()
        
    elif player_choice == "No Thanks":
        None
        
    
if __name__ == "__main__":
    main()
--------------------------------------------------------------------------------

Brief Description on How the "Icebreaker Game" is played / Game Rules

1. Once our game has started, our player that starts the game is Player 0 (Green Circle)
2. We're prompted to move our player in a position that is adjacent (can move up, dowm, left, right, diagonally

3. So our first main step is to move the Player to any valid position (failure to make a valid move will display a "NOT VALID" message, but you have as mnay attempts to make a valid move. 

4. Once we've moved our player, when then have to break and iceblock 

5. Break any iceblock that has not yet been broken, and an iceblock where a player is not present. In a result of clicking in a invalid position to break an iceblock (block that is occupied  or broken), you'll be prompted with the message "NOT VALID", but you have as mnay attempts to make a valid break ice move.

6. Once we've broken our Iceblock, its now the second players turn 

7. The second player (Player 1) now has to go through the sam process, making a valid move and and valid ice break move

8. The goal of this game is to enclose the opponents so they're no longer able to make a valid move, ineventiablly making the player thats no longer able to move, the loser, and the other player, the winner. 

