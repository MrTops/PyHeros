"""
contians generic enemy
"""

class GenericEnemy(object):
    """
    class defining basic traits of a enemy
    """
    def __init__(self, name):
        """only need name
           health and power are controled by level (such like ch)
        """
        self.name = name