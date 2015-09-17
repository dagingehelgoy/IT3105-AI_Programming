class AStarNode:
    MOVEMENT_COST = 1

    def __init__(self, parent):
        self.parent = parent
        self.gValue = 0
        self.hValue = 0
        self.fValue = self.gValue + self.hValue
        self.kids = []
        self.state = None

        self.state = self.calculateStateIndex()

    def checkIfGoalState(self):
        raise NotImplementedError

    def calculateStateIndex(self):
        raise NotImplementedError

    def __lt__(self, other):
        return self.fValue < other.fValue

    def set_gValue(self, newGValue):
        self.gValue = newGValue
        self.fValue = self.gValue + self.hValue

    def set_hValue(self, newHValue):
        self.hValue = newHValue
        self.fValue = self.gValue + self.hValue

    """Algorithm methods"""

    @staticmethod
    def calculateHeuristicValue(self):
        raise NotImplementedError

    @staticmethod
    def calculateGValue(self):
        raise NotImplementedError

    @staticmethod
    def generate_all_successors(self):
        raise NotImplementedError


