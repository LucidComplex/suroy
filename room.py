import os

class Room(object):
    def __init__(self, *args, **kwargs):
        self.file_path = None
        self.intro = None
        self.title = None
        self.desc = None
        self.items = None
        self.exits = None
        try:
            self.file_path = args[0].path
        except AttributeError:
            self.file_path = args[0].name
        with open(self.file_path) as room_data:
            temp = []
            use = False
            is_item = False
            is_exit = False
            for line in room_data:
                l = str.lower(line.rstrip())
                if l in self.__dict__:
                    temp = []
                    attr = l
                    use = True
                    if l == 'items':
                        is_item = True
                        temp = {}
                    if l == 'exits':
                        is_exit = True
                        temp = {}
                    continue
                if l == 'end' and use:
                    use = False
                    if is_item or is_exit:
                        is_item = False
                        is_exit = False
                    else:
                        temp = ''.join(temp)
                    setattr(self, attr, temp)
                    continue
                if use:
                    if is_item:
                        count, name = l.split(' ', 1)
                        temp[name] = int(count)
                    elif is_exit:
                        direction, name = l.split(' ', 1)
                        temp[direction] = name
                    else:
                        temp.append(line)
