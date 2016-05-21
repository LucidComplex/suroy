#!/bin/env python
import room
import os


class Suroy(object):
    def __init__(self, *args):
        try:
            directory = args[0]
        except Exception:
            directory = 'rooms'
        self.load_rooms(directory)
        self.current_room = self.rooms['begin']

    def load_rooms(self, directory):
        rooms = os.scandir(directory)
        room_dict = {}
        for room_data in rooms:
            if room_data.is_file() and room_data.name.endswith('.rdf'):
                room_dict[room_data.name[:-4]] = room.Room(room_data)
        self.rooms = room_dict

    def start(self):
        self.print_room(True)
        while True:
            self.prompt()

    def prompt(self):
        print('>>>', end=' ')
        command = input()
        self.parse_command(command)

    def move_room(self, direction):
        self.current_room = self.rooms[self.current_room.exits[direction]]
        self.print_room(True)

    def parse_command(self, command):
        direction = command
        self.move_room(direction)

    def print_room(self, first=False):
        print(self.current_room.title)
        if first:
            print(self.current_room.intro)
        print(self.current_room.desc)
        if self.current_room.items:
            print('Items:')
            for name, count in self.current_room.items.items():
                print(count, ' - ', name)
            print()
        print('Exits:')
        for direction, name in self.current_room.exits.items():
            print(str.upper(direction), ' - ', name)

def main():
    print('Loading game data.')
    suroy = Suroy()
    suroy.start()




if __name__ == '__main__':
    main()
