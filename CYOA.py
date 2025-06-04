

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.class_definition
class GameObject:
    def __init__(self, name, description, interact_text):
        self.name = name
        self.description = description
        self.interact_text = interact_text
        self.used = False

    def interact(self):
        if not self.used:
            self.used = True
            return self.interact_text
        else:
            return f"You've already used the {self.name}."


@app.class_definition
class Room:
    def __init__(self, name, description, object_in_room):
        self.name = name
        self.description = description
        self.object = object_in_room
        self.connected_rooms = {}

    def describe(self):
        desc = f"\n-- {self.name} --\n{self.description}\n"
        desc += f"You see a {self.object.name} here. {self.object.description}"
        return desc

    def connect_room(self, direction, room):
        self.connected_rooms[direction] = room

    def get_connection(self, direction):
        return self.connected_rooms.get(direction, None)


@app.class_definition
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room

    def move(self, direction):
        next_room = self.current_room.get_connection(direction)
        if next_room:
            self.current_room = next_room
            return f"You move {direction} to the {next_room.name}."
        else:
            return "You can't go that way."


@app.cell
def _():
    def main():
        # Create objects
        sword = GameObject("Sword", "It glows faintly with a magical aura.", "You pick up the Sword. It feels powerful.")
        book = GameObject("Ancient Book", "Covered in dust and written in an unknown language.", "You flip through the pages and learn a spell.")
        key = GameObject("Silver Key", "Lying on a pedestal, looks important.", "You take the Silver Key. It might unlock something.")
        chest = GameObject("Treasure Chest", "Ornate and locked tight.", "You unlock the chest with the Silver Key and find gold!")

        # Create rooms
        entrance = Room("Dungeon Entrance", "A dark, damp place. The air is thick with moisture.", sword)
        library = Room("Ancient Library", "Shelves filled with decaying books line the walls.", book)
        armory = Room("Old Armory", "Rusty weapons and armor litter the ground.", key)
        treasure_room = Room("Treasure Room", "This room shines with golden light.", chest)

        # Connect rooms
        entrance.connect_room("north", library)
        library.connect_room("south", entrance)
        library.connect_room("east", armory)
        armory.connect_room("west", library)
        armory.connect_room("north", treasure_room)
        treasure_room.connect_room("south", armory)

        # Start game
        player = Player(entrance)
        print("Welcome to the Dungeon Adventure!")
    
        while True:
            print(player.current_room.describe())
            command = input("\nWhat do you want to do? (move [north/south/east/west], interact, quit): ").strip().lower()

            if command.startswith("move"):
                direction = command.split(" ")[1]
                print(player.move(direction))
            elif command == "interact":
                print(player.current_room.object.interact())
            elif command == "quit":
                print("Thanks for playing!")
                break
            else:
                print("Unknown command. Try again.")

    if __name__ == "__main__":
        main()
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
