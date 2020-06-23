"""
a class to handle keyboard events
"""

import keyboard

class KeyIO(object):
    """
    Hooks key events
    """
    def __init__(self):
        self.eventStack = {}
        self.stickStack = []
        self.running = False

    def hookEvent(self, keyName, allowSpam = False):
        """
        adds a key to the stack
        function is called upon key press

        @param
        callOnDown = True
        weither or not to call upon key down or key up, default to down (true)
        """
        def func_wrapper(func):
            try:
                self.eventStack[keyName] = func, allowSpam
            except:
                raise Exception("an error occured whilst hooking \"${}\", if this error persists please contact a developer".format(keyName))
        return func_wrapper
    
    def unhookAll(self):
        """unhooks all current keybinds"""
        self.eventStack = {}
        self.stickStack = []
    
    def unhook(self, keyName):
        """
        attempts to unhook a single keyname
        """

        try:
            if keyName in self.eventStack.keys():
                self.eventStack[keyName] = None
            
            if keyName in self.stickStack.keys():
                self.stickStack.remove(keyName)
        except:
            raise ValueError("given keyname is not in stack :(, if this error persists please contact a developer")

    def start(self):
        """
        starts for keys
        """
        self.running = True

        def calledFunction(e):
            try:
                if self.running:

                    if keyboard.is_pressed(e.name):
                        allowed = False

                        if e.name in self.eventStack.keys():
                            allowed = True

                        if allowed:
                            allowed = False

                            foundEvent = self.eventStack[e.name]

                            if foundEvent[1]:
                                allowed = True
                            elif not e.name in self.stickStack:
                                allowed = True
                                self.stickStack.append(e.name)
                            else:
                                allowed = False
        
                            if allowed:
                                foundEvent[0](e)
                    elif not keyboard.is_pressed(e.name):
                        if e.name in self.stickStack:
                            self.stickStack.remove(e.name)


            except:
                raise Exception("an error occured, if this error persists please contact a developer")

        keyboard.hook(calledFunction)

    
    def stop(self):
        self.running = False