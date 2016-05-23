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
            'inventory': self.inventory,
            'use': self.use,
            'examine': self.examine,
            'drop': self.drop
        }
        self.used = []

    def drop(self, *args):
        word = ' '.join(args)
        if len(word) == 0:
            print(' Drop what?')
            return
        try:
            for i, item in enumerate(self.player['inventory']):
                if str.lower(item.title) == word:
                    self.current_room.items.append(item)
                    del self.player['inventory'][i]
                    print(' Dropped.')
                    return
        except Exception:
            print('You don\'t have that item.')


    def use(self, *args):
        word = ' '.join(args)
        if len(word) == 0:
            print(' Use what?')
            return
        if self.current_room.title == 'Exam Room' and word == 'test paper':
            self.play = False
            check = 0
            required = ('pen', 'calculator')
            for item in self.player['inventory']:
                if str.lower(item.title) in required:
                    check = check + 1
            if check == 2:
                for item in self.used:
                    if str.lower(item.title) == 'packed lunch':
                        print('YOU PASSED THE EXAM!')
                        return
                print(' You take the exam, but your calculator started to look like a chocolate bar. You could\'t concentrate.\nYOU FAILED.')
            else:
                print('Your approached to take the exam, but your teacher merely stared at you... as if you were lacking something for the exam.\nYOU FAILED.')
        for item in self.player['inventory']:
            if str.lower(item.title) == str.lower(word):
                try:
                    if self.current_room.conflict:
                        if str.lower(word) in self.current_room.solution.keys():
                            solution_text, solve = self.current_room.solution[str.lower(word)]
                            print('', solution_text)
                            if solve:
                                self.current_room.conflict = False
                                self.current_room.description = self.current_room.solved
                                for i, item in enumerate(self.player['inventory']):
                                    if str.lower(item.title) == str.lower(word):
                                        del self.player['inventory'][i]
                            return
                    print('', item.use_cases[''])
                    self.used.append(item)
                    for i, item in enumerate(self.player['inventory']):
                        if str.lower(item.title) == str.lower(word):
                            if item.drop_on_use:
                                del self.player['inventory'][i]
                            return
                except KeyError:
                    print('I can\'t use that.')
        print(' I don\'t have a', word, 'to use.')

    def examine(self, *args):
        if len(args) == 0:
            print(' Examine what?')
            return
        word = ' '.join(args)
        for item in self.player['inventory'] + self.current_room.items:
            if str.lower(item.title) == str.lower(word):
                print('', item.description)
                return

    def inventory(self, *args):
        print(' You are carrying:')
        if len(self.player['inventory']) == 0:
            print('  Nothing')
            return
        for item in self.player['inventory']:
            print(' ', item.title)

    def get(self, item_name):
        if len(self.player['inventory']) == 5:
            print(' You can\'t carry anymore.')
            return
        if len(str.strip(item_name)) == 0:
            print('You want to get what item?')
            return
        try:
            grabbed = [item for item in self.current_room.items
                if str.lower(item.title) == str.lower(item_name)][0]
            self.current_room.items = [item for item in
                self.current_room.items
                if str.lower(item.title) != str.lower(item_name)]
            self.player['inventory'].append(grabbed)
            print(' Taken.')
        except ValueError:
            print(' I don\'t see', item_name, 'around here.')

    def look(self, *args):
        self.print_room()

    def move(self, direction):
        try:
            if self.current_room.conflict:
                print(' YOU LOSE.')
                self.play = False
                return
            self.current_room = self.current_room.exits[direction]
            self.print_room(intro=True)
        except KeyError:
            print(' I can\'t get there.')

    def down(self, *args):
        self.move('d')

    def up(self, *args):
        self.move('u')

    def north(self, *args):
        self.move('n')

    def south(self, *args):
        self.move('s')

    def east(self, *args):
        self.move('e')

    def west(self, *args):
        self.move('w')

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
                print('  ', item.title)
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
