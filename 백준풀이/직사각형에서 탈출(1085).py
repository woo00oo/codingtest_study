# 직사각형은 경계선까지의 거리 고려에서 대각선이 최소인 경우가 없으므로 대각선은 고려하지 않아도 됨.
# x,y 까지 고려해야하는 이유는 x,y 좌표기준으로 w,h까지의 거리와 0,0까지의 거리를 고려해야하기 때문.

x, y, w, h = map(int, input().split())
print(min([x,y,w-x,h-y]))