invalid_msg = 'Invalid values have been entered.'

def rgb_hex():
  red = int(raw_input('Please enter a value for Red: '))
  if red < 0 or red > 255:
    print invalid_msg
    return
  green = int(raw_input('Please enter a value for Green: '))
  if green < 0 or green > 255:
    print invalid_msg
    return
  blue = int(raw_input('Please enter a value for Blue: '))
  if blue < 0 or blue > 255:
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + blue
  print '%s' % (hex(val)[2:]).upper()

def hex_rgb():
  hex_val = raw_input('Please enter a hexidecimal value: ')
  if len(hex_val) != 6:
    print invalid_msg
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print 'Red: %s, Green: %s, Blue %s' % (red, green, blue)
  
def convert():
  while True:
    option = raw_input('Enter 1 to conver RGB to Hex. Enter 2 to convert HEX to RGB. Enter X to Exit: ')
    if option == '1':
      rgb_hex()
    elif option == '2':
      hex_rgb
    elif option == 'X':
      break
    else:
      print invalid_msg
      
convert()