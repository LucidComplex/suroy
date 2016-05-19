import unittest
import os
import room

class RoomTestCase(unittest.TestCase):
    def setUp(self):
        sample_path = os.scandir('rooms')
        for sample in sample_path:
            if sample.is_file() and sample.name.startswith('test_'):
                if sample.name == 'test_room.rdf':
                    self.r = room.Room(sample)
                    self.sample = sample
                    break

    def test_room_takes_path(self):
        with open('rooms/test_room.rdf') as test:
            r = room.Room(test)
        self.assertEqual(r.file_path, 'rooms/test_room.rdf')

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
        exits = {'n': 'test_room2', 'w': 'test_room3'}
        self.assertEqual(self.r.exits, exits)

