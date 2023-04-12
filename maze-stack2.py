class Empty(Exception):
    pass

class stack :
    def __init__ (self):
        self._data = []

    def is_empty(self):
        return len(self._data)==0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def top(self):
        if self.is_empty():
            #return None
            raise Empty('Stack is empty!')
        return self._data[-1]



SIZE = 5
#maze problem
maze = [
    [0,1,0,0,0],
    [0,0,0,1,0],
    [1,0,1,1,0],
    [0,0,1,0,0],
    [1,0,1,0,0]
]
#list to store the solution matrix
solution = [[0]*SIZE for _ in range(SIZE)]

#function to solve the maze
#using backtracking
def solvemaze(r, c):
    #if destination is reached, maze is solved
    #destination is the last cell(maze[SIZE-1][SIZE-1])
    if (r==SIZE-1) and (c==SIZE-1):
        solution[r][c] = 1;
        return True;
    #checking if we can visit in this cell or not
    #the indices of the cell must be in (0,SIZE-1)
    #and solution[r][c] == 0 is making sure that the cell is not already visited
    #maze[r][c] == 0 is making sure that the cell is not blocked
    if r>=0 and c>=0 and r<SIZE and c<SIZE and solution[r][c] == 0 and maze[r][c] == 0:
        #if safe to visit then visit the cell
        solution[r][c] = 1
        #going down
        if solvemaze(r+1, c):
            return True
        #going right
        elif solvemaze(r, c+1):
            return True
        #going up
        elif solvemaze(r-1, c):
            return True
        #going left
        elif solvemaze(r, c-1):
            return True
        #backtracking
        solution[r][c] = 0;
        return False;
    return 0;


def solvemaze_stack(r, c) :
    mystack = stack()
    currpos = [0, 0]
    mystack.push(currpos)

    while currpos != [SIZE-1, SIZE-1] and not mystack.is_empty() :
        r = currpos[0]
        c = currpos[1]
        solution[r][c] = 1

        if (c+1)<SIZE and maze[r][c+1]==0 : # Move one step right
            currpos = [r, c+1]
            maze[r][c+1] = 1
            mystack.push(currpos)
        elif (r+1)<SIZE and maze[r+1][c]==0 : # Move one step down
            currpos = [r+1, c]
            maze[r+1][c] = 1
            mystack.push(currpos)
        elif (c-1)>=0 and maze[r][c-1]==0 : # Move one step left
            currpos = [r, c-1]
            maze[r][c-1] = 1
            mystack.push(currpos)
        elif (r-1)>=0 and maze[r-1][c]==0 : # Move one step up
            currpos = [r-1, c]
            maze[r-1][c] = 1
            mystack.push(currpos)            
        else :
            solution[r][c] = 0
            currpos = mystack.pop()
            r = currpos[0]
            c = currpos[1]
            maze[r][c] = 0
            
    r = currpos[0]
    c = currpos[1]
    solution[r][c] = 1
    
    return True
    

if(solvemaze(0,0)):
    for i in solution:
        print (i)
print()
if (solvemaze_stack(0,0)) :
    for i in solution:
        print (i)
else:
    print ("No solution")
