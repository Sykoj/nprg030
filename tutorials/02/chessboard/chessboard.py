ascii_code_A = 65

chessboard = [] # [i] returns i-th row of chessboard
for x in range(8):
    chessboard.append([0] * 8)

def index_to_column_letter(index):
    return chr(index + ascii_code_A)

def index_from_column_letter(letter):
    return ord(letter) - ascii_code_A

def print_chessboard():
    max_value = max([ max(row) for row in chessboard])
    max_value_length = len(str(max_value))
    
    if max_value_length < 2: # make space for letters A
        max_value_length = 2

    def print_cell(value = '', separator = '|'):
        print(str(value).ljust(max_value_length), end = separator)

    def print_letters():
        print_cell()
        for index in range(len(chessboard)):
            print_cell(index_to_column_letter(index), separator = '+')

    def print_row(row_index):
        print_cell(row_index + 1)
        for value in chessboard[row_index]:
            print_cell(value)

    print_letters()
    for row_index in range(len(chessboard)):
        print() # insert new line
        print_row(row_index)


# read input

row = input()

while row != '-1':
    coordinate = row[:2]
    number = int(row[3:])

    coordinate_y = int(coordinate[0]) - 1
    coordinate_x = index_from_column_letter(coordinate[1])
    
    if chessboard[coordinate_y][coordinate_x] != 0:
        print('Position already occupied: ' + coordinate)
        exit()
    else:
        chessboard[coordinate_y][coordinate_x] = number

    row = input()

print_chessboard()