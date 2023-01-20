from _collections import deque

# popleft()
# Remove and return an element from the left side of the deque.

q = deque()
p = deque()

q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
print(q)

for item in (q):
    print(item)

print(len(q))
