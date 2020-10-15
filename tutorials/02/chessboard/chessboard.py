ascii_code_A = 65

chessboard = [] # [i] returns i-th row of chessboard
for x in range(8):
    chessboard.append([0] * 8)

row = input()

while row != '-1':
    coordinate = row[:2]
    number = int(row[3:])

    coordinate_y = int(coordinate[0]) - 1
    coordinate_x = ord(coordinate[1]) - ascii_code_A
    
    if chessboard[coordinate_y][coordinate_x] != 0:
        print('Position already occupied: ' + coordinate)
        exit()
    else:
        chessboard[coordinate_y][coordinate_x] = number

    row = input()

print(chessboard)