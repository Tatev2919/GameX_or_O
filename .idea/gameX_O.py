import re

gameL = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
print(gameL)
finish = 0
count = 0
x_or_o = ""
second_player = ""
first_player = input("Is first start x player or o player ? /enter x or o ").strip()

while first_player not in ('x', 'o'):
    print("correct your asnwer enter x or o ")
    first_player = input("enter x or o ").strip()
if (first_player == 'x'):
    second_player = 'o'
else:
    second_player = 'x'

while (finish == 0):
    x = input("enter x coordinate").strip()
    y = input("enter y coordinate").strip()
    if ((re.match("^[0-2]$", x)) == None) | ((re.match("^[0-2]$", y)) == None):
        print("please reenter the values")
        continue
    else:
        x = int(x)
        y = int(y)

        if (gameL[x][y] in ('-')):
            if (count % 2 == 0):
                if (first_player == 'o'):
                    gameL[x][y] = 'o'
                else:
                    gameL[x][y] = 'x'
            else:
                if first_player == 'x':
                    gameL[x][y] = 'o'
                else:
                    gameL[x][y] = 'x'
            count += 1
            print(count)
        if count > 4:
            print("more than 5")
            i = x
            j = y
            h = v = c = 0
            if (count % 2 == 0):
                x_or_o = second_player
            else:
                x_or_o = first_player
            print(x_or_o)
            for raw in gameL:
                if raw[y] == x_or_o:
                    h += 1
                if h == 3:
                    finish = 1
                    break
                if v == x:
                    if (raw[0] == raw[1] == raw[2] == x_or_o):
                        finish = 1
                        break
                v += 1

            # need to be modifed:

            for k in range(3):
                for m in range(3):
                    if (k == m):  # | (k + m == 2):
                        print(x_or_o)
                        print(gameL[k][m], "  k:", k, "  m:", m)
                        if (gameL[k][m] == x_or_o):
                            c += 1
                            print(c)
                    if c == 3:
                        finish = 1
                        break
                    # if ( (k + m) == 2):
                    #     print(x_or_o)
                    #     print(gameL[k][m],"  k:",k,"  m:",m)
                    #     if (gameL[k][m] == x_or_o):
                    #         finish = 1
                    #         break
        print(gameL)

for row in gameL:
    print(row)

print("Game Over")

