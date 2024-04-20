from tkinter import *
from tkinter import messagebox
current_indexvtcl = -8
current_indexhrztl = -8
current_turn = 0

def check_board(board,row,column):
    global current_indexvtcl
    global current_indexhrztl
    global current_turn
    turn = 'w' if current_turn % 2 == 0 else 'b'
    opponent = 'w' if current_turn % 2 == 1 else 'b'
    print(current_indexhrztl,current_indexvtcl)
    check_if_is_switching(board,row,column,turn)
    if current_indexvtcl != 8:
        if check_if_playing(board,row,column):
            current_turn += 1
            return
    if turn == board[row][column]['text'][0]:
        if (board[row][column]['text'] == 'bN' or board[row][column]['text'] == 'wN'):
            valid_move_knight(board,row,column)
        if (board[row][column]['text'] == 'bB' or board[row][column]['text'] == 'wB'):
            valid_move_bishop(board,row,column,turn)
        if (board[row][column]['text'] == 'bR' or board[row][column]['text'] == 'wR'):
            valid_move_rook(board,row,column,turn)
        if (board[row][column]['text'] == 'bQ' or board[row][column]['text'] == 'wQ'):
            valid_move_bishop(board,row,column,turn)
            valid_move_rook(board,row,column,turn)
        if board[row][column]['text'] == 'wP':
            valid_move_white_pawn(board,row,column)
        if board[row][column]['text'] == 'bP':
            valid_move_black_pawn(board,row,column)
        if (board[row][column]['text'] == 'bK' or board[row][column]['text'] == 'wK'):
            valid_move_king(board,row,column,turn)


    visualising_valid(board)
                
def valid_move_knight(board,row,column):
        global current_indexvtcl
        global current_indexhrztl
        current_indexvtcl = row      
        current_indexhrztl = column
        if (row + 1 <= 7 and column + 2 <= 7) :
            if (board[row+1][column+2]['text'][0] != board[row][column]['text'][0]):
                board[row+1][column+2]['text'] = 'valid'
        if (row + 2 <= 7 and column + 1 <= 7):
            if (board[row+2][column+1]['text'][0] != board[row][column]['text'][0]):                        
                board[row+2][column+1]['text'] = 'valid'
        if (row - 2 >= 0 and column -1 >= 0):
            if (board[row-2][column-1]['text'][0] != board[row][column]['text'][0]):                        
                board[row-2][column-1]['text'] = 'valid'
        if (row - 1 >= 0 and column - 2 >= 0):
            if (board[row-1][column-2]['text'][0] != board[row][column]['text'][0]):                        
                board[row-1][column-2]['text'] = 'valid'
        if (row + 1 <= 7 and column - 2 >= 0):
            if (board[row+1][column-2]['text'][0] != board[row][column]['text'][0]):                        
                board[row+1][column-2]['text'] = 'valid'
        if (row - 1 >= 0 and column + 2 <= 7):
            if (board[row-1][column+2]['text'][0] != board[row][column]['text'][0]):                        
                board[row-1][column+2]['text'] = 'valid'
        if (row + 2 <= 7 and column - 1 >= 0):
            if (board[row+2][column-1]['text'][0] != board[row][column]['text'][0]):                        
                board[row+2][column-1]['text'] = 'valid'
        if (row - 2 >= 0 and column + 1 <= 7):
            if (board[row-2][column+1]['text'][0] != board[row][column]['text'][0]):                        
                board[row-2][column+1]['text'] = 'valid'
        
def valid_move_bishop(board,row,column,turn):
    global current_indexvtcl
    global current_indexhrztl
    current_indexvtcl = row
    current_indexhrztl = column
    extending = 1
    opponent  = 'w' if turn == 'b' else 'b'
    while(True):
        if row+extending > 7 or column +extending > 7:
            break
        if board[row+extending][column+extending]['text'][0] != opponent:
            if board[row+extending][column+extending]['text'][0] == turn:
                break
            board[row+extending][column+extending]['text'] = 'valid'
            extending += 1
        else:
            board[row+extending][column+extending]['text'] = 'valid'
            break
    extending = 1
    while(True):
        if row-extending < 0 or column - extending < 0:
            break
        if board[row-extending][column-extending]['text'][0] != opponent:
            if board[row-extending][column-extending]['text'][0] == turn:
                break
            board[row-extending][column-extending]['text'] = 'valid'
            extending += 1
        else:
            board[row-extending][column-extending]['text'] = 'valid'
            break
    extending = 1
    while(True):
        if row+extending > 7 or column - extending < 0:
            break
        if board[row+extending][column-extending]['text'][0] != opponent:
            if board[row+extending][column-extending]['text'][0] == turn:
                break
            board[row+extending][column-extending]['text'] = 'valid'
            extending += 1
        else:
            board[row+extending][column-extending]['text'] = 'valid'
            break
    extending = 1
    while(True):
        if row-extending < 0 or column + extending > 7:
            break
        if board[row-extending][column+extending]['text'][0] != opponent:
            if board[row-extending][column+extending]['text'][0] == turn:
                break
            board[row-extending][column+extending]['text'] = 'valid'
            extending += 1
        else:
            board[row-extending][column+extending]['text'] = 'valid'
            break
    extending = 1

def valid_move_rook(board,row,column,turn):
    global current_indexvtcl
    global current_indexhrztl
    current_indexvtcl = row
    current_indexhrztl = column
    extending = 1
    opponent  = 'w' if turn == 'b' else 'b'
    while(True):
        if row + extending > 7:
            break
        if board[row+extending][column]['text'][0] != opponent:
            if board[row+extending][column]['text'][0] == turn:
                break
            board[row+extending][column]['text'] = 'valid'
            extending += 1
        else:
            board[row+extending][column]['text'] = 'valid'
            break
    extending = 1
    while(True):
        if row - extending < 0:
            break
        if board[row-extending][column]['text'][0] != opponent:
            if board[row-extending][column]['text'][0] == turn:
                break
            board[row-extending][column]['text'] = 'valid'
            extending += 1
        else:
            board[row-extending][column]['text'] = 'valid'
            break
    extending = 1
    while(True):
        if column + extending > 7:
            break
        if board[row][column+extending]['text'][0] != opponent:
            if board[row][column+extending]['text'][0] == turn:
                break
            board[row][column+extending]['text'] = 'valid'
            extending += 1
        else:
            board[row][column+extending]['text'] = 'valid'
            break
    extending = 1
    while(True):
        if column - extending < 0:
            break
        if board[row][column-extending]['text'][0] != opponent:
            if board[row][column-extending]['text'][0] == turn:
                break
            board[row][column-extending]['text'] = 'valid'
            extending += 1
        else:
            board[row][column-extending]['text'] = 'valid'
            break

def valid_move_white_pawn(board,row,column):
    global current_indexvtcl
    global current_indexhrztl
    current_indexvtcl = row
    current_indexhrztl = column
    if row == 6:
        if board[row-1][column]['text'][0] == 'N':
            board[row-1][column]['text'] = 'valid'
            if board[row-2][column]['text'][0] == 'N':
                board[row-2][column]['text'] = 'valid'
        if column - 1 >= 0:
            if board[row-1][column-1]['text'][0] == 'b':
                board[row-1][column-1]['text'] = 'valid'
        if column + 1<= 7:
            if board[row-1][column+1]['text'][0] =='b':
                board[row-1][column+1]['text'] ='valid'
    if row != 6:
        if board[row-1][column]['text'][0] == 'N':
            board[row-1][column]['text'] = 'valid'
        if column - 1 >= 0:
            if board[row-1][column-1]['text'][0] == 'b':
                board[row-1][column-1]['text'] = 'valid'
        if column + 1<= 7:
            if board[row-1][column+1]['text'][0] =='b':
                board[row-1][column+1]['text'] ='valid'

def valid_move_black_pawn(board,row,column):
    global current_indexvtcl
    global current_indexhrztl
    current_indexvtcl = row
    current_indexhrztl = column
    if row == 1:
        if board[row+1][column]['text'][0] == 'N':
            board[row+1][column]['text'] = 'valid'
            if board[row+2][column]['text'][0] == 'N':
                board[row+2][column]['text'] = 'valid'
        if column - 1 >= 0:
            if board[row+1][column-1]['text'][0] == 'w':
                board[row+1][column-1]['text'] = 'valid'
        if column + 1<= 7:
            if board[row+1][column+1]['text'][0] =='w':
                board[row+1][column+1]['text'] ='valid'
    if row != 1:
        if board[row+1][column]['text'][0] == 'N':
            board[row+1][column]['text'] = 'valid'
        if column - 1 >= 0:
            if board[row+1][column-1]['text'][0] == 'w':
                board[row+1][column-1]['text'] = 'valid'
        if column + 1<= 7:
            if board[row+1][column+1]['text'][0] =='w':
                board[row+1][column+1]['text'] ='valid'
    
def valid_move_king(board,row,column,turn):
    global current_indexvtcl
    global current_indexhrztl
    current_indexvtcl = row
    current_indexhrztl = column
    if row+1 <=7:
        if board[row+1][column]['text'][0]!= turn:
            board[row+1][column]['text'] = 'valid'
        if column + 1 <=7:
            if board[row+1][column+1]['text'][0] != turn:
                board[row+1][column+1]['text'] = 'valid'
        if column - 1 >= 0:
            if board[row+1][column-1]['text'][0] != turn:
                board[row+1][column-1]['text'] = 'valid'
    if row -1 >=0:
        if board[row-1][column]['text'][0] != turn:
            board[row-1][column]['text'] = 'valid'
        if column + 1<=7:
            if board[row-1][column+1]['text'][0] != turn:
                board[row-1][column+1]['text'] = 'valid'
        if column -1 >=0:
            if board[row-1][column-1]['text'][0] != turn:
                board[row-1][column-1]['text'] = 'valid'
    if column + 1<=7:
        if board[row][column+1]['text'][0] != turn:
            board[row][column+1]['text'] = 'valid'
    if column -1 >=0:
        if board[row][column-1]['text'][0] != turn:
            board[row][column-1]['text'] = 'valid'
        
def check_if_selecting(board):
    for i in range(8):
        for j in range(8):
            if board[i][j]['text'] == 'valid':
                return True
    return False


def check_if_is_switching(board,row,col,turn):
    if turn == board[row][col]['text'][0] or board[row][col]['text'] == 'No':
        clear_valid(board)


def check_if_playing(board,row,column):
    global current_indexvtcl
    global current_indexhrztl
    global current_turn
    a = board[row][column] 
    b = board[current_indexvtcl][current_indexhrztl]
    if b['text'] == 'wP' and row == 0 and a['text'] == 'valid':
        a['image'] = b['image']
        board[current_indexvtcl][current_indexhrztl]['image'] = 'pyimage1'
        b['text'] = 'No'
        a['text'] = 'wQ'
        a['bg'] = '#779556' if column % 2 == 0 else '#ebecd0'
        a['image'] = 'pyimage12'
        current_indexhrztl = -8
        current_indexvtcl = -8
        clear_valid(board)
        return True
    if b['text'] == 'bP' and row == 7 and a['text'] == 'valid':
        a['image'] = b['image']
        board[current_indexvtcl][current_indexhrztl]['image'] = 'pyimage1'
        b['text'] = 'No'
        a['text'] = 'bQ'
        a['bg'] = '#779556' if column % 2 == 1 else '#ebecd0'
        a['image'] = 'pyimage12'
        current_indexhrztl = -8
        current_indexvtcl = -8
        clear_valid(board)
        return True
    bruh = b['text']
    if  (a['image'] == 'pyimage9' or a['image'] == 'pyimage3') and check_if_selecting and b['text'][1]!='K':
        print('a player won')
        player = 'WHITE' if current_turn % 2 == 0 else 'BLACK'
        if messagebox.askretrycancel(title=str(player)+' WON!',message='DO YOU WANT TO START A NEW GAME?'):
            new_game(board)
        else:
            pass
        return True
    if a['text'] == 'valid':
        #mass_murder = 0 if row % 2 == 0 else 1
        a['image'] = b['image']
        #a['text'] = bruh
        board[current_indexvtcl][current_indexhrztl]['image'] = 'pyimage1'
        b['text'] = 'No'
        #board[row][column]['bg'] = '#779556' if (mass_murder + current_indexhrztl) % 2 == 0 else '#ebecd0'
        clear_valid(board)   
        current_indexhrztl = -8
        current_indexvtcl = -8
        return True
    
    return False
    
        
def visualising_valid(board):
    for i in range(8):
        for j in range(8):
            if board[i][j]['text'] == 'valid':
                board[i][j]['bg'] = '#FF474C'

def clear_valid(board):
    for i in range(8):
        for j in range(8):
            if board[i][j]['text'] == 'valid':
                mass_murder = 0 if i % 2 == 0 else 1
                board[i][j]['bg'] = '#779556' if (mass_murder + j) % 2 == 0 else '#ebecd0'
                board[i][j]['text'] = changing_valid_chess_piece_text_base_on_image(board,i,j)
            
def changing_valid_chess_piece_text_base_on_image(board,row,column): #nigga i'm tired no want to use arrays
    a = board[row][column]['image']
    if a == 'pyimage1':
        return 'No'
    if a == 'pyimage2':
        return 'bB'
    if a == 'pyimage3':
        return 'bK'
    if a == 'pyimage4':
        return 'bN'
    if a == 'pyimage5':
        return 'bP'
    if a == 'pyimage6':
        return 'bQ'
    if a == 'pyimage7':
        return 'bR'
    if a == 'pyimage8':
        return 'wB'
    if a == 'pyimage9':
        return 'wK'
    if a == 'pyimage10':
        return 'wN'
    if a == 'pyimage11':
        return 'wP'
    if a == 'pyimage12':
        return 'wQ'
    if a == 'pyimage13':
        return 'wR'

def new_game(board):
    global current_turn
    clear_valid(board)
    for i in range(8):
        for j in range(8):
            board[i][j]['text'] = 'No'
            board[i][j]['image'] = 'pyimage1'
    board[0][0]['text'] = 'bR'
    board[0][0]['image'] = 'pyimage7' 
    board[0][7]['text'] = 'bR'
    board[0][7]['image'] = 'pyimage7' 
    board[0][1]['text'] = 'bN'
    board[0][1]['image'] = 'pyimage4'
    board[0][6]['text'] = 'bN'
    board[0][6]['image'] = 'pyimage4'
    board[0][2]['text'] = 'bB'
    board[0][2]['image'] = 'pyimage2' 
    board[0][5]['text'] = 'bB'
    board[0][5]['image'] = 'pyimage2' 
    board[0][3]['text'] = 'bQ'
    board[0][3]['image'] ='pyimage6' 
    board[0][4]['text'] = 'bK'
    board[0][4]['image']= 'pyimage3'
    for j in range(8):
        board[1][j]['text'] = 'bP'
        board[1][j]['image'] = 'pyimage5'
    board[7][0]['text'] = 'wR'
    board[7][0]['image'] ='pyimage13' 
    board[7][7]['text'] = 'wR'
    board[7][7]['image'] ='pyimage13' 
    board[7][1]['text']= 'wN'
    board[7][1]['image'] ='pyimage10'
    board[7][6]['text']= 'wN'
    board[7][6]['image'] ='pyimage10'
    board[7][2]['text'] = 'wB'
    board[7][2]['image'] = 'pyimage8'
    board[7][5]['text'] = 'wB'
    board[7][5]['image'] = 'pyimage8' 
    board[7][3]['text'] = 'wQ'
    board[7][3]['image'] = 'pyimage12'
    board[7][4]['text'] = 'wK'
    board[7][4]['image'] = 'pyimage9'
    for j in range(8):
        board[6][j]['text'] = 'wP'
        board[6][j]['image'] = 'pyimage11'   
    current_turn = -1
