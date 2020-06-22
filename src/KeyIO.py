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

    def hookEvent(self, keyName, firedFunction, allowSpam = False):
        """
        adds a key to the stack
        function is called upon key press

        @param
        callOnDown = True
        weither or not to call upon key down or key up, default to down (true)
        """
        try:
            self.eventStack[keyName] = firedFunction, allowSpam
        except:
            raise Exception("an error occured whilst hooking \"${}\", if this error persists please contact a developer".format(keyName))

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