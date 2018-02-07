from requests import post
from bs4 import BeautifulSoup
from SudokuSolver.Cell import Cell

class Sudoku:
    def __init__(self):
        # self.cells = list()
        self.cells = [0, 0, 0, 0, 0, 0, 7, 0, 1, 0, 6, 0, 5, 0, 0, 9, 4, 3, 4, 2, 0, 0, 1, 0, 0, 8, 0, 5, 0, 4, 7, 8, 0, 0, 6, 0, 0, 8, 6, 0, 4, 0, 0, 0, 7, 0, 7, 2, 6, 9, 0, 0, 0, 8, 2, 0, 3, 8, 7, 6, 5, 0, 0, 6, 9, 0, 0, 0, 1, 8, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0]
    
    def load(self, source="internet"):
        page = post("http://www.sudokuweb.org/", data={"sign2":"9x9"}).text
        soup = BeautifulSoup(page, 'html.parser')

        for index, td in enumerate(soup.find_all('td')):
            if td.span['class'][0] == 'sedy':
                self.cells.append(int(td.span.text))
            else:
                self.cells.append(0)
    
    def fill(self, region_type, indexGrid, indexCell, digit):
        assert (region_type in ('row', 'col', 'box')), "Invalid region_type"
        assert (0 <= indexGrid <= 8), "Invalid indexGrid"
        assert (indexCell is None or 0 <= indexCell <= 8), "Invalid indexCell"
        
        rowIndex = self.convert(region_type, 'row', indexGrid, indexCell)
        colIndex = self.convert(region_type, 'col', indexGrid, indexCell)
        boxIndex = self.convert(region_type, 'box', indexGrid, indexCell)
        
        self.cells[rowIndex[0] * 9 + rowIndex[1]] = digit
        self.print(rowIndex[0], rowIndex[1])
        
    def get(self, region_type, indexGrid, indexCell=None):
        assert (region_type in ('row', 'col', 'box')), "Invalid region_type"
        assert (0 <= indexGrid <= 8), "Invalid indexGrid"
        assert (indexCell is None or 0 <= indexCell <= 8), "Invalid indexCell"
        
        if region_type == 'row':
            if indexCell is None:
                return self.cells[indexGrid * 9 : indexGrid * 9 + 9]
            return self.cells[indexGrid * 9 + indexCell]
        
        elif region_type == 'col':
            result_list= list()
            for index, cell in enumerate(self.cells):
                if index % 9 == indexGrid:
                    result._listappend(cell)
            if indexCell is None:
                return result_list
            return result_list[indexCell]
        
        elif region_type == 'box':
            result_list = list()
            row_range = (indexGrid//3*3, indexGrid//3*3+1, indexGrid//3*3+2)
            col_range = (indexGrid%3*3, indexGrid%3*3+1, indexGrid%3*3+2)
            for index, cell in enumerate(self.cells):
                if index % 9 in col_range and index // 9 in row_range:
                    result_list.append(cell)
            if indexCell is None:
                return result_list
            return result_list[indexCell]
    
    def convert(self, fromHouse, toHouse, indexGrid, indexCell):
        if toHouse == 'row':
            if fromHouse == 'row':
                return indexGrid, indexCell
            elif fromHouse == 'col':
                return indexCell, indexGrid
            elif fromHouse == 'box':
                newIndexGrid = indexGrid // 3 * 3 + indexCell // 3
                newIndexCell = indexGrid % 3 * 3 + indexCell % 3
                return newIndexGrid, newIndexCell
        
        elif toHouse == 'col':
            if fromHouse == 'row':
                return indexCell, indexGrid
            elif fromHouse == 'col':
                return indexGrid, indexCell
            elif fromHouse == 'box':
                newIndexGrid = indexGrid % 3 * 3 + indexCell % 3
                newIndexCell = indexGrid // 3 * 3 + indexCell // 3
                return newIndexGrid, newIndexCell
        
        elif toHouse == 'box':
            if fromHouse == 'row':
                newIndexGrid = indexGrid // 3 * 3 + indexCell // 3
                newIndexCell = indexGrid % 3 * 3 + indexCell % 3
                return newIndexGrid, newIndexCell
            elif fromHouse == 'col':
                newIndexGrid = indexCell // 3 * 3 + indexGrid // 3
                newIndexCell = indexCell % 3 * 3 + indexGrid % 3
                return newIndexGrid, newIndexCell
            elif fromHouse == 'box':
                return indexGrid, indexCell
        
    
    def print(self, row=None, col=None):
        print(' ' * ((col//3)*8+2 + (col%3)*2+1 + 1) + "*" if col is not None else '')
        print("  -------------------------\n" ,end='')
        print("* " if row == 0 else "  ", end='')
        
        for index, cell in enumerate(self.cells):
            if index % 9 == 0:
                print("|" ,end=' ')
            
            print(cell or "_", end=' ')
            
            if index % 3 == 2:
                print("|", end=' ')
            
            if index % 9 == 8:
                print()
            
            if index % 27 == 26:
                print("  -------------------------")
            
            if row and index % 9 == 8 and index // 9 == row-1 :
                print("* ", end='')
            elif index % 9 == 8:
                print("  ", end='')
        print()
