
class Room:
    def __init__(self, color):
        self.color = color
        self.doors = {}
        self.exit = None

    def add_door(self, dest, dir):
        self.doors[dir] = dest

    def __str__(self):
        txt = f"Room: {self.color}\n"
        for direction in self.doors:
            txt += f"There is a door {direction} leading to {self.doors[direction]}\n"
        if self.exit is not None:
            txt += "There is an exit door"
        return txt

class Game:
    def __init__(self):
        self.rooms = {}
        self.load_rooms()
        self.load_doors()

    def load_rooms(self):
        file = open('rooms.txt')
        lines = file.readlines()
        for line in lines:
            color = line.strip()
            self.rooms[color] = Room(color)

    def load_doors(self):
        file = open('doors.txt')
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(',')
            room = self.rooms[data[0]]
            destination = data[1]
            direction = data[2]
            if direction == "exit":
                room.exit = 'locked'
            else:
                room.add_door(destination, direction)

    def print_rooms(self):
        for color in self.rooms:
            print(self.rooms[color])


game = Game()
game.print_rooms()