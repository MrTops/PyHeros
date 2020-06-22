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

        def test(e):
            print("you touched {}".format(e.name))
        
        self.KIO.hookEvent("e", test)
        self.KIO.start()

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
        