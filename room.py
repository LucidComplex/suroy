import os

class Room(object):
    def __init__(self, path):
        self.items = []
        self.exits = {}
        with open(path) as room_data:
            for line in room_data:
                l = str.lower(line.rstrip())
                if l == 'title':
                    self.title = next(room_data).rstrip()
                elif l == 'intro':
                    self.intro = next(room_data).rstrip()
                elif l == 'desc':
                    self.description = next(room_data).rstrip()
                elif l == 'items':
                    item = str.lower(next(room_data).rstrip())
                    while item != 'end':
                        self.items.append(item)
                        item = str.lower(next(room_data).rstrip())
                elif l == 'exit':
                    exit = str.lower(next(room_data).rstrip())
                    while exit != 'end':
                        self.exits[exit[0]] = exit[2:]
                        exit = str.lower(next(room_data).rstrip())


def load_rooms():
    root_dir = 'rooms2'
    root = Room(os.path.join(root_dir, 'room.rdf'))
    loaded = {'room': root}
    frontier = [root]
    while len(frontier) > 0:
        temp = frontier.pop()
        for direction, exit in temp.exits.items():
            if exit in loaded.keys():
                temp.exits[direction] = loaded[exit]
            else:
                temp_room = Room(os.path.join(root_dir, exit + '.rdf'))
                temp.exits[direction] = temp_room
                loaded[exit] = temp_room
                frontier.append(temp_room)
    return root
