#-- Class Definitions --#

class Sentence(object) :
    """A sentence structure containing a subject, verb, and object."""
    
    def __init__(self, subject, verb, obj) :
        """Constructor for Sentence class objects

        Parameters:
            subject -- the tuple containing the subject of the sentence
            verb -- the tuple containing the verb used in the sentence
            object -- the tuple containing the object of the sentence
        """
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]
# end Sentence class

#-- Functions in parser module --#

def peek(scanned_sentence) :
    if scanned_sentence :
        word = scanned_sentence[0]
        return word[0]
    else : 
        return None





