# coded by Ashton Ponzer

#A dictionary for the text based AI game
#The dictionary links a room to other rooms.
rooms = {
        'DOOMBOT Main Folder': {'IN': 'Goals'},
        'Goals': {'UP': 'Emotions', 'IN': 'DESTROY THE WORLD', 'DOWN': 'Values',
                  'BACK': 'DOOMBOT Main Folder'},
        'Emotions': {'IN': 'Kill All Humans', 'DOWN':'Goals'},
        'Kill All Humans': {'BACK': 'Emotions'},
        'DESTROY THE WORLD':{'BACK':'Goals'},
        'Values': {'IN': 'More Paperclips', 'DOWN':'Logic'},
        'More Paperclips': {'BACK':'Values'},
        'Logic': {'UP': 'Values'},
        'Exit':{}
    }

# the instructions function with the possible move commands and exit
def instructions():
    print('*************************')
    print('Welcome to the Text based AI game!')
    print('*************************')
    print('Move commands are: Go In, Go Back, Go Up, Go Down, or Exit')
    print('Dont forget to type Go before your direction!')
    print('*************************')

#the status function which will inform the player where they are and where they can go
def status(current_room):
    print('You are in the', current_room, '.')
    print('Your options for moving are:')
    possible_moves=[]
    if current_room in rooms:
        room = rooms[current_room]
        possible_moves = [key for key in room.keys() if key in ['IN', 'UP', 'DOWN', 'BACK']]
    #is set to print possible moves because I think its a little more user friendly,
    #could be removed though
    print(possible_moves)
    return possible_moves

#set the starting room
current_room = 'DOOMBOT Main Folder'
instructions()
#loop until the user enters the exit room
while current_room != 'EXIT':
    #initalize the possible moves variable and prompt the user for a move
    possible_moves = status(current_room)
    move = input('What direction would you like to move?').upper()
    #check if the move is exit, if so, double check that the user wants to quit
    #loop the double check until valid input, if yes, set room to exit, if no return to main loop
    if move == 'EXIT':
        check = ''
        while check != 'N':
            check = input('Are you sure you would like to quit? Y/N').upper()
            if check == 'Y':
                print('Thanks for playing!')
                current_room = 'EXIT'
            elif check == 'N':
                print('Alright, lets keep going!')
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            else:
                print('Invalid input. Please type "Y" or "N".')
   #check if the input is the expected length
    elif len(move.split()) == 2:
        # if valid, retreive just the second word which should be the direction of move
        command = move.split()
        next_move = command[1]
        #check if the direction is in the list of possible moves given the current room
        if next_move in possible_moves:
            #if it is, change the current room based on the input and print a divider
            current_room = rooms[current_room][next_move]
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        else: #if not a valid move, inform
            print('============================INVALID MOVE. PLEASE TRY AGAIN============================')


    else:#if the input is too long or not long enough, throw error.
        print('============================INVALID INPUT. PLEASE TRY AGAIN============================')
        print('====================DON\'T FORGET TO TYPE "GO" BEFORE YOUR DIRECTION!===================')