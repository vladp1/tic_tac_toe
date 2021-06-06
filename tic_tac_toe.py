def print_battlefield():  # печать игрового поля
  print('---------')
  print('|', field[0][0], field[0][1], field[0][2], '|')
  print('|', field[1][0], field[1][1], field[1][2], '|')
  print('|', field[2][0], field[2][1], field[2][2], '|')
  print('---------')

a = "          "  # input('Enter cells:')
field = [[a[0], a[1], a[2]], [a[3], a[4], a[5]], [a[6], a[7], a[8]]]

print_battlefield()

flag = 'X'
while True:

  while True:
    y, x = input("Enter the coordinates:").split()
    try:
      y = int(y)
      x = int(x)
    except TypeError:
      print("You should enter numbers!")
    if x < 1 or x > 3 or y < 1 or y > 3:
      print("Coordinates should be from 1 to 3!")
    elif field[y-1][x-1] == "X" or field[y-1][x-1] == "O": 
      print("This cell is occupied! Choose another one!")
    else: 
      field[y-1][x-1] = flag
      break


  print_battlefield()

  x_wins = ((field[0][0] == field[0][1] == field[0][2] == 'X')\
       or (field[1][0] == field[1][1] == field[1][2] == 'X')\
       or (field[2][0] == field[2][1] == field[2][2] == 'X')\

       or (field[0][0] == field[1][0] == field[2][0] == 'X')\
       or (field[0][1] == field[1][1] == field[2][1] == 'X')\
       or (field[0][2] == field[1][2] == field[2][2] == 'X')\

       or (field[0][0] == field[1][1] == field[2][2] == 'X')\
       or (field[0][2] == field[1][1] == field[2][0] == 'X')\
         )

  o_wins = ((field[0][0] == field[0][1] == field[0][2] == 'O')\
       or (field[1][0] == field[1][1] == field[1][2] == 'O')\
       or (field[2][0] == field[2][1] == field[2][2] == 'O')\

       or (field[0][0] == field[1][0] == field[2][0] == 'O')\
       or (field[0][1] == field[1][1] == field[2][1] == 'O')\
       or (field[0][2] == field[1][2] == field[2][2] == 'O')\

       or (field[0][0] == field[1][1] == field[2][2] == 'O')\
       or (field[0][2] == field[1][1] == field[2][0] == 'O')\
         )

  count_x = 0
  count_o = 0
  for i in field:
    for j in i:
      if j == 'X':
        count_x += 1
      if j == 'O':
        count_o += 1

  print(f"XX={count_x}, OO={count_o}")

  if abs(count_x - count_o) > 1 or (x_wins and o_wins):
    print('Impossible')
  elif x_wins:
    print('X wins')
    break
  elif o_wins:
    print('O wins')
    break
  elif (count_x + count_o) < 9:
    print('Game not finished')
  else:
    print('Draw')
    break

  if flag == "X":
    flag = "O"
  else:
    flag = "X"
