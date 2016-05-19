import unittest
import os
import room

class RoomTestCase(unittest.TestCase):
    def test_room_takes_path(self):
        with open('rooms/test_room.rdf') as test:
            r = room.Room(test)
        self.assertEqual(r.file_path, 'rooms/test_room.rdf')

    def test_room_loads_intro(self):
        sample_path = os.scandir('rooms')
        for sample in sample_path:
            if sample.is_file() and sample.name.startswith('test_'):
                r = room.Room(sample)
                sample = sample
                break
        with open(sample.path) as test:
            for line in test:
                if line == 'Intro\n':
                    intro = test.__next__()
        self.assertEqual(r.intro, intro)

    def test_room_loads_title(self):
        sample_path = os.scandir('rooms')
        for sample in sample_path:
            if sample.is_file() and sample.name.startswith('test_'):
                r = room.Room(sample)
                sample = sample
                break
        with open(sample.path) as test:
            for line in test:
                if line == 'Title\n':
                    title = test.__next__()
        self.assertEqual(r.title, title)

    def test_room_loads_desc(self):
        sample_path = os.scandir('rooms')
        for sample in sample_path:
            if sample.is_file() and sample.name.startswith('test_'):
                r = room.Room(sample)
                sample = sample
                break
        desc = ('You are in a room. There is a window to the west.\n'
                'You notice a silver spoon on the floor.\n')
        self.assertEqual(r.desc, desc)

