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

    def __eq__(self, other) :
        return (self.subject == other.subject and
                self.verb == other.verb and
                self.obj == other.obj)
# end Sentence class

#-- Custom Exception Classes --#

class ParseError(Exception) :
    """Raised when we parse through an unexpected type of word."""
    def __init__(self, msg) :
        self.msg = msg

#-- Functions designed to aid in parsing --#

def peek(word_list) :
    """Look at the next words type in the scanned sentence without removal.
    
    Args:
        word_list - A list of type, word tuples from a sentence
    Returns:
        the type of word that is next in the list or None if the list is empty
    """
    result = None
    if word_list :
        word = word_list[0]
        result = word[0]
    return result

def match(word_list, expecting) :
    """Get and remove the next word from the list if it is the expected type.

    Args:
        word_list - A list of type, word tuples from a sentence
        expecting - the expected type of word we want from the list
    Returns:
        the next type, word tuple in list if expected type, else None
    """
    result = None
    if word_list :
        word = word_list.pop(0)
        if word[0] == expecting :
            result = word
    return result

def skip(word_list, word_types) :
    """Skips all sequential words in the word list of the given type.
    
    Args:
        word_list - A list of type,word tuples from a sentence
        word_type - the type of words we would like to skip over in the list
    """
    while peek(word_list) in word_types :
        match(word_list, peek(word_list))


#-- Basic sentence structure parsing functions --#

def parse_verb(word_list) :
    """Parse a scanned word list for the verb in the sentence.
    
    Args:
        word_list - list of type,word tuples from a sentence
    Returns:
        the next word of type verb found in the list
    Raises:
        ParseError - if the next word type found is not of type verb
    """
    skip(word_list, ['stop','error'])
    if peek(word_list) == 'verb' :
        return match(word_list, 'verb')
    else :
        raise ParseError("Error parsing: Expected a verb next.")

def parse_subject(word_list) :
    """Parse a scanned word list for the subject in the sentence.
    
    Args: 
        word_list - list of type,word tuples from the sentence
    Returns:
        the subject of the sentence from the word list
    Raises:
        ParseError - if the next type of word found is not a noun or verb
    """
    skip(word_list, ['stop','error'])
    if peek(word_list) == 'noun' :
        return match(word_list, 'noun')
    elif peek(word_list) == 'verb' :
        return ('noun', 'player')
    else :
        raise ParseError("Error parsing: Expected a noun or verb next.")

def parse_object(word_list) :
    """Parse a scanned word list for the object in the sentence.
    
    Args:
        word_list - list of type,word tuples from the sentence
    Returns:
        the object of the sentence from the word list
    Raises:
        ParseError - if the next type of word is not a noun or direction
    """     
    skip(word_list, ['stop','error'])
    if peek(word_list) == 'noun' :
        return match(word_list, 'noun')
    elif peek(word_list) == 'direction' :
        return match(word_list, 'direction')
    else :
        raise ParseError("Error parsing: Expected a noun or direction.")

def parse_sentence(word_list) :
    subject = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subject, verb, obj)
