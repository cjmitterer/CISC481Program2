import ast
import sudoku_constraints

from math import sqrt

#with open("sudoku-constraints.py") as constraints_file:
 #  constraints_file:
  #  csp = ast.literal_eval(constraints_file.read())

simplePuzzle = [[1, None, None, None],
                [None, 2, None, None],
                [None, 4, None, None],
                [None, None, None, 3]]
puzzleOne = [[7,    None, None, 4,    None, None, None, 8,    6],
             [None, 5,    1,    None, 8,    None, 4,    None, None],
             [None, 4,    None, 3,    None, 7,    None, 9,    None],
             [3,    None, 9,    None, None, 6,    1,    None, None],
             [None, None, None, None, 2,    None, None, None, None],
             [None, None, 4,    9,    None, None, 7,    None, 8],
             [None, 8,    None, 1,    None, 2,    None, 6,    None],
             [None, None, 6,    None, 5,    None, 9,    1,    None],
             [2,    1,    None, None, None, 3,    None, None, 5]]
puzzleTwo = None
puzzleThree = None
puzzleFour = None
puzzleFive = None

def print_hi(name):
    print(f'Hi, {name}')


# 1

fourxFourDomainPuzzle = {
    'C11': [1],
    'C12': [1, 2, 3, 4],
    'C13': [1, 2, 3, 4],
    'C14': [1, 2, 3, 4],

    'C21': [1, 2, 3, 4],
    'C22': [2],
    'C23': [1, 2, 3, 4],
    'C24': [1, 2, 3, 4],

    'C31': [1, 2, 3, 4],
    'C32': [1, 2, 3, 4],
    'C33': [3],
    'C34': [1, 2, 3, 4],

    'C41': [1, 2, 3, 4],
    'C42': [1, 2, 3, 4],
    'C43': [1, 2, 3, 4],
    'C44': [4]
}

fourxFourDomainPuzzleBroken = {
    'C11': [1],
    'C12': [1, 2, 3, 4],
    'C13': [1, 2, 3, 4],
    'C14': [1, 2, 3, 4],

    'C21': [1, 2, 3, 4],
    'C22': [2],
    'C23': [1, 2, 3, 4],
    'C24': [1, 2, 3, 4],

    'C31': [1, 2, 3, 4],
    'C32': [1, 2, 3, 4],
    'C33': [3],
    'C34': [1, 2, 3, 4],

    'C41': [1, 2, 3, 4],
    'C42': [1, 2, 3, 4],
    'C43': [1, 2, 3, 4],
    'C44': [4]
}


fourxFourConstraints = {
    ('C11', 'C12'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C13'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C31'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C12', 'C13'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C13', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C14', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C14', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C14', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C14', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C21', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C31'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C22', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C22', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C22', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C22', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C23', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C23', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C23', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C24', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C24', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C31', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C32', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C32', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C32', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C32', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C33', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C33', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C33', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C34', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C34', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C41', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C41', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C41', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C42', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C42', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C43', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
}

# 1 TODO
nineXNineConstraints = sudoku_constraints.nineXNineConstraints

# 2 TODO
# May need to sort var1 and var2

# Inputs:
#   domains: this is the list



def helper(i, c1, c2, domain):
    for j in domain:
        if c1 is not None and [i, j] in c1 or c2 is not None and [i, j] in c2:
            return True
    return False

# Uses list comprehension, iterate over a list easily

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

    smallestVal = minimumRemainingValues(constraints, domainCopy, assignments)

    for i in range(len(domainCopy[smallestVal])):
        possibleCandidate = domain[smallestVal][i]
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
    retval = not AC3(constraints, domain)
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
                newPuzzleDict[builtKey] = unsolved
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
    #print(len(nineXNineConstraints))
    print(puzzleConverter(puzzleOne))