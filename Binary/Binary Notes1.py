#Binary notes 1

'''Translating from a number to the corresponding binary number'''

print bin(2)
print bin(3)
print bin(4)
print bin(5)

'''Using int to translate (number, base), so ('1', 2) would return the base 2
equivalant of the number 1'''

print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
print int('11001001', 2)

'''Binary operators >> and << . >> shifts binary digits over by a specified
number of times. If you were to shift over 8 >> 2 it would equal 1.
8 in binary is 100, shifted over 2 places to the right, it equals 001, which
translates to 1 in binary'''

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

print shift_right
print shift_left

'''The & operator looks at the bits in common between two values and returns
the result of only those common bits, for instance 0b10101 & 0b111 would return
0b101 or the value of 5'''

print bin(0b1110 & 0b101)
print bin(0b100)

'''Similar to how the & operator works, the | operator takes the result of
each binary number if either of the numbers resulted in a 1 in that digit'''

print bin(0b1110 | 0b101)
print bin(0b1111) #aka 15
print 0b1111

'''The ^ operator takes only the bits if only 1 of the numbers contains a 1
for that digit'''

print 0b1110 ^ 0b101
print bin(11)

'''Using the ~ operator you add 1 to a number and flip it to negative'''

print ~1
print ~2
print ~3
print ~42
print ~123

'''Using a bitmask with the & operator'''

def check_bit4(input):
  mask = 0b1000
  desired = input & mask
  if desired > 0:
    return "on"
  else:
    return "off"

'''Using a mask to turn bits on using the | operator'''

a = 0b10111011
mask = 0b100
print bin(a | mask)

'''Bitflipping using the ^ operator and a mask'''

a = 0b11101110
mask = 0b11111111
print bin(a ^ mask)

'''Flip the bit to the corresponding distance using shift left to place a 0b1
in a particular digit.'''

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)

def flip_bit(number, n):
  mask = 0b1 << (n-1)
  result = bin(mask ^ number)
  return result

print flip_bit(0b1000, 6)
