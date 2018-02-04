import requests
from bs4 import BeautifulSoup

class Sudoku(object):
	def __init__(self):
		self.cells = list()
	
	def load(self, source="internet"):
		page = requests.get("http://www.sudokuweb.org/").text
		soup = BeautifulSoup(page, 'html.parser')

		for index, td in enumerate(soup.find_all('td')):
			if td.span['class'][0] == 'sedy':
				self.cells.append(int(td.span.text))
			else:
				self.cells.append(0)
	
	def fill(self, row, col, digit):
		pass
	
	def print(self, row=None, col=None):
		print(' ' * (((col-1)//3)*8+2 + ((col-1)%3)*2+1 + 1) + "*" if col is not None else '')
		print("  -------------------------\n" ,end='')
		print("* " if row == 1 else "  ", end='')
		
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
			
			if row and index % 9 == 8 and index // 9 == row-2 :
				print("* ", end='')
			elif index % 9 == 8:
				print("  ", end='')
		print()