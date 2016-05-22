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

    def start(self):
        while self.play:
            self.print_room()
            self.prompt()
            self.handle_command()

    def prompt(self):
        print('>>>', end=' ')
        self.command = input()

    def handle_command(self):
        print(self.grammar.recognize_verb(self.command))

    def print_room(self):
        room = self.current_room
        print(room.title, '\n')
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
            print('  ', direction, '-', exit.title, '\n')


def main():
    print('Loading game data...')
    print('Loaded!\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    suroy = Suroy()
    suroy.start()

if __name__ == '__main__':
    main()
