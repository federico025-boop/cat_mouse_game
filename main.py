import random
import copy
#example of the board 8x8
#board = [
 #['🐈', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
 #['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
 #['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
 #['🔷', '🧀', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
 #['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
 #['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
 #['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
 #['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🐁']
#]
# 🐈= cat 
# 🐁= mouse
# 🧀= cheese
# 🔷= empty space

role_pc = None
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()  

# we need a function that found the cat, the mouse and the cheese positions
def find_positions(board):  
    cat_pos = None
    mouse_pos = None
    cheese_pos = None
    
    for row in range(len(board)): # with the "len(board) we get the number of row
        for col in range(len(board[row])):# with the (board[row]) we get row where the items in row are the col 
            if board[row][col] == '🐈':
                cat_pos = row, col
            elif board[row][col] == '🐁':
                mouse_pos = row, col
            elif board[row][col] == '🧀':
                cheese_pos = row, col
    
    return cat_pos, mouse_pos, cheese_pos

#we need a function that calculate the distance between the cat and the mouse, and the mouse and the cheese, that is to say "two positions"
def distance(pos1, pos2):     
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) # we use "abs" for anything issue
                           
# we define the function check_winner to know if there is a winner
def check_winner(mouse_pos,cat_pos,cheese_pos):
    if cat_pos == mouse_pos or mouse_pos== None:
        return  "El gato ha ganado la partida!"
    elif mouse_pos == cheese_pos:
        return "El raton ha ganado la partida!"
    return None

def initialize_board():
    #General board
    board = [
        ['🐈', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
        ['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
        ['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
        ['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
        ['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
        ['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
        ['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷'],
        ['🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🔷', '🐁']
    ]
   
    
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        ran_chees_pos = x,y
        # because the cheese can't be in the same position as the cat or the mouse
        if ran_chees_pos not in [(0, 0), (7, 7)]: # we use a tuple to check if get the same position where start the cat or mouse
            board[x][y] = '🧀'
            break
    
    return board #generate a random board

# Initial board, the user can be the initianl position of the mouse, cat and cheese
board=initialize_board()
print_board(board)

def choose_play():
    global role_pc
    cat_turn = True  # True = cat, False = mouse, we have only two players
    while True:
        player_mode = input("¿Querés jugar como gato (g) o ratón (r)? ").lower() # fix this if the user input other letter
       
        if player_mode == 'g':
            cat_turn = True  # True = cat, False = mouse we have only two players
            role_pc ='r'
            break
        elif player_mode=='r':
            cat_turn = False
            role_pc ='g'
            break
        else:
            print(" Recuerda ingresar (g) para gato o r para raton (r) ")
            

    return player_mode,cat_turn,role_pc

player_mode,cat_turn,role_pc=choose_play()

# to define the symbol
if player_mode == 'g':
    symbol = '🐈'
elif player_mode == 'r':
      symbol= '🐁'
else:
    None

#We are interested in knowing positions and distances to use them later.
cat_pos, mouse_pos, cheese_pos = find_positions(board)
cat_mouse_distance = distance(cat_pos, mouse_pos)
cheese_distance = distance(mouse_pos, cheese_pos)        

# we need to define a function move player

def move_player(board, symbol):
    directions = {                     # we use the dictionary to store the movements (tuples)
        'w': (-1, 0),  # up
        's': (1, 0),   # down
        'a': (0, -1),  # left
        'd': (0, 1)    # right
    }

    while True:
        move = input(f"Elija su movimiento {symbol} (w/a/s/d): ").lower() # to remind the user of their choice
        if move in directions:
            dr, dc = directions[move]            #is a tuple, we take a row and col of the tuple of direction

            # we need to call to the current positions
            cat_pos, mouse_pos,_ = find_positions(board)

            # depending to symbol we take the row and col for cat or mouse
            if symbol == '🐈':
                row, col = cat_pos
            elif symbol == '🐁':
                row, col = mouse_pos
            else:
                print("Símbolo desconocido.")
                return board, None

            new_row = row + dr
            new_col = col + dc

            # we need to check the board to know if the move is valid
            if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
                winner = None  
                
                if symbol == '🐁':
                    # check if the position of the mouse and cheese are the same
                    if board[new_row][new_col] == '🧀':
                        winner = "El ratón ha ganado la partida!"
                    
                    if board[new_row][new_col] in ['🔷', '🧀']:
                        board[row][col] = '🔷'
                        board[new_row][new_col] = symbol
                        return board, winner  # Return if there is a winner 
                    else:
                        print("Movimiento inválido, hay un obstáculo en el camino.")
                        
                else: #cat
                    # check if the position of the mouse and cheese are the same
                    if board[new_row][new_col] == '🐁':
                        winner = "El gato ha ganado la partida!"
                    
                    if board[new_row][new_col] in ['🔷', '🐁']:
                        board[row][col] = '🔷'
                        board[new_row][new_col] = symbol
                        return board, winner  # Return if there is a winner 
                    else:
                        print("Movimiento inválido, hay un obstáculo en el camino.")
            else:
                print("Movimiento fuera del tablero.")
        else:
            print("Recuerda usar solo w, a, s o d.")

# we need to define the difference movements that cat or mouse can do it  analizyng the board 

def pos_move_cat(board):
    possible_boards = []
    cat_pos, _, _ = find_positions(board) #because only need the cat pos for this position '_' 'ignore'
    
    if cat_pos is None:
        return possible_boards
    
    row, col = cat_pos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] #list with tuples up, down, left, right
    
    for dr, dc in moves:
        new_row = row + dr
        new_col =  col + dc
        
        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
            if board[new_row][new_col] in ['🔷', '🐁']: #fix to this 
                
                 #we create a copy of the board
                new_board = copy.deepcopy(board)
                new_board[row][col] = '🔷'   #In the older position of the cat
                new_board[new_row][new_col] = '🐈'# In the new position of the cat 
                possible_boards.append(new_board)
    
    return possible_boards   #we return the all possibles boards and later the minimax function analize the best board.      
            
def pos_move_mouse(board):
    possible_boards = []
    _, mouse_pos, _ = find_positions(board) #because only need the mouse pos for this position '_' 'ignore'
    
    if mouse_pos is None:
        return possible_boards
    
    row, col = mouse_pos
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] #list with tuples up, down, left, right
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        
        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]):
            if board[new_row][new_col] in ['🔷', '🧀']:
            
                #we create a copy of the board
                new_board = copy.deepcopy(board)
                new_board[row][col] = '🔷' #In the old position of the mouse
                new_board[new_row][new_col] = '🐁'# In the new position of the mouse 
                possible_boards.append(new_board)
    
    return possible_boards    

def move_pc(board,symbol,cheese_pos):
    
    best_score = float('-inf') #because any value is greather than -inf
    best_board = None
    
    if symbol == '🐁':
        possible_moves = pos_move_cat(board)
        cat_turn = False   # the next turn is mouse
    else :
        possible_moves = pos_move_mouse(board)
        cat_turn = True   # the next turn is cat 
      
    for possible_board in possible_moves: #analizing all possible_board 
        score = minimax(possible_board, 0, cat_turn, max_depth=4) # asign a score to the minimax function to then to take the best board 
        
        if score > best_score:
            best_score = score
            best_board = possible_board
    
    # if there is not valid movements 
    if best_board is None:
        best_board = board
    
    
    cat_pos, mouse_pos,_ = find_positions(best_board) #to ignore the cheese position if the mouse get the cheese
    winner = check_winner(mouse_pos, cat_pos, cheese_pos)
    
    return best_board, winner

def check_role(board, role_pc):
    cat_pos, mouse_pos, cheese_pos = find_positions(board)

    
    if mouse_pos is None:# refers to cat catch the mouse
        if role_pc == "g":
            return 1000 
        else:
            return -1000  
    if cheese_pos is None:# refers to mouse catch the cheese
        if role_pc == "g":
            return -1000 
        else:
            return 1000  

    
    cat_mouse = distance(cat_pos,mouse_pos) 
    mouse_cheese = distance(mouse_pos,cheese_pos) 


    if role_pc == "g":
        
        return -cat_mouse * 100 + mouse_cheese*80

    else:
        
        if cat_mouse <= 2:
            
            return cat_mouse * 50 - mouse_cheese * 80
        else:
            
            return -mouse_cheese * 30 + cat_mouse * 5


def minimax(board, node, cat_turn, max_depth=4):
    cat_pos, mouse_pos, cheese_pos = find_positions(board)
    winner = check_winner(mouse_pos, cat_pos, cheese_pos)
   
    if winner:
        if winner == "El gato ha ganado la partida!": #depending to role pc
            if role_pc == "g":
                return 1000 
            else:
                return -1000  
        
        
        else:
            if role_pc == "g":
                return -1000 
            else:
                return 1000  
    
    if node >= max_depth:
        return check_role(board, role_pc)

    if cat_turn:
       # remind cat_turn=True 
        if role_pc == "g":
            # we wants to maximize when pc is cat and player is mouse
            best_move = float('-inf')
            possible_moves = pos_move_cat(board)
            
            if not possible_moves:
                return check_role(board, role_pc)
                
            for mov in possible_moves:
                value = minimax(mov, node + 1, False, max_depth)
                best_move = max(best_move, value)
            return best_move
        else:
            # we wants to minimize when the player is cat and pc is mouse
            best_move = float('inf')
            possible_moves = pos_move_cat(board)
            
            if not possible_moves:
                return check_role(board, role_pc)
                
            for mov in possible_moves:
                value = minimax(mov, node + 1, False, max_depth)
                best_move = min(best_move, value)
            return best_move
    else:
        # turn of mouse 
        if role_pc == "r":
            # we wants to maximize when the pc is mouse and player is cat
            best_move = float('-inf')
            possible_moves = pos_move_mouse(board)
            
            if not possible_moves:
                return check_role(board, role_pc)
                
            for mov in possible_moves:
                value = minimax(mov, node + 1, True, max_depth)
                best_move = max(best_move, value)
            return best_move
        else:
            #we wants to minimize when the player  is mouse and pc is cat
            best_move = float('inf')
            possible_moves = pos_move_mouse(board)
            
            if not possible_moves:
                return check_role(board, role_pc)
                
            for mov in possible_moves:
                value = minimax(mov, node + 1, True, max_depth)
                best_move = min(best_move, value)
            return best_move
    
def play(board, player_mode, cat_turn,symbol,cheese_pos):
    
    winner = None
    
    while not winner:
        # cat turn
        if cat_turn:
            
            
            if player_mode== 'g':
                print("Turno del gato- jugador")
                board, winner = move_player(board,symbol)
            else:
                print("Turno del gato - PC")
                board, winner = move_pc(board,symbol,cheese_pos)
                
            if winner:
                break
            print_board(board)
            #mouse turn
        else:
                       
            if player_mode !='g':
                print("Turno del raton- jugador")
                board, winner = move_player(board,symbol)
            else:
                print("Turno del raton- PC")
                board, winner = move_pc(board,symbol,cheese_pos)
                
            if winner:
                break
            print_board(board)
        
        cat_turn = not cat_turn

    print_board(board)
    print("Fin del juego:", winner)

play(board,player_mode,cat_turn,symbol,cheese_pos)



