import requests
from bs4 import BeautifulSoup

class Sudoku:
    def __init__(self):
        # self.cells = list()
        self.cells = [0, 0, 0, 0, 0, 0, 7, 0, 1, 0, 6, 0, 5, 0, 0, 9, 4, 3, 4, 2, 0, 0, 1, 0, 0, 8, 0, 5, 0, 4, 7, 8, 0, 0, 6, 0, 0, 8, 6, 0, 4, 0, 0, 0, 7, 0, 7, 2, 6, 9, 0, 0, 0, 8, 2, 0, 3, 8, 7, 6, 5, 0, 0, 6, 9, 0, 0, 0, 1, 8, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0]
    
    def load(self, source="internet"):
        page = requests.post("http://www.sudokuweb.org/", data={"sign2":"9x9"}).text
        soup = BeautifulSoup(page, 'html.parser')

        for index, td in enumerate(soup.find_all('td')):
            if td.span['class'][0] == 'sedy':
                self.cells.append(int(td.span.text))
            else:
                self.cells.append(0)
    
    def fill(self, region_type, indexBig, indexSmall, digit):
        assert (region_type in ('row', 'col', 'box')), "Invalid region_type"
        assert (0 <= indexBig <= 8), "Invalid indexBig"
        assert (indexSmall is None or 0 <= indexSmall <= 8), "Invalid indexSmall"
        
        row, col = self.getRowIndex(region_type, indexBig, indexSmall)
        
        # if digit in self.get('row', row):
        
        self.cells[row * 9 + col] = digit
        self.print(row, col)
        
    def get(self, region_type, indexBig, indexSmall=None):
        assert (region_type in ('row', 'col', 'box')), "Invalid region_type"
        assert (0 <= indexBig <= 8), "Invalid indexBig"
        assert (indexSmall is None or 0 <= indexSmall <= 8), "Invalid indexSmall"
        
        if region_type == 'row':
            if indexSmall is None:
                return self.cells[indexBig * 9 : indexBig * 9 + 9]
            return self.cells[indexBig * 9 + indexSmall]
        
        elif region_type == 'col':
            result_list= list()
            for index, cell in enumerate(self.cells):
                if index % 9 == indexBig:
                    result._listappend(cell)
            if indexSmall is None:
                return result_list
            return result_list[indexSmall]
        
        elif region_type == 'box':
            result_list = list()
            row_range = (indexBig//3*3, indexBig//3*3+1, indexBig//3*3+2)
            col_range = (indexBig%3*3, indexBig%3*3+1, indexBig%3*3+2)
            for index, cell in enumerate(self.cells):
                if index % 9 in col_range and index // 9 in row_range:
                    result_list.append(cell)
            if indexSmall is None:
                return result_list
            return result_list[indexSmall]
    
    def getRowIndex(self, region_type, indexBig, indexSmall):
        if region_type == 'row':
            return indexBig, indexSmall
        elif region_type == 'col':
            return indexSmall, indexBig
        elif region_type == 'box':
            row = indexBig // 3 * 3 + indexSmall // 3
            col = indexBig % 3 * 3 + indexSmall % 3
            return row, col
    
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
