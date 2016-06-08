# This is a simple mod to hold classes we will test with nosetests

class Person(object) :

    def __init__(self, firstname, lastname) :
        self.firstname = firstname
        self.lastname = lastname
        self.family = {}

    def get_info(self) :
        return "{1}, {0}".format(self.firstname, self.lastname)

    def add_family_members(self, members) :
        family_kw = ['son', 'daughter', 'dad', 'mom', 'brother','sister']
        for member in members :
            if member not in family_kw :
                raise FamilyMemberError(member,
                    'Error: key for family member not recognized')
        self.family.update(members)

    def get_family_member(self, name) :
        return self.family.get(name, None)

    def get_family_size(self) :
        return len(self.family)

class FamilyError(Exception) :
    # Base class for errors raised in Person class
    pass

class FamilyMemberError(FamilyError) :

    def __init__(self, member, msg) :
        self.member = member
        self.msg = msg

