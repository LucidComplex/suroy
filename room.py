import os

def load_rooms(directory):
    try:
        room_paths = os.scandir(directory)
    except FileNotFoundError:
        return
    for room in room_paths:
        if room.is_file() and room.name.endswith('.rdf'):
            x = Room(room)
            print(x)

class Room(object):
    def __init__(self, *args, **kwargs):
        self.file_path = None
        self.intro = None
        self.title = None
        self.desc = None
        try:
            self.file_path = args[0].path
        except AttributeError:
            self.file_path = args[0].name
        with open(self.file_path) as room_data:
            temp = []
            use = False
            for line in room_data:
                l = str.lower(line.rstrip())
                print(l)
                if l in self.__dict__:
                    attr = l
                    use = True
                    continue
                if l == 'end':
                    use = False
                    temp = ''.join(temp)
                    setattr(self, attr, temp)
                    temp = []
                    continue
                if use:
                    temp.append(line)

