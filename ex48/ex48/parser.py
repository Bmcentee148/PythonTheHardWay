#-- Class Definitions --#

class Sentence(object) :
    """A sentence structure containing a subject, verb, and object."""
    
    def __init__(self, subject, verb, obj) :
        """Constructor for Sentence class objects

        Parameters:
            subject -- the tuple containing the subject of the sentence
            verb -- the tuple containing the verb used in the sentence
            obj -- the tuple containing the object of the sentence
        """
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]
# end Sentence class

#-- Custom Exception Classes --#

class ParseError(Exception) :

    def __init__(self, msg) :
        self.msg = msg

#-- Functions designed to aid in parsing --#

def peek(scanned_sentence) :
    result = None
    if scanned_sentence :
        word = scanned_sentence[0]
        result = word[0]
    return result

def match(scanned_sentence, expecting) :
    result = None
    if scanned_sentence :
        word = scanned_sentence.pop(0)
        if word[0] == expecting :
            result = word
    return result

def skip(scanned_sentence, word_type) :
    while peek(scanned_sentence) == word_type :
        match(scanned_sentence, word_type)


#-- Basic text parsing functions --#

def parse_verb(scanned_sentence) :
    skip(scanned_sentence, 'stop')
    if peek(scanned_sentence) == 'verb' :
        return match(scanned_sentence, 'verb')
    else :
        raise ParseError("Error parsing: Expected a verb next.")

def parse_subject(scanned_sentence) :
    pass

def parse_object(scanned_sentence) :
    pass