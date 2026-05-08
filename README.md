# The Command-Line Game Manager!
## Add, Delete, List and Start your games, all from a CLI

### Installation
Download the provided "CLGM.py" file from the repository/
(Will create an extra file once ran)/
Requires Python/
Can be added to System PATH variable for global access/

### Use
Adding Games
  CLGM.py add <Name of Game> <Path to Game .exe>\
  For example:\
  CLGM.py add Muck D:\SteamLibrary\steamapps\common\Muck\Muck.exe

Deleting Games
  CLGM.py delete <Name of Game>\
  For Example:\
  CLGM.py Delete Muck

Listing Games\
  CLGM.py List

Starting Games
  CLGM.py start <Name of Game>\
  For Example:\
  CLGM.py start Muck\

### Known Issue
Emulator Support
  Support is limitted
  Testing shows support for Dolphin Emulator but not PCSX2-QT
  For Example:
  CLGM.py add EmulatedGame "C:\Emulator.exe" "C:\Game.iso"
