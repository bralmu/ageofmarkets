import enum


class Cell_Type(enum.Enum):

    Ground = 0
    Sea = 1


class Cell:
  
    def __init__(self, cell_type, horizontal_position, vertical_position): 
        self.cell_type = cell_type
        self.horizontal_position = horizontal_position
        self.vertical_position = vertical_position
  
    def __str__(self):
        return str(self.cell_type) + ", " + str(self.horizontal_position) + ", " + str(self.vertical_position)

    def get_serializable(self):
        return [self.cell_type, self.horizontal_position, self.vertical_position]
