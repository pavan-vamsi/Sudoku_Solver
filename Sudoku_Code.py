N = 9   # default size of a Sudoku is 9

def isSafe(a,row,col,value):
    for i in range(9):      #checking if we found same number in the same row
        if a[row][i] == value:
            return False
        
    for i in range(9):      #checking if we found same number in the same column
        if a[i][col] == value:
            return False
    
    sRow = row - row%3
    sCol = col - col%3
    for i in range(3):      #checking if we found same number in the sub matrix of size 3*3
        for j in range(3):
            if a[i+sRow][j+sCol] == value:
                return False
            
    return True

def printing(a):    #to print the result of the Sudoku
    for i in range(N):
        for j in range(N):
            print(a[i][j], end=" ")
        print()
        
def solving(a,row,col):
    if(row == N-1 and col == N):    #To avoid further backtracking
        return True
    
    if col == N:    #if reaches the end of the column which is 9
        col = 0
        row+=1
    
    if a[row][col] > 0:     #if the slot contains already a value i.e. > 0 then we iterate to next value
        return solving(a,row,col+1)
    
    for i in range(1,N+1,1):
        if isSafe(a,row,col,i):
            a[row][col] = i
            
            if solving(a,row,col+1):
                return True
        a[row][col] = 0
    return False
    
# Taking a sample 9*9 Array which has a solution of Sudoku
a = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

if (solving(a, 0, 0)):
	printing(a)
else:
	print("no solution exists for this sample array.")