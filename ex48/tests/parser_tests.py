from nose.tools import *
from ex48.parser import *

def test_sentence_class() :
    s = Sentence(('noun','player'), ('verb','go'), ('noun','north'))
    assert_equals(s.subject , "player")
    assert_equals(s.verb , "go")
    assert_equals(s.obj , "north")

def test_peek() :
    assert_equals(peek([('verb','go'), ('noun','princess')]), 'verb' )

def test_match() :
    assert_equals(match([('verb','go'), ('noun','princess')], 'verb'),
         ('verb', 'go'))
    
    assert_equals(match([('verb','go'), ('noun','princess')], 'noun'), None)
    
    assert_equals(match([('noun','bear'), ('noun','princess')], 'noun'),
         ('noun', 'bear'))

    assert_equals(match([],'verb'), None)


def test_parse_verb() :
    wordlist = [('stop','the'), ('error','baby'),('verb','go'),
        ('direction','north'), ('noun','princess')]
    emptylist = []
    assert_equals(parse_verb(wordlist), ('verb', 'go') )
    assert_raises(ParseError, parse_verb, emptylist )
    assert_raises(ParseError, parse_verb, 
        [('stop','the'), ('noun','princess')] )



def test_parse_subject() :
    assert_equals(parse_subject([('verb','go'),('direction','north')]), 
        ('noun','player'))
    assert_equals(parse_subject([('noun','princess'),('verb','go'),
        ('direction','north')]), ('noun','princess'))
    assert_raises(ParseError, parse_subject ,
        [('direction','south'),('noun','princess')])

def test_parse_object() :
    assert_equals(parse_object([('stop','is'),('direction','north')]), 
        ('direction','north'))
    assert_equals(parse_object([('stop','the'),('noun','princess'),
        ('direction','north')]), ('noun','princess'))
    assert_raises(ParseError, parse_object ,
        [('verb','eat'),('noun','princess')])

def test_parse_sentence() :
    words = [('noun','princess'),('verb','eat'),('noun','bear')]
    s = Sentence(('noun','princess'), ('verb','eat'), ('noun','bear'))
    assert_equals(parse_sentence(words), s)

    words = [('verb','eat'),('noun','bear')]
    s = Sentence(('noun','player'), ('verb','eat'), ('noun','bear'))
    assert_equals(parse_sentence(words), s)

    words = [('direction','north'),('verb','eat'),('noun','bear')]
    assert_raises(ParseError, parse_sentence, words)
