# Write a class to hold player information, e.g. what room they are in
# currently.
#
# name
# current_room


class Player():
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom

    def __str__(self):
        return f"The player's current location: {self.currentRoom}"
