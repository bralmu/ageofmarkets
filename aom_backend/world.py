import random
import cell


class World:

    def __init__(self):
        self.cells = []
        for horizontal_position in range (0,10):
            for vertical_position in range (0, 10):
                cell_type = random.randint(0,2)
                if cell_type == 2:
                    cell_type = 0
                new_cell = cell.Cell(cell_type, horizontal_position, vertical_position)
                self.cells.append(new_cell)
  
    def __str__(self):
        string = ""
        for single_cell in cells:
            string.append(single_cell)
        return cells[0]

    def get_serializable(self):
        serializable_data = []
        for single_cell in self.cells:
            serializable_data.append(single_cell.get_serializable())
        return serializable_data
