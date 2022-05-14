import ast
import sudoku_constraints
import puzzles

from math import sqrt


def print_hi(name):
    print(f'Hi, {name}')



# 1 TODO
nineXNineConstraints = sudoku_constraints.nineXNineConstraints
fourXFourConstraints = sudoku_constraints.fourXFourConstraints

# 2 TODO
# May need to sort var1 and var2


def helper(i, c1, c2, domain):
    for j in domain:
        if c1 is not None and [i, j] in c1 or c2 is not None and [i, j] in c2:
            return True
    return False


# Uses list comprehension, iterate over a list easily
# Inputs:
#   domains: this is the list
def revise(constraints, domain, var1, var2):
    #print(domain)
    initial = len(domain[var1])


    c1 = constraints.get((var1, var2))
    c2 = constraints.get((var2, var1))
    domain[var1][:] = [i for i in domain[var1] if helper(i, c1, c2, domain[var2])] # Helper returns true or false, if true something doesn't
    return initial != len(domain[var1]) # If size changes something got removed

"""
def revise(CSP, var1, var2):
    values1 = [CSP[k] for k in CSP.keys() if k[0] == var1 or k[1] == var1]
    values2 = [CSP[k] for k in CSP.keys() if k[0] == var2 or k[1] == var2]
    for x in values1:
        for y in values2:
            if () and x != y:
                revised = True
                #remove x from values1
                break
"""

# 3 TODO
#BADDDD
# If nothing in domain, just die
def AC3(constraints, domain):
    arc = list(constraints)
    #print(arc)
    for x in domain:
        if len(domain[x]) == 0:
            return False
    while arc:
        (xi, xj) = arc.pop(0)
        if(revise(constraints, domain, xi, xj)):
            if(len(domain[xi]) == 0):
                return False
            """for xk in arc[xi]:######THIS IS WRONG FIND Working ROUTE, SORT xk and xi?
                if xk != xi:
                    arc.append((xk, xi))"""
            arc.append((xj, xi))
        #if c1 is not None and [i, j] in c1 or c2 is not None and [i, j] in c2
    return True



# 4 TODO
# ALSO BAD
def minimumRemainingValues(constraints, domain, assignments):
    currentMin = float("inf") #Some large number to be overwritten immeidately
    location = None
    for x in domain:
        # if(len(domain[x]) < currentMin and len(domain[x]) > 1):
        if len(domain[x]) < currentMin and x not in assignments:
            currentMin = len(domain[x])
            location = x
    return location

# 5 TODO

def backTrackingSearch(constraints, domain, assignments = {}):
    domainCopy = domain.copy()
    if isWrong(constraints, domainCopy, assignments):
        return None
    if isComplete(constraints, domainCopy, assignments):
        return assignments
    assignmentsBackup = assignments.copy()
    print(assignmentsBackup)
    smallestVal = minimumRemainingValues(constraints, domainCopy, assignments)
    #print(smallestVal)
    for i in range(len(domainCopy[smallestVal])):
        possibleCandidate = domainCopy[smallestVal][i]                                                          # Changed Domain Copy
        #print(possibleCandidate)
        assignmentsBackup[smallestVal] = [possibleCandidate] # First function/expansion

        backTrackProgess = backTrackingSearch(constraints, domainCopy.copy(), assignmentsBackup)
        if backTrackProgess is not None:
            return backTrackProgess
    return None

    #return None #If reached it has failed

# Helper
def isComplete(constraints, domain, assignments):

    if len(assignments) != len(domain):
        return False
    for x in assignments:
        if assignments[x][0] not in domain[x]:
            return False

    dummyassign = assignments.copy()
    return AC3(constraints, dummyassign) # If anything is removed it was not correct

def isWrong(constraints, domain, assignments):
    for x in assignments:
        domain[x] = assignments[x].copy()
    retval = not AC3(constraints, domain.copy())
    return retval

def puzzleConverter(puzzleArray):
    puzzlewidth = len(puzzleArray)
    unsolved = []
    for i in range(puzzlewidth):
        unsolved.append(i+1)

    newPuzzleDict = {}
    for i in range(puzzlewidth):
        for j in range(puzzlewidth):
            builtKey = "C"+str(i+1)+str(j+1)
            if puzzleArray[i][j] is None:
                newPuzzleDict[builtKey] = unsolved.copy() # Need .copy(
            else:
                newPuzzleDict[builtKey] = [puzzleArray[i][j]]

    return newPuzzleDict

def urlToBoard(urlBoard):
    boardRowSize = sqrt(len(urlBoard))
    newBoard = [boardRowSize][boardRowSize]
    for i in range(urlBoard):
        newBoard[i/boardRowSize][i%boardRowSize] = urlBoard[i]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hellow World")
    #print(fourxFourConstraints.get(('C11', 'C12')))
    #print(revise(fourxFourConstraints, fourxFourDomainPuzzle, 'C11', 'C12'))
    #print(AC3(fourxFourConstraints, fourxFourDomainPuzzle))
    #print(AC3(fourxFourConstraints, fourxFourDomainPuzzleBroken))
    #print(minimumRemainingValues(fourxFourConstraints, fourxFourDomainPuzzle, ['C11']))
    #print(backTrackingSearch(fourxFourConstraints, fourxFourDomainPuzzle))
    #print(backTrackingSearch(fourxFourConstraints, fourxFourDomainPuzzleBroken))



    #print(fourxFourDomainPuzzle)
    #print(puzzleConverter(simplePuzzle))
    #print(backTrackingSearch(fourxFourConstraints, fourxFourDomainPuzzle))
    #print(backTrackingSearch(fourxFourConstraints, puzzleConverter(simplePuzzle)))
    print(backTrackingSearch(fourXFourConstraints, puzzleConverter(puzzles.simplePuzzle)))
    print(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleOne)))