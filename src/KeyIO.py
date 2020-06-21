"""
a class to handle keyboard events
"""

from packages import keyboard

class KeyIO(object):
    """
    Hooks key events
    """
    def __init__(self):
        self.downEventStack = {}
        self.upEventStack = {}
        self.running = False

    def hookEvent(keyName, firedFunction, callOnDown = True):
        """
        adds a key to the stack
        function is called upon key press

        @param
        callOnDown = True
        weither or not to call upon key down or key up, default to down (true)
        """
        try:
            if callOnDown:
                self.downEventStack[keyName] = firedFunction
            elif not callOnDown:
                self.upEventStack[keyName] = firedFunction
            else:
                raise ValueError("given argument \"callonDown\" was not valid, if this error persists please contact a developer")
        except:
            raise Exception("an error occured whilst hooking \"${}\", if this error persists please contact a developer".format(keyName))

    def start():
        """
        starts for keys
        """
        def calledFunction(e, down):
            try:
                if self.running:
                    allowed = False
                    if e.name in self.downEventStack.keys() and down: allowed = True
                    if e.name in self.upEventStack.keys() and not down: allowed = True

                    if allowed:
                        if down:
                            self.downEventStack[e.name](e)
                        elif not down:
                            self.upEventStack[e.name](e)
                        else:
                            raise ValueError("an error occured when firing a key ${} event, if this error persists please contact a developer".format(down))
            except:
                raise Exception("an error occured, if this error persists please contact a developer")

        keyboard.on_press(calledFunction)
        keyboard.on_release(calledFunction)