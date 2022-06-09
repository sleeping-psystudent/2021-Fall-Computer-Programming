import time
from functools import wraps

def show_process_time(method):
    """(5 pts) Method decorator

    Show the processing time of the decorated method
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        beg = time.time()
        d = method(*args, **kwargs)
        end = time.time()
        print(method.__repr__(),"executime time:", (end-beg))
        pass

    return wrapper


class Sudoku:
    """Sudoku solver

    A sudoku is represented by a 9x9 matrix. Each element
    in the matrix is an integer value from 1 to 9.

    For example:

            columns
                                      +-----+    +-----+   +-----+
       9,5,7,6,1,3,2,8,4              |9,5,7|    |6,1,3|   |2,8,4|
       4,8,3,2,5,7,1,9,6              |4,8,3|    |2,5,7|   |1,9,6|
    r  6,1,2,8,4,9,5,3,7              |6,1,2|    |8,4,9|   |5,3,7|
    o  1,7,8,3,6,4,9,5,2   ------->   +-----+    +-----+   +-----+
    w  5,2,4,9,7,1,3,6,8   ------->   block0     block1    block2
    s  3,6,9,5,2,8,7,4,1
       8,4,5,7,9,2,6,1,3              +-----+    +-----+   +-----+
       2,9,1,4,3,6,8,7,5              |1,7,8|    |3,6,4|   |9,5,2|
       7,3,6,1,8,5,4,2,9              |5,2,4|    |9,7,1|   |3,6,8|
                                      |3,6,9|    |5,2,8|   |7,4,1|
                                      +-----+    +-----+   +-----+
                                      block3     block4    block5

                                      +-----+    +-----+   +-----+
                                      |8,4,5|    |7,9,2|   |6,1,3|
                                      |2,9,1|    |4,3,6|   |8,7,5|
                                      |7,3,6|    |1,8,5|   |4,2,9|
                                      +-----+    +-----+   +-----+
                                      block6     block7    block8

    A finished sudoku must satisfy following requirements:
        1. Each row consists of a sequence of numbers from 1 to 9
            ,and each digit can only occur once
        2. Each col consists of a sequence of numbers from 1 to 9
            ,and each digit can only occur once
        3. Each block consists of a sequence of numbers from 1 to 9
            ,and each digit can only occur once

    Argument:
        fname (str): sudoku file name
    """
    def __init__(self, fname):
        """(5 pt) Construct the sudoku 2D matrix from file named as 'fname'"""
        f = open(fname, 'r')
        self.sudoku = f.read()
        f.close()
        
        board = self.sudoku.split('\n')

        self.arr2D = []
        for row in board:
            r = []
            for n in row:
                if n != ',':
                    r.append(int(n))
            self.arr2D.append(r)
        self.tem = []
        pass

    def __str__(self):
        """(5 pt) Return printable string representing current sudoku 2D matrix

        For example:

            9 5 7 6 1 3 2 8 4
            4 8 3 2 5 7 1 9 6
            6 1 2 8 4 9 5 3 7
            1 7 8 3 6 4 9 5 2
            5 2 4 9 7 1 3 6 8
            3 6 9 5 2 8 7 4 1
            8 4 5 7 9 2 6 1 3
            2 9 1 4 3 6 8 7 5
            7 3 6 1 8 5 4 2 9
        """
        string = ''
        for i in range(9):
            for j in range(9):
                string += str(self.arr2D[i][j])
                if j != 8:
                    string += ' '
            if i != 8:
                string += '\n'
        return string
        pass

    def check_block(self, block_idx):
        """(10 pt) Return True if the block with index 'block_idx' is valid

        Note:
            Refer the docstring of the Sudoku class. `block_idx` is an integer from 0 to 8.
            valid means no repeated numbers in the block except 0
        """
        remainder = int(block_idx/3)
        switch_re ={0:self.arr2D[0:3], 1:self.arr2D[3:6], 2:self.arr2D[6:9]}
        temp = switch_re.get(remainder)
        quotient = block_idx%3
        switch_qu =switch_qu ={0:[temp[i][0:3] for i in range(3)], 1:[temp[i][3:6] for i in range(3)], 2:[temp[i][6:9] for i in range(3)]}
        temp_2 = switch_qu.get(quotient)

        temp_3 = []
        for row in temp_2:
            for col in row:
                temp_3.append(col)
        if temp_3.count(0) != 0:
            block = len(set(temp_3))-1
            return (temp_3.count(0)+block)==9
        else:
            block = len(set(temp_3))
            return block==9
        pass

    def check_row(self, row_idx):
        """(5 pt) Return True if the row with index 'row_idx' is valid

        Note:
            Refer the docstring of the Sudoku class. `row_idx` is an integer from 0 to 8.
            valid means no repeated numbers in the row except 0
        """
        if self.arr2D[row_idx].count(0) != 0:
            row = len(set(self.arr2D[row_idx]))-1
            return (self.arr2D[row_idx].count(0)+row)==9
        else:
            row = len(set(self.arr2D[row_idx]))
            return row==9
        pass

    def check_col(self, col_idx):
        """(5 pt) Return True if the col with index 'col_idx' is valid

        Note:
            Refer the docstring of the Sudoku class. `col_idx` is an integer from 0 to 8.
            valid means no repeated numbers in the col except 0
        """
        temp = []
        for row in self.arr2D:
            temp.append(row[col_idx])
        if temp.count(0) != 0:
            col = len(set(temp))-1
            return (temp.count(0)+col)==9
        else:
            col = len(set(temp))
            return col==9
        pass

    def is_solved(self):
        """(5 pt) Return True if the sudoku is solved

        Note:
            A solve sudoku must satisfy following requirements:
                1. Each row consists of a sequence of numbers from 1 to 9
                    ,and each digit can only occur once
                2. Each col consists of a sequence of numbers from 1 to 9
                    ,and each digit can only occur once
                3. Each block consists of a sequence of numbers from 1 to 9
                    ,and each digit can only occur once
        """
        # row
        check = self.arr2D
        for row in check:
            if row.count(0) != 0:
                return False
            if len(set(row)) != 9:
                return False
        # column
        temp = []
        for i in range(9):
            temp_2 = []
            for row in self.arr2D:
                temp_2.append(row[i])
            temp.append(temp_2)
        for col in temp:
            if col.count(0) != 0:
                return False
            if len(set(col)) != 9:
                return False        
        # block
        for block in range(9):
            remainder = int(block/3)
            switch_re ={0:self.arr2D[0:3], 1:self.arr2D[3:6], 2:self.arr2D[6:9]}
            temp_3 = switch_re.get(remainder)
            quotient = block%3
            switch_qu =switch_qu ={0:[temp_3[i][0:3] for i in range(3)], 1:[temp_3[i][3:6] for i in range(3)], 2:[temp_3[i][6:9] for i in range(3)]}
            temp_4 = switch_qu.get(quotient)
            
            temp_5 = []
            for row in temp_4:
                for col in row:
                    temp_5.append(col)
            if temp_5.count(0) != 0:
                return False
            if len(set(temp_5)) != 9:
                return False  
            
        return True
        pass
        
    def solve_puzzle(self, only_one_solve = True):
        """(60 pt) Solve the sudoku puzzle automatically

        Note:
            You can define others functions inside this method to help you solve the puzzle
        """
        can = []
        solves = []
        pos = [-1, -1]
        for y in range(9):
            if pos[0] != -1 and pos[1] != -1:
                break
            for x in range(9):
                if self.arr2D[y][x] == 0:
                    pos = [x, y]
                    break
        if pos[0] == -1 and pos[1] == -1:
            return self.arr2D
        
        for f in range(1, 10):
            x = pos[0]
            y = pos[1]
            
            # row
            row = self.arr2D[y]
            if f in row:
                continue
            # col
            col = []
            for r in range(9):
                col.append(self.arr2D[r][x])
            if f in col:
                continue
            # block
            switch_re ={0:self.arr2D[0:3], 1:self.arr2D[0:3], 2:self.arr2D[0:3], 3:self.arr2D[3:6], 4:self.arr2D[3:6], 5:self.arr2D[3:6], 6:self.arr2D[6:9], 7:self.arr2D[6:9], 8:self.arr2D[6:9]}
            temp = switch_re.get(y)
            switch_qu =switch_qu ={0:[temp[i][0:3] for i in range(3)], 1:[temp[i][0:3] for i in range(3)], 2:[temp[i][0:3] for i in range(3)], 3:[temp[i][3:6] for i in range(3)], 4:[temp[i][3:6] for i in range(3)], 5:[temp[i][3:6] for i in range(3)], 6:[temp[i][6:9] for i in range(3)], 7:[temp[i][6:9] for i in range(3)], 8:[temp[i][6:9] for i in range(3)]}
            temp_2 = switch_qu.get(x)               
            temp_3 = []
            for row in temp_2:
                for col in row:
                    temp_3.append(col)
            if f in temp_3:
                continue 
            can.append(f)
            
        if len(can) == 0: 
            return None
        for i in range(len(can)):
            y = pos[1]
            x = pos[0]
            self.arr2D[y][x] = can[i]
            re = self.solve_puzzle(self.arr2D)
            if re is None:
                self.arr2D[y][x] = 0
                pass
            elif isinstance(re, list) and len(re) == 0:
                self.arr2D[y][x] = 0
                pass
            else:
                if only_one_solve:
                    return re
                for j in range(len(re)):
                    solves.append(re[j])
        return solves
    
    # Uncomment the line below when you finish the decorator show_process_time
    @show_process_time
    def solve(self):
        return self.solve_puzzle(self)
