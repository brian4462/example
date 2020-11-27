'''
기본 아이디어 및 규칙
- 4방향 이동가능 (상하좌우)
- 벽으로는 이동 불가능
- 목표지점에 도착시 도착텍스트 출력

XXXXXXXX X
XXXXXXXX X
X        X
X XXXXXXXX
XOXXXXXXXX

'X':0
' ':1
'O':2

'''
#맵 초기 정보 (2차원배열)
map =  [
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,0,0],
        [0,2,0,0,0,0,0,0,0,0]
       ]

#초기 현재 위치 정보
current_X = 4
current_Y = 1


while True:
    #맵 출력
    print()
    for i in range(5):
        line = '        '
        for j in range(10):
            if map[i][j] == 0:
                line += 'X'
            elif map[i][j] == 1:
                line += ' '
            elif map[i][j] == 2:
                line += 'O'
        print(line)
    
    #탈출확인
    if map[0][8]==2:
        print()
        print('  XXXXXXXXXXXXXXXXXXXXXX')
        print('  X  CONGRATULATIONS!  X')
        print('  XXXXXXXXXXXXXXXXXXXXXX')
        break
    
    #문제 출력
    print()
    print('         (w : 위)')
    print('(a : 좌) (s : 아래) (d : 우)')
    command = input("다음행동을 입력하세요 : ")

    #현재위치 계산
    prev_location = [current_X,current_Y]
    if command.lower() == 'w':
        if current_X > 0:
            if map[current_X-1][current_Y] == 1:
                current_X -= 1
            else:
                print('더 이상 이동할 수 없습니다')
        else:
            print('더 이상 이동할 수 없습니다')
    elif command.lower() == 's':
        if current_X < 4:
            if map[current_X+1][current_Y] == 1:
                current_X += 1
            else:
                print('더 이상 이동할 수 없습니다')
        else:
            print('더 이상 이동할 수 없습니다')
    elif command.lower() == 'a':
        if current_Y > 0:
            if map[current_X][current_Y-1] == 1:
                current_Y -= 1
            else:
                print('더 이상 이동할 수 없습니다')
        else:
            print('더 이상 이동할 수 없습니다')
    elif command.lower() == 'd':
        if current_Y < 9:
            if map[current_X][current_Y+1] == 1:
                current_Y += 1
            else:
                print('더 이상 이동할 수 없습니다')
        else:
            print('더 이상 이동할 수 없습니다')
    next_location = [current_X,current_Y]

    #위치 이동
    map[prev_location[0]][prev_location[1]] -= 1
    map[next_location[0]][next_location[1]] += 1


