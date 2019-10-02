from room import Room
from player import Player
from item import Item

# Declare items

stone = Item("Stone", "Tiny or huge rock")
sword = Item("Sword", "Preferred weapon of Donatello")
dollar = Item("Dollar", "Money for exchanging goods")
axe = Item("Axe", "Famous sidekick of Paul Bunyan")
jacket = Item("Jacket", "Keeps the cold out")
pill = Item("Pill", "Cures what ailes you")
shovel = Item("Shovel", "Digs a ditch or clears the road")
macbook = Item("Macbook", "Helpful for writing Python programs")
stereo = Item("Stereo", "Music playing machine")

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [stone, axe, jacket]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [pill, macbook, stereo]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [dollar, sword, shovel]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [sword, dollar, axe]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [dollar, macbook, jacket]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(input('What\'s your name? '), room['outside'], None)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
