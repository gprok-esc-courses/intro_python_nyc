
class Drone:
    def __init__(self, ammo):
        self.landed = True 
        self.direction = None
        self.ammo = ammo
    
    def takeoff(self):
        self.landed = False
        print("Drone took off")

    def land(self):
        self.landed = True 
        print("Drone landed")

    def change_direction(self, direction):
        if self.landed:
            print("Drone is landed, cannot change direction")
        elif direction not in ['North', 'South', 'East', 'West']:
            print("Invalid direction")
        else:
            self.direction = direction 
            print(f"Drone heads {direction}")

    def shoot(self):
        if self.ammo == 0:
            print("Out of ammo, cannot shoot")
        else:
            print("Shooting ...")
            self.ammo = self.ammo - 1


if __name__ == '__main__':
    print("Hello Drone")