class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        stolb = defaultdict(set) # столбец : цифры
        cube = defaultdict(set)
        
        for indx_row, row in enumerate(board):
            numbers_row=set()
            # проверка по строкам
            ro = indx_row // 3
            

            for indx, cell in enumerate(row):
                if cell in numbers_row or cell in stolb[indx]:
                    return False

                lo = indx // 3
                
                if cell in cube[(ro,lo)]:
                    return False

                if cell != '.':
                    numbers_row.add(cell)
                    stolb[indx].add(cell)
                    cube[(ro,lo)].add(cell)
                
        return True

