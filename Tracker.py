#print('Welcome to The Number 1 Game tracker!. What would you like to do? \n 1 - Add game \n 2 - List Games \n Exit - Close program')
import sys
import subprocess

arrGames = []
dictGame = {}

def UserChoice():
    
    if sChoice.upper() == 'ADD':
            
            print('You have chosen to add a game.')
            tFile = open('Tracking.txt', 'a')
            #sName = sys.argv[2]
            #sExec = sys.argv[3]
           # sEntry = {'Name':sys.argv[2]} | {'Location':sys.argv[3]}
            tFile.write(f'{sys.argv[2]} | {sys.argv[3]} \n')
            print(f'{sys.argv[2]} has been saved!')
            tFile.close()
    
    elif sChoice.upper() == 'LIST':
        tFile = open('Tracking.txt', 'r+')
        for GameName in tFile:
            dictGame = {'Name':GameName.split(' | ')[0], 'Location':GameName.split(' | ')[1]}
            print(f'{dictGame.get('Name')} - {dictGame.get('Location')}')
        tFile.close()
    
    elif sChoice.upper() == 'START':
        tFile = open('Tracking.txt', 'r+')
        for GameName in tFile:
           dictGame = {'Name':GameName.split(' | ')[0], 'Location':GameName.split(' | ')[1]}
           if sys.argv[2].upper() == dictGame.get('Name').upper() :
            print('Game found!')
            subprocess.run(dictGame.get('Location'))   
        tFile.close
        
         

if sys.argv[1] != '':
    sChoice = sys.argv[1]
    UserChoice()
