'''List comprehension to write to a file'''

my_list = [i ** 2 for i in range(1, 11)]

my_file = open("output.txt", "w")

for v in my_list:
  my_file.write(str(v) + '\n')
  
my_file.close()

'''Printing file contents'''

my_file = open('output.txt', 'r')

print my_file.read()

my_file.close()

'''Readline to read individual lines'''

my_file = open('text.txt', 'r')

print my_file.readline()
print my_file.readline()
print my_file.readline()

my_file.close()


'''Using with and as to assign a name, write to the file, and close after
being run.'''

with open('test.txt', 'w') as filename:
  filename.write('Success!')
  