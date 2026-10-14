import sys
 
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
 
    def calc(start_white):
        white = a
        dark = b
        size = 1
        layers = 0
        cur_white = start_white
        while True:
            if cur_white:
                if white < size:
                    break
                white -= size
            else:
                if dark < size:
                    break
                dark -= size
            layers += 1
            size *= 2
            cur_white = not cur_white
        return layers
 
    print(max(calc(True), calc(False)))