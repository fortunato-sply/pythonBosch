global coluna 
coluna = [
            [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ']
         ]

def printGame(coluna):
    print(f'''
      1   2   3   4   5   6   7
    | {coluna[0][5]} | {coluna[1][5]} | {coluna[2][5]} | {coluna[3][5]} | {coluna[4][5]} | {coluna[5][5]} | {coluna[6][5]} |
    | {coluna[0][4]} | {coluna[1][4]} | {coluna[2][4]} | {coluna[3][4]} | {coluna[4][4]} | {coluna[5][4]} | {coluna[6][4]} |
    | {coluna[0][3]} | {coluna[1][3]} | {coluna[2][3]} | {coluna[3][3]} | {coluna[4][3]} | {coluna[5][3]} | {coluna[6][3]} |
    | {coluna[0][2]} | {coluna[1][2]} | {coluna[2][2]} | {coluna[3][2]} | {coluna[4][2]} | {coluna[5][2]} | {coluna[6][2]} |
    | {coluna[0][1]} | {coluna[1][1]} | {coluna[2][1]} | {coluna[3][1]} | {coluna[4][1]} | {coluna[5][1]} | {coluna[6][1]} |
    | {coluna[0][0]} | {coluna[1][0]} | {coluna[2][0]} | {coluna[3][0]} | {coluna[4][0]} | {coluna[5][0]} | {coluna[6][0]} |
      ''')
      
# =============================================================================
# for i in range(1,8):
#     print(f"{i}".center(5, ' '), end='')
#     for n in range(0, 7):
#         print(f'| {coluna[i-1][n-1]} |'.center(5, ' '))
# =============================================================================

      

def putInColumn(part, column):
    for i in range(0, 6):
        if coluna[column][i] == ' ':
            coluna[column][i] = part
            break
        else:
            print('nao entrou')
    
def verifyPoints(part): 
    for i in range(0, 7):
        for j in range(0,6):
            print(i, j)
            if coluna[i][j] != ' ':
                print(coluna[i][j])
                

while 1:
    verifyPoints('o')
    printGame(coluna)
    putInColumn('o', 0)
    input()
# print(tabuleiro)
# putInColumn('o', 0)
# print(coluna)