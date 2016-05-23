class Grammar(object):
    def __init__(self):
        self.verbs = []
        with open('verbs.grammar') as verbs:
            for verb in verbs:
                verb = verb.rstrip()
                synonyms = verb.split(',')
                self.verbs.append(synonyms)

    def recognize(self, type, phrase):
        words = phrase.split(' ')
        size = len(words)
        for i in range(size):
            for t in getattr(self, type):
                if ' '.join(words[:size - i]) in t:
                    return t[0], ' '.join(words[size - i:])
        return False, False


def load_grammar():
    return Grammar()
