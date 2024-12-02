import random
board=[[0, 0, 0, 0, 0, 0, 0, 0, 8],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]

#create new board
def create_board():
    global board
    board=[]
    for i in range(9):
        board.append([0,0,0,0,0,0,0,0,0])
"""
# check Condition
def check_place(row,col,value):
    for i in range(9):
        #check row condition
        if(board[row][i]==value):
            print("row condtion")
            return False
        #check column condiion
        if (board[i][col]==value):
            print("col condtion")
            return False
        if(board[((row//3)*3)+(i//3)][((col//3)*3)+(i%3)]==value):
            print("box condtion")
            return False
        
    # suitable value for row,col
    return True
"""
def check_place(row, col, value):
    global board
    # Check row condition
    for i in range(9):
        if board[row][i] == value:
            return False

    # Check column condition
    for i in range(9):
        if board[i][col] == value:
            return False

    # Check subgrid condition
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == value:
                return False

    return True

            
# insert_value
def insert_value(size):
    global board
    count=size
    while(count!=0):
        row=int(input("Enter row col value :"))
        col=int(input("Enter  col value : "))
        value=int(input("Enter  value : "))
        #row,col,value=tuple(lst.split())
        if(check_place(row,col,value)):
            board[row][col]=value
            print_board()
            print("value inserted..")
            count=count-1
        else:
            pass
        break
    
def isempty():
    global board
    empty=0
    for row in board:
        for value in row:
            if value==0:
                empty+=1
    print("Total ",81-empty," value filled ")
    print("Balance " ,empty)
# Auto random value fill
def isfull():
    global board
    
    for row in board:
        for value in row:
            if value==0:
                return False
    return True
def auto_fill(size):
    global board
    #random.seed(42)
    count=size
    while(count!=0):
        
        row=random.randint(0,8)
        col=random.randint(0,8)
        value=random.randint(1,9)
        #row,col,value=tuple(lst.split())
        if(board[row][col]==0):
            if check_place(row,col,value) :
                board[row][col]=value
                #print_board()
                count=count-1
       
    
    
    

# print Board
def print_board():
    global board
    print("_____ Welcome to Board____\n")
    for row in board:
        print(row)
    isempty()
        
# how much filled
def how_much():
    count=0
    for row in board:
        for value in row:
            if value!=0:
                count+=1
    print("number of values in board : ",count)

# fill full board using backTracking
def sudu():
    global board
    if isfull():
        return True
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                for num in range(1,10):
                
                    if check_place(i,j,num):
                        board[i][j]=num
                        if sudu():
                            return True
                        
                        board[i][j]=0
                return False
    return False

if __name__=='__main__':
    
    
                                
    print("Welcome to suduku Game ")
    while 1:
        print()
        print("1.Start new Game ")
        print("2.Show board ")
        print("3.Insert a value into board ")
        print("4.Show the Result and end the game ")
        print("5.exit")
        choice=input("Enter Your Choice ")
        if choice =='1':
            print("Select level \n1. Easy \n2.Medium \n3.Hard")
            level=input("Enter level : ")
            if level=='1':
                create_board()
                auto_fill(20)
                print_board()
            elif level=='2':
                create_board()
                auto_fill(15)
                print_board()
            elif level=='3':
                create_board()
                auto_fill(10)
                print_board()
            else:
                print("Wrong choice !!!")
        elif choice =='2':
            
            print_board()
        elif choice=='3':
            
            insert_value(1)
        elif choice=='4':
            
            sudu()
            print_board()
        elif choice=='5':
            print("program Exiting ...!!!")
            break
        else:
            print("You entered Wrong choice ..!!")
        
            
    
    

