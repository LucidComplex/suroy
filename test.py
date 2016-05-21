import os
import room
import suroy
import unittest

class RoomTestCase(unittest.TestCase):
    def setUp(self):
        sample_path = os.scandir('test_rooms')
        for sample in sample_path:
            if sample.is_file():
                if sample.name == 'begin.rdf':
                    self.r = room.Room(sample)
                    self.sample = sample
                    break

    def test_room_takes_path(self):
        with open('test_rooms/begin.rdf') as test:
            r = room.Room(test)
        self.assertEqual(r.file_path, 'test_rooms/begin.rdf')

    def test_room_loads_intro(self):
        intro = ('You wake up on an old wooden floor. '
                'You look outside and see a dark forest.\n'
                'You notice a silver spoon on the floor.\n')
        self.assertEqual(self.r.intro, intro)

    def test_room_loads_title(self):
        with open(self.sample.path) as test:
            for line in test:
                if line == 'Title\n':
                    title = test.__next__()
        self.assertEqual(self.r.title, title)

    def test_room_loads_desc(self):
        desc = 'You are in a room. There is a window to the west.\n'
        self.assertEqual(self.r.desc, desc)

    def test_room_loads_items(self):
        items = {'silver spoon': 1, 'peanuts': 2}
        self.assertEqual(self.r.items, items)

    def test_room_loads_exits(self):
        exits = {'n': 'test_room2', 's': 'test_room3'}
        self.assertEqual(self.r.exits, exits)


class SuroyTestCase(unittest.TestCase):
    def setUp(self):
        self.test = suroy.Suroy('test_rooms')

    def test_load_rooms(self):
        loaded_rooms = {
            'begin': room.Room('test_rooms/begin.rdf'),
            'test_room2': room.Room('test_rooms/test_room2.rdf'),
            'test_room3': room.Room('test_rooms/test_room3.rdf'),
        }
        test_loaded = suroy.Suroy('test_rooms')
        self.assertEqual(test_loaded.rooms.keys(), loaded_rooms.keys())

    def test_move_room_north(self):
        self.test.parse_command('n')
        self.assertEqual(self.test.current_room, self.test.rooms['test_room2'])

    def test_move_room_south(self):
        self.test.parse_command('s')
        self.assertEqual(self.test.current_room, self.test.rooms['test_room3'])

    def test_look_room(self):
        try:
            self.test.parse_command('look')
        except Exception:
            self.fail()
