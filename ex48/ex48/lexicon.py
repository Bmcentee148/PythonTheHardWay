# This will break sentences into (word_type, word) 
directions = ['north', 'south', 'east', 'west',
    'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'from', 'of', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

def scan(sentence) :
    lex = []
    words = sentence.split()
    
    for w in words :
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