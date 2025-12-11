from drone import Drone

if __name__ == '__main__':
    d = Drone(5)

    command = ''

    while command != 'Exit':
        command = input("Give command: ")
        command = command.strip()
        match command:
            case 'Land':
                d.land()
            case 'Takeoff':
                d.takeoff()
            case 'Shoot':
                d.shoot()
            case 'Move':
                direction = input("Give direction: ")
                d.change_direction(direction)
            case 'Exit':
                d.land()
                print("Bye!")
            case _:
                print("Unknown command")