class Board:
    def __init__(self, table, blank_row, blank_col):
        self.table = table
        self.blank_row = blank_row
        self.blank_col = blank_col
        self.n = 0

    def getTable(self):
        return self.table
    
    def getBlankRow(self):
        return self.blank_row
    
    def getBlankCol(self):
        return self.blank_col
    
    def __lt__(self, other):
        return self.n <= other.n