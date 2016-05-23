class Item(object):
    def __init__(self, path):
        self.use_cases = {}
        with open(path) as item_data:
            for line in item_data:
                l = str.lower(line.rstrip())
                if l == 'title':
                    self.title = next(item_data).rstrip()
                elif l == 'desc':
                    self.description = next(item_data).rstrip()
                elif l == 'use':
                    use_case = str.strip(next(item_data))
                    while str.lower(use_case) != 'end':
                        on, text, drop = use_case.split(':')
                        if len(str.strip(drop)) == 0:
                            self.drop_on_use = False
                        else:
                            self.drop_on_use = True
                        self.use_cases[on] = text
                        use_case = str.strip(next(item_data))
