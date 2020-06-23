"""
Handles all of the input output and displaying "graphics" to the screen
"""

from src import KeyIO
from src import Datahandler
import os
import time
import threading

class Game(object):
    def __init__(self):
        self.KIO = KeyIO.KeyIO()
        self.KIO.start()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def aliveThread(self):
        """
        generates a thread to keep the game running
        """
        def runFunction():
            while True:
                time.sleep(10000)

        newThread = threading.Timer(1000000, runFunction)
        newThread.setName("alive_thread")
        newThread.start()
        return newThread
    
    def playGame(self):
        self.clear()
        print("There is not game, press 'b' to return")
        self.KIO.unhookAll()

        @self.KIO.hookEvent('b')
        def mainMenu(e):
            self.mainMenu()
    
    def settings(self):
        self.clear()
        print("There is no settings yet, press 'b' to return")
        self.KIO.unhookAll()

        @self.KIO.hookEvent('b')
        def mainMenu(e):
            self.mainMenu()
    
    def loadSave(self):
        self.clear()
        print("There is not a loading system, press 'b' to return")
        self.KIO.unhookAll()

        @self.KIO.hookEvent('b')
        def mainMenu(e):
            self.mainMenu()

    def exitGame(self):
        self.clear()
        os.abort()
        print("bye and thanks for playing")

    def mainMenu(self):
        self.clear()
        print("""
=================================================================================================
|Welcome to |PyHeros| the universe is in danger, we need your help. Go through levels and defeat|
|the monsters whom plague our universe. There are many difficulties but you can manage!         |
|The more monsters you kill, the more gold you make, use gold to upgrade yourself.              |
=================================================================================================
|SELECTIONS:                                                                                    |
|===============================================================================================|
|P: Play Game | S: Settings | L: Load A Save | E: exit                                          |
=================================================================================================
        """)

        self.KIO.unhookAll()

        @self.KIO.hookEvent('p')
        def hook(e):
            self.playGame()
        
        @self.KIO.hookEvent('s')
        def hook(e):
            self.settings()
        
        @self.KIO.hookEvent('l')
        def hook(e):
            self.loadSave()

        @self.KIO.hookEvent('e')
        def hook(e):
            self.exitGame()
        
        
        