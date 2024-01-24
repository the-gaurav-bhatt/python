list = [0,0,0,0,0,0,0,0,0]
def drawBoard():
    counter = 0
    for element in list:
        counter= counter+1
        if(element==0):
            print('| '+ '' +" |",end=' ')
        else:
            print('| '+str(element) +" |",end=' ')
            
        if((counter%3)==0):
            print()

def hasWon(player):
    # Corrected the indices in the if conditions
    for i in range(0,9,3):
        if(list[i]==player and list[i+1]==player and list[i+2]==player): # indices start from 0
            return True
        
    for i in range(0,3,1):
        if(list[i]==player and list[i+3]==player and list[i+6]==player): # indices start from 0
            return True
    # Corrected the indices in the if conditions
    if((list[0]==player and list[4]==player and list[8]==player)or(list[2]==player and list[4]==player and list[6]==player) ): # indices start from 0
        return True
    return False # Added return False to handle the case when no winning condition is met

player = 'X'
while (hasWon(player)==False):
    if(hasWon(player)):
        print(player+' won the Game')
        continue
    drawBoard()
    print('-------------------')
    if(player=='X'):
        pos = int(input('Enter the position:'))
        list[pos-1] = 'X'
        player= 'O'
    else:
        pos = int(input('Enter the position:'))
        list[pos-1] = 'O'
        player='X'
    if(hasWon(player)):
        print(player+' won the Game')
        continue