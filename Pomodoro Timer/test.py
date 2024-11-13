from collections import deque

list123 = [1, 2, 3]

deck_it = deque(list123)
result = deck_it.rotate(-1)

print(result)