# This will break sentences into (word_type, word) 
directions = ['north', 'south', 'east', 'west',
    'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'from', 'of', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(sentence) :
    """Turns a string of words into a list of (type, word) pairs.

    Args:
        sentence - The string of words to scan through
    Returns:
        a list of type, word tuples contained in the sentence
    """
    lex = []
    words = sentence.split()
    
    for w in words :
        w = w.lower().strip('?!.,')
        if w in directions :
            lex.append(('direction', w))
        elif w in verbs :
            lex.append(('verb', w))
        elif w in stops :
            lex.append(('stop', w))
        elif w in nouns :
            lex.append(('noun', w))
        else :
            try :
                num = int(w)
                lex.append(('number', num))
            except ValueError as e :
                lex.append(('error', w))

    return lex

