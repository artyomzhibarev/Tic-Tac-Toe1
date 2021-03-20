step_checker = False
win_char = None
char_counter = 0
field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
grid = [['', '', ''], ['', '', ''], ['', '', '']]
print(f"---------"
      f"\n| {field[0][0]} {field[0][1]} {field[0][2]} |"
      f"\n| {field[1][0]} {field[1][1]} {field[1][2]} |"
      f"\n| {field[2][0]} {field[2][1]} {field[2][2]} |"
      f"\n---------")

while True:
    input_coord = list(input('Enter the coordinates: ').split())
    if not ((input_coord[0]).isdigit() and (input_coord[1]).isdigit()):
        print('You should enter numbers!')
        continue
    if not 0 < int(input_coord[0]) < 4:
        print('Coordinates should be from 1 to 3!')
        continue
    if not 0 < int(input_coord[1]) < 4:
        print('Coordinates should be from 1 to 3!')
        continue
    if grid[int(input_coord[0]) - 1][int(input_coord[1]) - 1]:
        print('This cell is occupied! Choose another one!')
        continue
    if not step_checker:
        grid[int(input_coord[0]) - 1][int(input_coord[1]) - 1] = "X"
        step_checker = True
        field[int(input_coord[0]) - 1][int(input_coord[1]) - 1] = 'X'
        char_counter += 1
    else:
        grid[int(input_coord[0]) - 1][int(input_coord[1]) - 1] = 'O'
        step_checker = False
        field[int(input_coord[0]) - 1][int(input_coord[1]) - 1] = 'O'
        char_counter += 1

    # rows check
    for row in grid:
        if ''.join(row) == 'XXX':
            win_char = 'X'
            break
        elif ''.join(row) == 'OOO':
            win_char = 'O'
            break

    # transpose grid
    transposed_grid = []
    for i in range(3):
        transposed_grid.append([row[i] for row in grid])
    # columns check
    for row in transposed_grid:
        if ''.join(row) == 3 * 'X':
            win_char = 'X'
            break
        elif ''.join(row) == 3 * 'O':
            win_char = 'O'
            break

    # diagonal checks
    if ''.join([grid[0][0], field[1][1], field[2][2]]) == 3 * 'X':
        win_char = 'X'
    elif ''.join([grid[0][0], field[1][1], field[2][2]]) == 3 * 'O':
        win_char = 'O'
    elif ''.join([grid[0][2], field[1][1], field[2][0]]) == 3 * 'X':
        win_char = 'X'
    elif ''.join([grid[0][2], field[1][1], field[2][0]]) == 3 * 'O':
        win_char = 'O'

    print(f"---------"
          f"\n| {field[0][0]} {field[0][1]} {field[0][2]} |"
          f"\n| {field[1][0]} {field[1][1]} {field[1][2]} |"
          f"\n| {field[2][0]} {field[2][1]} {field[2][2]} |"
          f"\n---------")

    if win_char:
        print(f'{win_char} wins')
        break
    if win_char is None and char_counter > 8:
        print('Draw')
        break
