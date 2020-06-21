import KeyIO
newIO = KeyIO.KeyIO()

def aDown(e):
    print("a is down")

newIO.hookEvent('a', aDown)
newIO.start()
input()