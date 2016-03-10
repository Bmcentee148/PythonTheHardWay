# create a mapping of state to abbreviation
states = [
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
]

cities = [
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
]

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#pint out some cities
print '-' * 10
print "New York State has: ", cities['NY']
print "Oregon State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

