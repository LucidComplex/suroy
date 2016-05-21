#!/bin/env python
import room
import grammar
import os
import sys


class Suroy(object):
    def __init__(self, *args):
        try:
            directory = args[0]
        except Exception:
            directory = 'rooms'
        self.load_rooms(directory)
        self.current_room = self.rooms['begin']
        self.grammar = grammar.Grammar()
        self.inventory = {}

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
        try:
            self.current_room = self.rooms[self.current_room.exits[direction]]
        except Exception:
            print('I can\'t get there.')
            return
        self.print_room(True)

    def look(self, *args):
        self.print_room()

    def south(self, *args):
        self.move_room('s')

    def north(self, *args):
        self.move_room('n')

    def east(self, *args):
        self.move_room('e')

    def west(self, *args):
        self.move_room('w')

    def get(self, *args):
        try:
            quantity = self.current_room.items.pop(args[0])
        except KeyError:
            print('I can\'t find that item.')
            return
        try:
            self.inventory[args[0]] += quantity
        except KeyError:
            self.inventory[args[0]] = quantity
        print('Taken.')

    def parse_command(self, command):
        if self.grammar.check_grammar(command):
            com_split = command.split(' ')
            getattr(self, self.grammar.simplify(com_split[0]))(com_split[-1])
        else:
            print('Huh? I don\'t understand what you mean.')

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
            print(str.upper(direction), ' - ', self.rooms[name].title.rstrip())

def main(directory):
    print('Loading game data.')
    suroy = Suroy(directory)
    suroy.start()


if __name__ == '__main__':
    try:
        directory = sys.argv[1]
    except Exception:
        main('')
    main(directory)
