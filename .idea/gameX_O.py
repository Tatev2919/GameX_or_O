import re

gameL = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']];
print(gameL)
finish = 0;
count = 0;

while (finish == 0):
    x = int(input("enter x coordinate"));
    if (x < 0 | x>3):
        print("please reenter the value");
        y = int(input("enter y coordinate"));
        if (y < 0 | y > 3):
            print("please reenter the value");
    elif (gameL[x][y] not in ('x', 'O')):
        if (count % 2 == 0):
            gameL[x][y] = 'x';
        else:
            gameL[x][y] = 'O';
        count += 1;
    print(gameL)

    if(gameL[0][0] == gameL[0][1] == gameL[0][2]):
        print(True)
