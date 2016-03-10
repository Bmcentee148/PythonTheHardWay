# create a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Francisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

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

# do it using the cities and states dicts
print '-' * 10
print "Michigan State has: ", cities[states['Michigan']]
print "Florida State has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbreviation in states.items() :
    print "%s is abbreviated as %s." % (state, abbreviation)

# print every city in state
print '-' * 10
for abbrev, city in cities.items() :
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbreviation in states.items() :
    "%s state is abbreviated as %s, and has the city %s" % (
        state, abbreviation, cities[abbreviation])

print '-' * 10
# safely get an abbreviation given a state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state Texas is: %s" % city
