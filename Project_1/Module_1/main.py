# coding=utf-8
import math
from heapq import heappush, heappop

MOVEMENT_COST = 1


def calculateHValue(initNode, goalNode):
    xOff = math.fabs(goalNode.X - initNode.X)
    yOff = math.fabs(goalNode.Y - initNode.Y)
    return xOff + yOff


def calculateGValue(initNode):
    return initNode.parent.g + MOVEMENT_COST


def generate_all_successors(x):
    pass


def best_first_search(initNode, goalNode, ):
    closedNodes = []
    openNodes = []
    initNode.g = calculateGValue(initNode)
    initNode.h = calculateHValue(initNode, goalNode)

    heappush(openNodes, initNode)

    while (True):
        if openNodes.count() == 0:
            print "No solution found"
            break
        x = heappop(open)
        heappush(closedNodes, x)
        if x.X == goalNode.X and x.X == goalNode.Y:
            print "Solution found!"
            break

        succ = generate_all_successors(x)

        for s in succ:
            # If node S* has previously been created, and if state(S*) = state(S), then S ← S*.
            x.kids.append(s)

