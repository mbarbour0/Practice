'''Iterating through a dictionary'''

dictionary = {'Roger': 32, 'AAron': 26, 'Jeremiah': 18, 'Ronda': 24, 'Craig': 23}

for key, value in dictionary.iteritems():
    print 'Our main man {} is tired of being {}'.format(key, value)


dictionary2 = {'cookies': 2.5, 'frying pans': 12.75, 'eggs': 2.25, 'ham': 4.25}

for k, v in dictionary2.iteritems():
    print 'The {} costs ${}'.format(k, v)


movies = {'Jurassic Park':7.25,'Jungle Book':8.8,'Sphere':7.1,'It':'Unknown','An':6.1}

for k,v in movies.iteritems():
    print 'The movie {} scored a {} from Matt'.format(k,v)


for k, v in dictionary.iteritems():
    print '{} is the homie, he rolls with {} other homies'.format(k,v)
    
    
    
'''Iterating through a set'''
    
''' A set indicates a series of values enclosed by a set of {} curly braces that
will only return unique values (no duplicates) of the data entered.'''

my_set = {1000,1000,2000,2000,2000,2000,1000,3000,4000,2000,9000}

print my_set

for i in my_set:
    print i