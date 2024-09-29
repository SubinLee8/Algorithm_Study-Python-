num = int(input())
direction = input().split()
x,y=1,1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
movesType=['L','R','U','D']

for i in direction:
    for j in range(len(movesType)):
        if i==movesType[j]:
            nx=x+dx[j]
            ny=y+dy[j]
    if nx<1 or ny<1:
        continue
    x=nx
    y=ny

print(x,y)