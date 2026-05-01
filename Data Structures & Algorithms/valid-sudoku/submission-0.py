class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        stolb = defaultdict(set) # столбец : цифры
        cube = defaultdict(set)
        
        for indx_row, row in enumerate(board):
            numbers_row=set()
            # проверка по строкам
            if indx_row in [0, 1, 2]:
                ro = 1
            if indx_row in [3, 4, 5]:
                ro = 2
            if indx_row in [6, 7, 8]:
                ro = 3
            

            for indx, cell in enumerate(row):
                if cell in numbers_row or cell in stolb[indx]:
                    print("Выход 1")
                    return False

                if indx in [0, 1, 2]:
                    lo = 1
                if indx in [3, 4, 5]:
                    lo = 2
                if indx in [6, 7, 8]:
                    lo = 3
                
                if cell in cube[(ro,lo)]:
                    return False

                if cell != '.':
                    
                    numbers_row.add(cell)
                    stolb[indx].add(cell)
                    cube[(ro,lo)].add(cell)
                
        return True

