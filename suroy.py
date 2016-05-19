#!/bin/env python
import room
import os


def load_rooms(directory):
    rooms = os.scandir(directory)
    room_dict = {}
    for room_data in rooms:
        if room_data.is_file() and room_data.name.endswith('.rdf'):
            room_dict[room_data.name[:-4]] = room.Room(room_data)

    return room_dict

def main():
    print('Loading game data.')
    rooms = load_rooms('rooms')
    room = rooms['begin']
    start_game(rooms)

def start_game(rooms):
    current_room = rooms['begin']
    while True:
        print_room(current_room, True)
        prompt()

def prompt():
    print('>>>', end=' ')
    command = input()

def print_room(room, first=False):
    print(room.title)
    if first:
        print(room.intro)
    print(room.desc)
    if room.items:
        print('Items:')
        for name, count in room.items.items():
            print(count, ' - ', name)
        print()
    print('Exits:')
    for direction, name in room.exits.items():
        print(str.upper(direction), ' - ', name)

if __name__ == '__main__':
    main()
