# RUN "WebSite".py" to get to the website

import ast
import sudoku_constraints
import puzzles
import copy


from math import sqrt


def print_hi(name):
    print(f'Hi, {name}')



# 1
# Located in sudoku_constraints and puzzles
nineXNineConstraints = sudoku_constraints.nineXNineConstraints
fourXFourConstraints = sudoku_constraints.fourXFourConstraints


# 2
# Helper function used to
def helper(i, c1, c2, domain):
    for j in domain:
        if c1 is not None and [i, j] in c1 or c2 is not None and [i, j] in c2:
            return True
    return False


# Uses list comprehension, iterate over a list easily
# Inputs:
#   constraints: the CSP constraints
#   domains: this is the incomplete sudoko board
#   var1: The value to be compared against var2 and be removed if its in var2
#   var2: The value to be compared against var1 and if var2 has the same values in var1 will lose values
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

# 3
# AC3 function that checks for all the possible issues and calls revise based on the inputs
# Inputs:
#   constraints: the CSP constraints
#   domains: this is the incomplete sudoko board
# Output:
# Boolean: indicating whether or not all variables have at least on value left in their domains
# Effects:
# calls revise and removes values from Xi that is in Xj
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



# 4
# minimumRemainingValues function returns the fewest values in its domain among the unassigned variables in the CSP
#   constraints: the CSP constraints, not used but used for consistency to represent the CSP
#   domains: this is the incomplete sudoko board
#   assignments: the list of values to be checked and based on
# Returns:
# location: the value that has the fewest remaining values
def minimumRemainingValues(constraints, domain, assignments):
    currentMin = float("inf") #Some large number to be overwritten immeidately
    location = None
    for x in domain:
        # if(len(domain[x]) < currentMin and len(domain[x]) > 1):
        if len(domain[x]) < currentMin and x not in assignments:
            currentMin = len(domain[x])
            location = x
    return location

# 5
# backtracks through a provided sudoku board and finds a solution
# Inputs:
# constraints: simple constraints dictionary of acceptable inputs
# domain: the board that is attempting to be solved
# assignments: initially empty it is the growing list of potential board assignments
# Outputs:
# assignments: When complete it return a full dictionary of all the assignments made in order of being added
# This can be used to get the order a board can be filled
def backTrackingSearch(constraints, domain, assignments = {}):
    #domainCopy = domain.copy()
    domainCopy = copy.deepcopy(domain)
    if isWrong(constraints, domainCopy, assignments):
        return (None, None)
    if isComplete(constraints, domainCopy, assignments):
        return (assignments, [domainCopy])
    #assignmentsBackup = assignments.copy()
    assignmentsBackup = copy.deepcopy(assignments)
    #print(assignmentsBackup)
    smallestVal = minimumRemainingValues(constraints, domainCopy, assignments)
    #print(smallestVal)
    for i in range(len(domainCopy[smallestVal])):
        possibleCandidate = domainCopy[smallestVal][i]                                                          # Changed Domain Copy
        #print(possibleCandidate)
        assignmentsBackup[smallestVal] = [possibleCandidate] # First function/expansion

        backTrackProgess, domainList = backTrackingSearch(constraints, domainCopy.copy(), assignmentsBackup)
        if backTrackProgess is not None:
            domainList.insert(0, domainCopy)
            return (backTrackProgess, domainList)
    return (None, None)

    #return None #If reached it has failed

# isComplete: Helper function that checks if the board is complete
#   constraints: the CSP constraints, not used but used for consistency to represent the CSP
#   domains: this is the incomplete sudoko board
#   assignments: the list of values to be checked and based on
# Returns:
# False if it fails: the amount in domains is too large, checks the assignments against domains and
# And if none of the Falses are checked it checks AC3 with the new copied assignments
def isComplete(constraints, domain, assignments):

    if len(assignments) != len(domain):
        return False
    for x in assignments:
        if assignments[x][0] not in domain[x]:
            return False

    dummyassign = assignments.copy()
    return AC3(constraints, dummyassign) # If anything is removed it was not correct

# isWrong: helper function that checks if there is inconsistencies, this is done so by calling
# AC3 with the constraints and a copy of domain
# Inputs:
#   constraints: the CSP constraints, not used but used for consistency to represent the CSP
#   domains: this is the incomplete sudoko board
#   assignments: the list of values to be checked and based on
# Returns:
# reval: A boolean for whether there is a detected wrong and to then be used break out of the backtracking function
def isWrong(constraints, domain, assignments):
    for x in assignments:
        domain[x] = assignments[x].copy()
    retval = not AC3(constraints, domain.copy())
    return retval

# puzzleConverter: Converts a 2d array into a dictionary to be used as a domain for other functions
# Inputs:
# puzzleArray: simple 2d array of a possible where all empty spots are None
# Outputs:
# newPuzzleDict: a dictionary version of the 2d array where all None values are replaced with the max amount of numbers
# and the keys are generated
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

# urlBoard: Function that converts the website URL to a 2d array
# representing the given board state
# Inputs:
# urlBoard: generated as a string that is the size of the amount of cells with n representing null and the numbers
# Outputs:
# newBoard: 2d array conversion of the url string, this can then be converted to a dictionary and be used as a domain
def urlToBoard(urlBoard):
    boardRowSize = int(sqrt(len(urlBoard)))
    newBoard = [[None]*boardRowSize for i in range(boardRowSize)]
    for i in range(len(urlBoard)):
        if(urlBoard[i] != "n"):
            newBoard[i//boardRowSize][i%boardRowSize] = int(urlBoard[i])
        else:
            newBoard[i//boardRowSize][i%boardRowSize] = None
    return newBoard

# Helper Function that prints the entire process of filling out a sudoko board when given a solved dictionary
# Inputs:
# A solved dictionary in order of when values were added
# Returns:
# Void
# Effects:
# Prints out each board state for all 81 cells
def boardPrinter(boardLore):
    puzzleArray = [[0 for x in range(9)] for y in range(9)]

    for x in boardLore:
        xint = int(x[1])        # C27 - xint = 2
        yint = int(x[2])
        #print(xint+yint)
        correctValue = boardLore[x]
        correctValue = correctValue[0]
        puzzleArray[xint-1][yint-1] = correctValue
        #
        for i in range(9):
            for j in range(9):
                if(j < 8):
                    print(puzzleArray[i][j], end=" ")
                else:
                    print(puzzleArray[i][j])
        print("")


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
    #print(backTrackingSearch(fourXFourConstraints, puzzleConverter(puzzles.simplePuzzle)))

    #print(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleTwo)))
    #print(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleThree)))
    #print(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleFour)))
    #print(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleFive)))



    #print(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleThree)))
    #holder = backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleOne))
    #print(boardPrinter(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleOne))))
    #print(boardPrinter(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleTwo))))
    #print(boardPrinter(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleThree))))
    #print(boardPrinter(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleFour))))
    #print(boardPrinter(backTrackingSearch(nineXNineConstraints, puzzleConverter(puzzles.puzzleFive))))

