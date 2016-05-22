class Grammar(object):
    def __init__(self):
        self.verbs = []
        with open('verbs.grammar') as verbs:
            for verb in verbs:
                verb = verb.rstrip()
                synonyms = verb.split(',')
                self.verbs.append(synonyms)


    def recognize_verb(self, phrase):
        words = phrase.split(' ')
        size = len(words)
        for i in range(size):
            for verbs in self.verbs:
                if phrase in verbs:
                    return verbs[0]
        return False


def load_grammar():
    return Grammar()
