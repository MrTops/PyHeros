"""
Runs the game
"""

from src import Game

def main():
    gameInstance = Game.Game()
    gameInstance.aliveThread()
    gameInstance.mainMenu()

main()