# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return(f'{self.name}')

    def move_direction(self):
        exits = []
        if self.n_to:
            exits.append('n')
        if self.s_to:
            exits.append('s')
        if self.e_to:
            exits.append('e')
        if self.w_to:
            exits.append('w')
        return exits