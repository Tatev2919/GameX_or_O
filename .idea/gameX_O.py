import re

gameL = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
print(gameL)
finish = 0
count = 0
first_player = input("Is first start x player or o player ? /enter x or o ")
while first_player not in('x','o'):
    print("correct your asnwer enter x or o ")
    first_player = input("enter x or o ")

while (finish == 0):
    x = input("enter x coordinate")
    y = input("enter y coordinate")
    if ((re.match("^[0-2]$", x)) == None) | ((re.match("^[0-2]$", y)) == None):
        print("please reenter the values")
        continue
    else:
        x = int(x)
        y = int(y)
        if (gameL[x][y] in ('-')):
            count += 1
            if (count % 2 == 0):
                if (first_player == 'o'):
                    gameL[x][y] = 'x'
                else:
                    gameL[x][y] = 'o'
            else:
                if first_player == 'x':
                    gameL[x][y] = 'x'
                else:
                    gameL[x][y] = 'o'

            print(count)
        if count >= 5:
            i = x
            h = v = 0
            j = y
            x_or_o = ""
            if (count % 2 == 0):
                x_or_o = 'o'
            else:
                x_or_o = 'x'
            while (h < 3) & (v < 3):
                if gameL[i][h] == x_or_o:
                    h += 1
                if gameL[v][j] == x_or_o:
                    v += 1
                else:
                    break
            if (h == 3) | (v == 3):
                print("finish")
                finish = 1
    print(gameL)
