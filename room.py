import os

class Room(object):
    def __init__(self, *args, **kwargs):
        self.file_path = None
        self.intro = None
        self.title = None
        self.desc = None
        self.items = None
        self.n = None
        self.s = None
        self.w = None
        self.e = None
        try:
            self.file_path = args[0].path
        except AttributeError:
            self.file_path = args[0].name
        with open(self.file_path) as room_data:
            temp = []
            use = False
            is_item = False
            for line in room_data:
                l = str.lower(line.rstrip())
                if l in self.__dict__:
                    temp = []
                    attr = l
                    use = True
                    if l == 'items':
                        is_item = True
                        temp = {}
                    continue
                if l == 'end' and use:
                    use = False
                    if is_item:
                        is_item = False
                    else:
                        temp = ''.join(temp)
                    setattr(self, attr, temp)
                    continue
                if use:
                    if is_item:
                        count, name = l.split(' ', 1)
                        temp[name] = int(count)
                    else:
                        temp.append(line)
