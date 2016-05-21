class Grammar(object):
    def __init__(self):
        with open('verbs.grammar') as verbs:
            v = [verb.rstrip() for verb in verbs]
        with open('nouns.grammar') as nouns:
            n = [noun.rstrip() for noun in nouns]
        with open('determiner.grammar') as determiners:
            d = [det.rstrip() for det in determiners]

        self.verbs = v
        self.nouns = n
        self.determiners = d
        self.valid = ('verb', 'verb noun', 'verb determiner noun')

    def check_type(self, word):
        if word in self.verbs:
            return 'verb'
        if word in self.nouns:
            return 'noun'
        if word in self.determiners:
            return 'determiner'

    def check_grammar(self, command):
        com_split = command.split(' ')
        types = [self.check_type(word) for word in com_split]
        if ' '.join(types) in self.valid:
            return True
        return False
