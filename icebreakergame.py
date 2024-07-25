from graphics import GraphWin, Rectangle, Point, Text, Circle


class Icebreaker:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = GraphWin("Vickrams Icebreaker Game- Version 1.0 - March-03-26", 550, 775)
        self.player0_score = 0
        self.player1_score = 0
        #self.mouse = Text(Point(100, 615), "Mouse") 
        #self.mouse.setSize(21)
        #self.mouse.setOutline("Orange")
        #self.mouse.draw(self.win)
        self.board= Board(self.win, width, height)
        self.player0, self.player1 = self.player_creations()
        self.current_player = self.player0                  
        self.button_creations()
        self.player_action = "Move"
       
        
        self.mouse_status = Text(Point(100,665), "")  
        self.mouse_status.setSize(16)
        self.mouse_status.setOutline("Pink")
        self.mouse_status.draw(self.win)
        
        self.player_status = Text(Point(100, 610), f"Player 0: (0,0)\nMove")
        self.player_status.setSize(16)
        self.player_status.setOutline("Pink")
        self.player_status.draw(self.win)
       
    def button_creations(self):
        self.quit_button = Rectangle(Point(225,680), Point(325,640))
        self.quit_button.setFill("Red")
        self.quit_button.draw(self.win)
        
        self.quit_button_text = Text(Point(275,660), "QUIT")
        self.quit_button_text.setSize(24)
        self.quit_button_text.draw(self.win)
        
        self.reset_button = Rectangle(Point(225,630), Point(325,590))
        self.reset_button.setFill("Blue")
        self.reset_button.draw(self.win)
        
        self.reset_button_text = Text(Point(275,610), "RESET")
        self.reset_button_text.setSize(24)
        self.reset_button_text.draw(self.win)
        
    def quit_game(self):
        self.mouse_status.setText("BYE BYE !!")
        self.mouse_status.setSize(21)
        self.win.getMouse() 
        self.win.close()
        
    def reset_game_board(self):
        self.board.reset_board()
        self.mouse_status.setText("RESET")
        self.mouse_status.setSize(21)
        
        #self.player0.position_player_reset_org(Point(45,45))
        #self.player1.position_player_reset_org(Point(495,495))
        
        self.player0.move_player(0,0)
        #self.player1.move_player(5,5)
        self.player1.move_player(self.width -1 , self.height - 1)
        
        self.current_player = self.player0
        self.player_status.setText(f"Player 0: (0,0)\nMove")
        self.player_action = "Move"
            
    def switch_players(self):
        if self.current_player == self.player0:
            self.current_player = self.player1
        else:
            self.current_player = self.player0
            
        
    def is_ice_block_occupied(self, column, row, point_clicked):
        x_coord = int(point_clicked.getX() // 90)
        y_coord = int(point_clicked.getY() // 90)
        
        ice_block_colour = self.board.ice_blocks[row][column].config["fill"]
        
        if ice_block_colour != "Grey": 
            return True
        
        x_coord_p0 = int(self.player0.player_symbol.p1.getX() // 90)
        y_coord_p0 = int(self.player0.player_symbol.p1.getY() // 90)
        
        x_coord_p1 = int(self.player1.player_symbol.p1.getX() // 90)
        y_coord_p1 = int(self.player1.player_symbol.p1.getY() // 90)
        
        if x_coord_p0 == x_coord and y_coord_p0 == y_coord:
            return True 
        
        if x_coord_p1 == x_coord and y_coord_p1 == y_coord:
            return True
        
        return False
             
    
    def play(self):
        
        while True:
            
            position = self.current_player.position
            
            #self.status_message_updated("MOVE PIECE", position, "")
            
            
            point_clicked = self.win.getMouse() 
            row = int(point_clicked.getY() // 90)
            column = int(point_clicked.getX() // 90)
                
            if 225 <= point_clicked.getX() <= 325 and 640 <= point_clicked.getY() <= 680:
                self.quit_game()
                return
            
            elif 225 <= point_clicked.getX() <= 325 and 590 <= point_clicked.getY() <= 630:
                self.reset_game_board()
                
            elif self.is_click_in_grid(point_clicked):
                is_occupied = self.is_ice_block_occupied(column,row, point_clicked)
                
                
                p_row = int(self.current_player.position.getY() // 90)
                p_column = int(self.current_player.position.getX() // 90)
                
                is_adj = self.board.move_validity_checker(column, row, (p_column, p_row))
                
                if self.player_action == "Move" and not is_occupied and is_adj:
                    if self.board.ice_blocks[row][column].config["fill"] != "White":
                        
                        self.current_player.move_player(row, column)
                        
                        self.player_action = "Break Ice"
                    
                        if self.current_player == self.player0:
                            self.player_status.setText(f"Player 0: [{column},{row}]\n{self.player_action}")
                        else:
                            self.player_status.setText(f"Player 1: [{column},{row}]\n{self.player_action}")
                        
                        self.mouse_status.setText(f"({column}, {row})")
                    else:
                        self.mouse_status.setText("NOT VALID")
                    #self.status_message_updated("BREAK ICE", self.current_player.position, "")
                    
                
                
                elif self.player_action == "Break Ice" and not is_occupied:
                    self.board.break_ice(column, row)
                    self.switch_players()
                    self.player_action = "Move"
                    
                    p_row = int(self.current_player.position.getY() // 90)
                    p_column = int(self.current_player.position.getX() // 90)
                    
                    if self.current_player == self.player0:
                        self.player_status.setText(f"Player 0: [{p_column},{p_row}]\n{self.player_action}")
                    else:
                        self.player_status.setText(f"Player 1: [{p_column},{p_row}]\n{self.player_action}")
                    
                       
                    self.mouse_status.setText(f"({column}, {row})")
                    
                    
                else:
                    self.mouse_status.setText("NOT VALID")
            else:
                self.mouse_status.setText("NOT VALID")
                
                   
            game_winner = self.determine_winner()
            
            if game_winner:
                self.mouse_status.setText(f"GAME OVER !!\n {game_winner} HAS WON")
                #self.score_screen_creation(game_winner)
                
                game_results = self.score_screen_creation(game_winner)
                
                if game_results == "Restart Game":
                    self.reset_game_board()
                elif game_results == "No Thanks":
                    self.quit_game()
                
                
    
    def player_creations(self):
        block_size = 90
        position_of_p0 = Point(45,45)
        player0 = Player(self.win, 'Player 0 ', 'Green', position_of_p0)
        #player0.draw
        
        position_of_p1 = Point(495, 495)
        player1 = Player(self.win, "Player 1", "Yellow", position_of_p1)
        #player1.draw()
        
        return player0, player1
    
    def is_click_in_grid(self, click_location):
        
        return 0 <= click_location.getX() <= 540 and 0 <= click_location.getY() <= 540
    
    def determine_winner(self):
        for player in [self.player0, self.player1]:
            if not player.can_move(self.board):
                if player == self.player0:
                    #self.player1_score += 1
                    return self.player1.name
                else:
                    #self.player0_score += 1
                    return self.player0.name
              
    def score_screen_creation (self, game_winner):
        self.score_screen_win = GraphWin("Icebreaker Game Score", 400, 300)
        self.score_screen_win.setBackground("Cyan")
        
        if game_winner == self.player0.name:
            self.player0_score += 1
        else:
            self.player1_score += 1
        
        game_score_txt = Text(Point(200,70), "Game Score:")
        player0_text = Text(Point(200, 90), f"Player 0: {self.player0_score}")
        player0_text.draw(self.score_screen_win)
        game_score_txt.draw(self.score_screen_win)
        
        player1_text = Text(Point(200, 120), f"Player 1: {self.player1_score}")
        player1_text.draw(self.score_screen_win)
        
        next_round_button = Rectangle(Point(100,170), Point(180,220))
        next_round_button.setFill("Pink")
        next_round_button.draw(self.score_screen_win)
        
        next_round_button_txt = Text(Point(140,195), "Next Round")
        next_round_button_txt.draw(self.score_screen_win)
        
        no_thanks_button = Rectangle(Point(220,170), Point(300,220))
        no_thanks_button.setFill("Purple")
        no_thanks_button.draw(self.score_screen_win)
        
        no_thanks_button_txt = Text(Point(260,195), "No Thanks")
        no_thanks_button_txt.setSize(16)
        no_thanks_button_txt.draw(self.score_screen_win)
        
        while True:
            point_clicked = self.score_screen_win.getMouse()
            
            if 100 <= point_clicked.getX() <= 180 and 170 <= point_clicked.getY() <= 220:
                self.score_screen_win.close()
                return "Restart Game"
            
            elif 220 <= point_clicked.getX() <= 300 and 170 <= point_clicked.getY() <= 220:
                self.score_screen_win.close()
                return "No Thanks"            
    
class Board:
    
    def __init__ (self, win, width, height):
        self.width = width
        self.height = height
        self.win = win
        self.draw_board()
    
    def draw_board(self):
        block_size = 90  
        self.ice_blocks = []
        for row in range(self.height):
            inner_list = []
            for column in range(self.width):
                x1 = column * block_size 
                y1 = row * block_size
                x2 = x1 + block_size
                y2 = y1 + block_size
                ice_block = Rectangle(Point(x1,y1), Point(x2,y2))
                
                
                inner_list.append(ice_block)
               
                
                ice_block.draw(self.win)
                ice_block.setFill("Grey")
                ice_block.setOutline("Black")   
            self.ice_blocks.append(inner_list)
        
    def break_ice(self, column, row):
        
        
        self.ice_blocks[row][column].setFill("White")
        
            
    def reset_board(self):
        
        block_size = 90  
        for row in range(self.height):
            for column in range(self.width): 
                self.ice_blocks[row][column].setFill("Grey")
                
        #self.draw_board()
        
        
    def move_validity_checker(self, column, row, current_position):
        
        current_x, current_y = current_position[0], current_position[1]
        
        if row == current_y and column == current_x:
            return False
        if 0 <= row < self.height and 0 <= column < self.width:
            if -1 <= abs(row - current_y) <= 1 and -1 <= abs(column - current_x) <= 1:
                return True 
                ##return (row, column) not in self.ice_blocks
        return False
                                                            
                                                            
                                                                     
class Player:
    
    def __init__(self, win, name, colour, position):
        self.win = win
        self.position = position
        self.name = name
        self.colour = colour
        #self.draw()
        self.player_symbol = Circle(self.position, 30)
        self.player_symbol.setFill(self.colour)
        self.player_symbol.draw(self.win)        
        
        
    def player_clicked (self, point):
        player_center_x_coord = self.position.getX()
        player_center_y_coord = self.position.getY()
        mouse_click_x_coord = point.getX()
        mouse_click_y_coord = point.getY()
        
        center_to_right_side_circle = player_center_x_coord + 30
        left_side_to_circle_center = player_center_x_coord - 30
        
        top_portion_of_circle = player_center_y_coord - 30
        bottom_portion_of_circle = player_center_y_coord + 30
        
        if left_side_to_circle_center <= mouse_click_x_coord <= center_to_right_side_circle and top_portion_of_circle <= mouse_click_y_coord <= bottom_portion_of_circle:
            return True
        else:
            return False
    
    def move_player(self, row, column):
        
        
        change_in_x = int(column - self.position.getX() // 90) * 90
        change_in_y = int(row - self.position.getY() // 90) * 90
        
        self.player_symbol.move(change_in_x, change_in_y)
        self.position = self.player_symbol.getCenter()
        
        return True 
            
        
    def can_move(self, board):
        
        xcoord_player, ycoord_player = int(self.position.getX() // 90), int(self.position.getY() // 90)
        
        for x_adj_positions in range (-1,2):
            for y_adj_positions in range (-1,2):
                
                adj_x_coord , adj_y_coord = xcoord_player + x_adj_positions, ycoord_player + y_adj_positions
                
                if adj_x_coord == xcoord_player and adj_y_coord == ycoord_player:
                    continue
                
                if 0 <= adj_x_coord < board.width and 0 <= adj_y_coord < board.height:
                    if board.ice_blocks[adj_y_coord][adj_x_coord].config["fill"] != "White":
                        return True
                       
        return False
    
    def position_player_reset_org(self, position):
        self.position.undraw()
        self.position = position 
        self.draw()
        
    
def splash_screen_creation():
    splash_screen_win = GraphWin("Vickram's Icebreaker - Splashscreen", 400, 300)
    
    splash_screen_win.setBackground("LightCyan")
    
    splash_screen_intro_text = Text(Point(200,70), "Welcome to the Icebreaker Game.\nThis game is written in part by Vickram Gill\nfor CMPT 103, Winter Session 2024")
    
    
    splash_screen_intro_text.setSize(17)
    splash_screen_intro_text.draw(splash_screen_win)
    
    want_to_play_txt = Text(Point(200,140), "Do you want to play?")
    want_to_play_txt.setSize(17)
    want_to_play_txt.setStyle("bold")
    want_to_play_txt.draw(splash_screen_win)
    
    
    play_game_button = Rectangle(Point(100,170), Point(180,220))
    play_game_button.setFill("LightGreen")
    play_game_button.draw(splash_screen_win)
    
    play_game_button_txt = Text(Point(140,195), "Play Game")
    play_game_button_txt.setSize(16)
    play_game_button_txt.draw(splash_screen_win)
    
    no_thanks_button = Rectangle(Point(220,170), Point(300,220))
    no_thanks_button.setFill("LightCoral")
    no_thanks_button.draw(splash_screen_win)
    
    no_thanks_button_txt = Text(Point(260,195), "No Thanks")
    no_thanks_button_txt.setSize(16)
    no_thanks_button_txt.draw(splash_screen_win) 
    
    while True:
        point_clicked = splash_screen_win.getMouse()
        
        if 100 <= point_clicked.getX() <= 180 and 170 <= point_clicked.getY() <= 220:
            splash_screen_win.close()
            return "Play Game"
        
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
