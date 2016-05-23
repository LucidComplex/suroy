#!/usr/bin/env python3
import room
import grammar


class Suroy(object):
    def __init__(self):
        self.player = {
            'inventory': []
        }
        self.current_room = room.load_rooms()
        self.grammar = grammar.load_grammar()
        self.play = True
        self.commands = {
            'look': self.look,
            'north': self.north,
            'south': self.south,
            'east': self.east,
            'west': self.west,
            'down': self.down,
            'up': self.up,
            'get': self.get,
            'inventory': self.inventory
        }

    def inventory(self, *args):
        print(' You are carrying:')
        if len(self.player['inventory']) == 0:
            print('  Nothing')
            return
        for item in self.player['inventory']:
            print(' ', item)

    def get(self, item_name):
        if len(str.strip(item_name)) == 0:
            print('You want to get what item?')
            return
        try:
            grabbed_index = self.current_room.items.index(item_name)
            grabbed_item = self.current_room.items.pop(grabbed_index)
            self.player['inventory'].append(grabbed_item)
            print(' Taken.')
        except ValueError:
            print(' I don\'t see', item_name, 'around here.')

    def look(self, *args):
        self.print_room()

    def down(self, *args):
        try:
            self.current_room = self.current_room.exits['d']
            self.print_room(intro=True)
        except KeyError:
            print(' I can\'t get there.')

    def up(self, *args):
        try:
            self.current_room = self.current_room.exits['u']
            self.print_room(intro=True)
        except Exception:
            print(' I can\'t get there.')

    def north(self, *args):
        try:
            self.current_room = self.current_room.exits['n']
            self.print_room(intro=True)
        except Exception:
            print(' I can\'t get there.')

    def south(self, *args):
        try:
            self.current_room = self.current_room.exits['s']
            self.print_room(intro=True)
        except Exception:
            print(' I can\'t get there.')

    def east(self, *args):
        try:
            self.current_room = self.current_room.exits['e']
            self.print_room(intro=True)
        except Exception:
            print(' I can\'t get there.')

    def west(self, *args):
        try:
            self.current_room = self.current_room.exits['w']
            self.print_room(intro=True)
        except Exception:
            print(' I can\'t get there.')

    def start(self):
        self.print_room(intro=True)
        while self.play:
            self.prompt()
            self.handle_command()

    def prompt(self):
        print('>>>', end=' ')
        self.command = input()

    def handle_command(self):
        command, args = self.grammar.recognize('verbs', self.command)
        try:
            method = self.commands[command]
        except Exception:
            print('I don\'t understand that.')
            return
        method(args)

    def print_room(self, intro=False):
        room = self.current_room
        print(room.title, '\n')
        if intro:
            print(room.intro, '\n')
        print(room.description, '\n')
        if room.items:
            print(' Items:')
            for item in room.items:
                print('  ', item)
            print()
        self.print_exits()

    def print_exits(self):
        print(' Exits:')
        for d, exit in self.current_room.exits.items():
            if d == 'n':
                direction = 'North'
            elif d == 's':
                direction = 'South'
            elif d == 'e':
                direction = 'East'
            elif d == 'w':
                direction = 'West'
            elif d == 'd':
                direction = 'Down'
            elif d == 'u':
                direction = 'Up'
            print('  ', direction, '-', exit.title)
        print()


def main():
    print('Loading game data...')
    print('Loaded!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    suroy = Suroy()
    suroy.start()

if __name__ == '__main__':
    main()
