# Simple skeleton file for running tests on our project

from nose.tools import *
from ex47prac.practice import *

brian = Person("Brian","McEntee")
casey = Person("Casey","McEntee")
michael = Person("Mike","McEntee")

def test_room() :
    assert_equal(casey.firstname, "Casey")
    assert_equal(casey.lastname, "McEntee")
    assert_equal(casey.get_family_size(), 0)

def test_persons_family() :
    brian.add_family_members({'sister' : casey, 'dad' : michael})
    casey.add_family_members({'brother' : brian, 'dad' : michael})
    michael.add_family_members({'daughter' : casey, 'son' : brian})
    
    assert_equal(brian.get_family_member('sister'), casey)
    assert_equal(brian.get_family_member('dad'), michael)
    assert_equal(brian.get_family_member('sister').get_family_member('dad'),
        michael)
    assert_equal(brian.get_family_size(), 2)

def test_info() :
    person_info = casey.get_info()
    assert_equal(person_info, "McEntee, Casey")

def test_member_error() :
    assert_raises(FamilyMemberError,
        casey.add_family_members,{'cousin' : brian})