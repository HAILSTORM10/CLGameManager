print('Welcome to The Number 1 Game tracker!. What would you like to do? \n 1 - Add game \n 2 - List Games \n Exit - Close program')


arrGames = []

def UserChoice():
    if Choice == '1':
            print('You have chosen to add a game.')
            tFile = open('Tracking.txt', 'a')
            sName = input('Enter name of Game: ')
            tFile.write(f'{sName}\n')
            print(f'{sName} has been saved!')
            #Main()
            tFile.close()
    elif Choice == '2':
        tFile = open('Tracking.txt', 'r+')
        for Game in tFile:
            arrGames.append(Game) 
        print(arrGames)
        tFile.close()

def Main():
    global Choice 
    Choice = ''
    while Choice.upper() != 'EXIT':    
        Choice = input('What will you be doing: ')
        UserChoice()
    else:
        print('Bye Bye!')

Main()
#UserChoice(Choice)
