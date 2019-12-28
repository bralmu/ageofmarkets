

class Player:
  
    def __init__(self, current_horizontal_position, current_vertical_position): 
        self.current_horizontal_position = current_horizontal_position
        self.current_vertical_position = current_vertical_position
        self.target_horizontal_position = current_horizontal_position
        self.target_vertical_position = current_vertical_position
  
    def __str__(self):
        return  str(self.current_horizontal_position) + ", " + \
                str(self.current_vertical_position) + ", " + \
                str(self.target_horizontal_position) + ", " + \
                str(self.target_vertical_position) + ", "

    def get_serializable(self):
        return [self.current_horizontal_position, self.current_vertical_position, self.target_horizontal_position, 
                self.target_vertical_position]
