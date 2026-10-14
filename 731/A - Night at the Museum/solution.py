s = input()
pos = 'a'
moves = 0
for ch in s:
    diff = abs(ord(ch) - ord(pos))
    moves += min(diff, 26 - diff)
    pos = ch
print(moves)