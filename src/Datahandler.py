"""
contains useful methods to create and use data
"""

import json
import os

class PlayerData(object):
    @staticmethod
    def getDataFromFile(fileLocation):
        """
        returns a PlayerData object with the data loaded from the given file, if an error occurs it will return a default playerdata object
        """
        try:
            fileLocation += ".json"
            try:
                open(fileLocation, "r").close()
            except:
                open(fileLocation, "w+").close()
            
            data = ""
            for line in open(fileLocation, "r").readlines():
                data += line.rstrip("\n")
            try:
                jsonData = json.loads(data)
            except:
                print("Defaulting data, if this is a valid save, this could be an error. If this is a valid save please exit and try again. If the error persists please contact a developer. Check that you spelt the file name correctly.")                
                jsonData = {}
            newPlayerData = PlayerData()
            newPlayerData.loadDataFromJson(jsonData)
            return newPlayerData
        except:
            raise Exception("Error loading player data from {}, if the error persists please contact a developer".format(fileLocation))

    @staticmethod
    def saveDataToFile(fileLocation, playerData):
        """
        saves the playerData object to the fileLocation
        """
        try:
            json.dump(playerData.data, open(fileLocation + "-temp.json", "w+"))
            os.remove(fileLocation + ".json")
            os.rename(fileLocation + "-temp.json", fileLocation + ".json")
        except:
            raise Exception("Error saving player data, if the error persists please contact a developer")

    def __init__(self):
        self.data = {
            "gold": 0,
            "monstersKilled": 0
        }
    
    def loadDataFromJson(self, dict):
        try:
            for key in dict.keys():
                if key in self.data.keys():
                    self.data[key] = dict[key]
        except:
            raise Exception("Error loading data from a json dictionary, if the error persists please conatact a developer! :)")