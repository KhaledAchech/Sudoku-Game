"""
This is a Sudoku solver game made 
with Backtracking algorithme
"""

#Board exemple 
board = [
    [7,8,' ',4,' ',' ',1,2,' '],
    [6,' ',' ',' ',7,5,' ',' ',9],
    [' ',' ',' ',6,' ',1,' ',7,8],
    [' ',' ',7,' ',4,' ',2,6,' '],
    [' ',' ',1,' ',5,' ',9,3,' '],
    [9,' ',4,' ',6,' ',' ',' ',5],
    [' ',7,' ',3,' ',' ',' ',1,2],
    [1,2,' ',' ',' ',7,4,' ',' '],
    [' ',4,9,2,' ',6,' ',' ',7]
]

#print function to have a better visual representation 
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#Before Solving
print('Before :\n')
print_board(board)
print('\n')
print("- - - - - - - - - - - - \n")

#Solving the board 
#(more like adding and checking each time the added value and backtracking if it's not valdi :) ).
def solve(bo):

	find = find_empty(bo)
	#if the board is solved
	if not find:
		return True
	else :
		row, col = find

	for i in range(1,10):
		if valid(bo, i, (row, col)):
		# if valid the value will be added to the board
			bo[row][col] = i
			if solve(bo):
				return True

			#reseting the found value for the backtracking	
			bo[row][col] = ' '

	return False


#find out if the insert is valid or not
def valid(bo, num, pos):#board, number and position
	
	#check row
	for i in range(len(bo[0])):
		if bo[pos[0]][i] == num and pos[1] != i:
			return False

	#check column
	for i in range(len(bo)):
 		if bo[i][pos[1]] == num and pos[0] != i :
 			return False

    #check box
	# Check box
	box_x = pos[1] // 3
	box_y = pos[0] // 3
    
    #looping through the whole box.
	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if bo[i][j] == num and (i,j) != pos:
				return False
	
	return True


#find the empty spot 
def find_empty(bo):
	for i in range(len(bo)):
		for j in range(len(bo[0])):
			if bo[i][j] == ' ':
				return (i,j) #row,col

	#if there's no more blank spots			
	return None

#calling the solve function and printing the new board :) .
solve(board)
print('After :\n')
print_board(board)

