from tkinter import *
from valid import *

turn_count = 1
def player_turn():
    turn_count
    return 'w' if turn_count % 2 == 0 else 'b'

def opponent():
    turn_count
    return 'b' if turn_count % 2 == 0 else 'w'
    
def new_game(board):
    for i in range(8):
        for j in range(8):
            board[i][j].config(image=Default)
    board[0][0].config(image=bR,text='bR') 
    board[0][7].config(image=bR,text='bR') 
    board[0][1].config(image=bN,text='bN') 
    board[0][6].config(image=bN,text='bN') 
    board[0][2].config(image=bB,text='bB') 
    board[0][5].config(image=bB,text='bB') 
    board[0][3].config(image=bQ,text='bQ') 
    board[0][4].config(image=bK,text='bK')
    for j in range(8):
        board[1][j].config(image=bP,text='bP') 
    board[7][0].config(image=wR,text='wR') 
    board[7][7].config(image=wR,text='wR') 
    board[7][1].config(image=wN,text='wN') 
    board[7][6].config(image=wN,text='wN') 
    board[7][2].config(image=wB,text='wB') 
    board[7][5].config(image=wB,text='wB') 
    board[7][3].config(image=wQ,text='wQ') 
    board[7][4].config(image=wK,text='wK')
    for j in range(8):
        board[6][j].config(image=wP,text='wP')     
def checkifright(row,column):
    if board_piece[row][column]['text'] == 'bP':
        print('true')
    else:
        print(board_piece[row][column]['text'])
    
def pressed():
    print('Pressed')
window = Tk()
window.title('Chess.nigga')
Default = PhotoImage(file="Chess_Assets\\0.png")
bB = PhotoImage(file="Chess_Assets\\bB.png")
bK = PhotoImage(file="Chess_Assets\\bK.png")
bN = PhotoImage(file="Chess_Assets\\bN.png")
bP = PhotoImage(file="Chess_Assets\\bP.png")
bQ = PhotoImage(file="Chess_Assets\\bQ.png")
bR = PhotoImage(file="Chess_Assets\\bR.png")
wB = PhotoImage(file="Chess_Assets\\wB.png")
wK = PhotoImage(file="Chess_Assets\\wK.png")
wN = PhotoImage(file="Chess_Assets\\wN.png")
wP = PhotoImage(file="Chess_Assets\\wP.png")
wQ = PhotoImage(file="Chess_Assets\\wQ.png")
wR = PhotoImage(file="Chess_Assets\\wR.png")


frame = Frame(window)
frame.pack()
board_piece = [[None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               [None,None,None,None,None,None,None,None],
               ]

for i in range(8):
    count = 0 if i % 2 == 0 else 1
    for j in range(8):
        if count % 2 == 0:
            board_piece[i][j] = Button(frame,
                                    image=Default,
                                    bg='#779556',
                                    width=50,
                                    height=50,
                                    activebackground='#779556',
                                    relief=SUNKEN,
                                    borderwidth=0,
                                    text='No',
                                    command=lambda row=i,column=j,turn=(player_turn()) : [pressed,checkifright(row,column),check_board(board_piece,row,column)]
                                    )
            
            board_piece[i][j].grid(row=i,column=j)
        else:
            board_piece[i][j] = Button(frame,
                                    image=Default,
                                    bg='#ebecd0',
                                    width=50,
                                    height=50,
                                    activebackground='#ebecd0',
                                    relief=SUNKEN,
                                    borderwidth=0,
                                    text='No',
                                    command=lambda row=i,column=j,turn=(player_turn()) : [pressed,checkifright(row,column),check_board(board_piece,row,column)]
                                    )           
            board_piece[i][j].grid(row=i,column=j)
        count += 1

new_game(board_piece)

window.mainloop()
