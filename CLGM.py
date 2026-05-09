import sys
import subprocess
import os

dictGame = {}

def UserChoice():
    
    if sChoice.upper() == 'ADD':
            
            if os.path.exists('Game.txt'): # File Exists
               
                #Add a game
                print('Adding a game...')
                
                #First, check if the game already exists
                tFile = open('Game.txt', 'r+')
                for GameName in tFile:
                    if sys.argv[2] == GameName.split(' | ')[0]:
                        print('Game with same name already exists!')
                        exit()
            else:
                 tFile = open('Game.txt', 'w+')    #Create the File
                
            #Game doesn't exist, add it
            tFile.write(f'{sys.argv[2]} | {sys.argv[3]} \n')
            print(f'{sys.argv[2]} has been saved!')
            tFile.close()    
    
    elif sChoice.upper() == 'LIST':
        print('Listing Games...')
        tFile = open('Game.txt', 'r+')
        #Loop through File
        for GameName in tFile: 
            dictGame = {'Name':GameName.split(' | ')[0], 'Location':GameName.split(' | ')[1]}
            print(f'Name: {dictGame.get('Name')} \nLocation: {dictGame.get('Location')}') #Display Game Name and Location
        tFile.close()
    
    elif sChoice.upper() == 'START':
        #'''
        tFile = open('Game.txt', 'r+')
        #Loop through File
        for GameName in tFile:
           dictGame = {'Name':GameName.split(' | ')[0], 'Location':GameName.split(' | ')[1]}
           if sys.argv[2].upper() == dictGame.get('Name').upper() : #If requested game is found
            print('Game found!')
            subprocess.run(dictGame.get('Location'))   #Start it
        tFile.close
        #'''
    
    elif sChoice.upper() == 'DELETE':
        print('Deleting a game...')
        arrGames = []
       
        tFile = open('Game.txt', 'r+') #Loop through and collect every game except chosen one
        for GameName in tFile:
            dictGame = {'Name':GameName.split(' | ')[0], 'Location':GameName.split(' | ')[1]}
            if dictGame.get('Name').upper() != sys.argv[2].upper():
                arrGames.append(dictGame)
        tFile.close()

        tFile = open('Game.txt', 'w+') #Re-wrtie collected gam
        for i in arrGames:
            print(i)
            tFile.write(f"{i.get('Name')} | {i.get('Location')}")
        tFile.close()
            



if sys.argv[1].upper() == 'HELP':
    print('Welcome to the Command Line Game Manager!\nYou can ADD, DELETE, LIST and START games that you have already added!')
else:
    sChoice = sys.argv[1]
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    UserChoice()
    
    