#My initials: R and P

# This is the cheating part:
#print('R', 'R', 'R', 'R', ' ', ' ', 'P', 'P', 'P', 'P', ' ')
#print('R', ' ', ' ', ' ', 'R', ' ', 'P', ' ', ' ', ' ', 'P')
#print('R', ' ', ' ', ' ', 'R', ' ', 'P', ' ', ' ', ' ', 'P')
#print('R', 'R', 'R', 'R', ' ', ' ', 'P', 'P', 'P', 'P', ' ')
#print('R', ' ', 'R', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ')
#print('R', ' ', ' ', 'R', ' ', ' ', 'P', ' ', ' ', ' ', ' ')
#print('R', ' ', ' ', ' ', 'R', ' ', 'P', ' ', ' ', ' ', ' ')

#This is the real code
for row in range(7):
  for col in range(12):
    if (row == 0 or row == 3) and col < 4:
      print('R', end='')
    elif (row == 1 or row == 2) and (col == 4):
      print('R', end='')
    elif col == 0 or (row > 3 and col == row - 2):
      print('R', end='')
    elif (row == 0 or row == 3) and (col > 5 and col < 10):
      print('P', end='')
    elif (row == 1 or row == 2) and (col == 10):
      print('P', end='')
    elif col == 6 :
      print('P', end='')
    else:
      print(' ', end='')
  print('')
