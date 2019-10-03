# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return(f'{self.name} is in {self.current_room}')

    def move(self, direction):
        if direction in self.current_room.move_direction():
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('Try again')

    def switch_room(self, new_room):
        self.current_room = new_room


eric = Player("eric", "outside")

print(eric)
print(2**3)
