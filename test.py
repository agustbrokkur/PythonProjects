from itertools import product, permutations
import numpy as np


def prufa1(A, c):
    B = A[:]
    if len(B) == 1 or c[0] == 0:
        rowStart = 0
    else:
        rowStart = c[0] - 1
    if len(B) - 1 == c[0]:
        rowEnd = c[0]
    else:
        rowEnd = c[0] + 1

    if len(B[0]) == 1 or c[1] == 0:
        colStart = 0
    else:
        colStart = c[1] - 1
    if len(B[0]) - 1 == c[1]:
        colEnd = c[1]
    else:
        colEnd = c[1] + 1

    counter = 0
    for row in xrange(rowStart, rowEnd + 1):
        for col in xrange(colStart, colEnd + 1):
            if B[row][col] == 1 and not (row == c[0] and col == c[1]):
                counter += 1

    if B[c[0]][c[1]] == 1:
        if counter <= 1 or counter >= 4:
            return 0
        elif counter == 2 or counter == 3:
            return 1
    else:
        if counter == 3:
            return 1
        else:
            return 0


def prufa2(A):
    B = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    #B = [[0]*len(A[0])]*len(A)
    for row in xrange(len(A)):
        for col in xrange(len(A[0])):
            k = prufa1(A, (row, col))
            B[row][col] = k
    return B



def checkFiveO(A):
	Base = [x[:] for x in A] # 0
	First = prufa2(Base[:]) # 1
	Second = prufa2(First[:]) # 2
	Third = prufa2(Second[:]) # 3
	Fourth = prufa2(Third[:]) # 4
	Fifth = prufa2(Fourth[:]) # 5
	PreviousCheck = Base == First or First == Second or Second == Third \
					or Third == Fourth or Fourth == Fifth
	BeforeLastCheck = Base == Second or First == Third \
					or Second == Fourth or Third == Fifth
	if PreviousCheck or BeforeLastCheck:
		return False
	return (Base == Third or Base == Fourth or Base == Fifth)

returnList = []
checkedList = []
# Decides the starting NxN matrix size
count = 1
# Number of states to be found
maxStates = 50
while True:
	# Takes all the ways you can arrange 1 and 0 in a list of size count and returns them as a list
	#subList = [list(x) for x in product([0, 1], repeat=count)]
	# Takes all the ways you can arrange the subLists above into a list of size count and returns them as a list
	matrixList = [list(x) for x in permutations([list(x) for x in product([0, 1], repeat=count)], count)]
	for matriz in matrixList:
		if checkFiveO(matriz) and matriz not in returnList and matriz not in checkedList:
			returnList.append(matriz)

			reverseMatrix = matriz[::-1]
			flipMatrix = np.fliplr(matriz).tolist()[:]
			reverseFlipMatrix = flipMatrix[::-1]

			checkedList.append(matriz)
			checkedList.append(reverseMatrix)
			checkedList.append(flipMatrix)
			checkedList.append(reverseFlipMatrix)

			print "\nMatrix number: ", len(returnList)
			for a in matriz:
				print a
			if maxStates <= len(returnList):
				print returnList
	count += 1
print returnList
