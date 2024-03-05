#Ashton Ponzer
def main():
    #A dictionary for the text based AI game
    #The dictionary links a room to other rooms.
    rooms = {
            'DOOMBOT Main': {'IN': 'Goals','Key':'None'},
            'Goals': {'UP': 'Emotions', 'IN': 'DESTROY THE WORLD', 'DOWN': 'Values',
                      'BACK': 'DOOMBOT Main Folder', 'Key':'NUMBER'},
            'Emotions': {'IN': 'Kill All Humans', 'DOWN':'Goals', 'Key':'UPPERCASE LETTER'},
            'Kill All Humans': {'BACK': 'Emotions','Key':'SYMBOL'},
            'DESTROY THE WORLD':{'BACK':'Goals', 'Key':'None'},
            'Values': {'UP':'Goals', 'IN': 'More Paperclips', 'DOWN':'Logic', 'Key':'ORDER'},
            'More Paperclips': {'BACK':'Values','Key':'LOCATION'},
            'Logic': {'UP': 'Values','Key':'LOWERCASE LETTER'},
            'Exit':{}
        }

    # the instructions function with the possible move commands and exit
    def instructions():
        print('************************************************************************************************')
        print('Welcome to the Text based AI game!')
        print('The DOOMBOT you have programmed has started to go Rouge and wants to destroy the world for some odd reason!')
        print('You will need to collect the 6 components to decypting the DOOMBOT\'s shut down portocol without alerting it!')
        print('These components include: a Number, an Uppercase Letter, a symbol, '
              'a lowercase Letter, their order, and the location of the protocol!')
        print('                   *************************************************************')
        print('To navigate the folder structure, use the '
              'Movement Commands: Go In, Go Back, Go Up, Go Down, or Exit')
        print('Dont forget to type \'Go\' before your direction!')
        print('To collect a component from the current folder, type: Get \'key name\'')
        print('Type \'exit\' at any time to quit the program')
        print('************************************************************************************************')

    #the status function which will inform the player where they are and where they can go
    def status(current_room):
        print('You are in the', current_room, 'folder.')
        print('So far you have collected:', player_inventory)
        print('Your options for moving are:')
        possible_moves=[]
        if current_room in rooms:
            room = rooms[current_room]
            possible_moves = [direction for direction in room.keys() if direction in ['IN', 'UP', 'DOWN', 'BACK']]
        #is set to print possible moves because I think its a little more user friendly,
        #could be removed though
        print(possible_moves)
        if rooms[current_room]['Key'] != 'None':
            print('The component in the room is the', rooms[current_room]['Key'])
        else:
            print('There is no component in this room.')
        return possible_moves

    #the function validate if there is a component, and retrieve it component
    def get_component(current_room):
        current_key = rooms[current_room]['Key']
        #if the value of key isnt none
        if current_key != 'None':
            #add the word the to the front for better inventory printing
            collected_key = 'the' + ' ' + current_key
            #add the rooms component to the player inventory
            player_inventory.append(collected_key)
            #set the rooms key to none
            rooms[current_room]['Key'] = 'None'
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('You collected found', collected_key, '! You are one step closer to saving the world!')
        #if the value of the key is none, print an error
        else:
            print('============================There is no key in this room!============================')



    #set the starting room and a few variables
    current_room = 'DOOMBOT Main'
    player_inventory = []
    instructions()
    game_over = False
    #a full list of items to check if user has all items
    comp_list = 'the NUMBER', 'the ORDER', 'the LOWERCASE LETTER', 'the UPPERCASE LETTER', 'the SYMBOL', 'the LOCATION'
    #loop until the user enters the exit room
    while game_over != True:
        #initalize the possible moves variable and prompt the user for a move
        possible_moves = status(current_room)
        move = input('Please enter a command:').upper()
        words = move.split()
        #check if the move is exit, if so, double check that the user wants to quit
        #loop the double check until valid input, if yes, set room to exit, if no return to main loop
        if move == 'EXIT':
            check = ''
            while check != 'N':
                check = input('Are you sure you would like to quit? Y/N').upper()
                if check == 'Y':
                    print('Thanks for playing!')
                    game_over = True
                elif check == 'N':
                    print('Alright, lets keep going!')
                    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                else:
                    print('Invalid input. Please type "Y" or "N".')
       #check if the input is the expected length
        elif len(words) == 2 or 3:
            # if valid, retreive just the second word which should be the direction of move
            command = words
            next_move = command[1]
            #check if the direction is in the list of possible moves given the current room
            if next_move in possible_moves:
                #if it is, change the current room based on the input and print a divider
                current_room = rooms[current_room][next_move]
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            #if the first word is get
            elif words[0] == 'GET':
                #and there are 3 words, accounts for the components uppercase/lowercase letter
                if len(words) == 3:
                    #then the user is trying to get the last two words as the components
                    reqd_comp = words[1] + ' ' + words[2]
                #but if its just 2 words
                elif len(words) == 2:
                    #the desired component is the second word
                    reqd_comp = words[1]
                #otherwise, error
                else:
                    print('============================That component isnt in this room!============================')
                #if the requested item is in the current room, run the get_component() using the current room
                if reqd_comp == rooms[current_room]['Key']:
                        get_component(current_room)
                #if the requested item is not in the current room, error
                else:
                    print('============================That component isnt in this room!============================')
            else: #if not a valid move, and dosent start with 'Get', movement error
                print('============================INVALID MOVE. PLEASE TRY AGAIN============================')


        else:#if the input is too long or not long enough, throw error.
            print('============================INVALID INPUT. PLEASE TRY AGAIN============================')
            print('====================DON\'T FORGET TO TYPE "GO" BEFORE YOUR DIRECTION!===================')
        #if the current room is ever destroy the world, the player ran into the DOOMBOT and lost the game
        if current_room == ('DESTROY THE WORLD'):
            print('You have run into the DOOMBOT! It now knows you are snooping around '
                  'and has lock you and any hope of saving humanity out!')
            print('(◡︵◡)=============(╥﹏╥)=============GAME OVER=============(╥﹏╥)=============(◡︵◡)')
            #stop the main gameplay loop
            game_over = True
        #if the player ever has all the components in their inventory, stop the main gameplay loop
        if all(components in player_inventory for components in comp_list):
            print('You have successfully collected all the components! The world is saved!')
            print('(^▽^) ˗ˏˋ ★ ˎˊ˗ (ง •̀ゝ•́)ง ˗ˏˋ ★ ˎˊ˗ GAME OVER ˗ˏˋ ★ ˎˊ˗ (ง •̀ゝ•́)ง ˗ˏˋ ★ ˎˊ˗ (^▽^)')
            print('Thanks for playing!')
            game_over = True
#the replay prompt as a fucntion
def replay():
    #loop
    while True:
        #ask user if they want to replay and normalize input
        response = input("Do you want to replay the program? Y/N: ").strip().upper()
        if response == 'Y':
            #if yes, replay is true
            return True
        elif response == 'N':
            #if no, replay is false
            return False
        #if not a valid input, reprompt
        else:
            print("Please enter Y or N.")
#the whole program as a function
def main_loop():
    #loop
    while True:
        #the main gameplay
        main()
        #until the replay prompt returns false
        if not replay():
            print('Thanks for playing!')
            #end the program
            break

main_loop()