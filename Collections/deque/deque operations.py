from collections import deque

# Declaring deque
queue = deque(['name','age','DOB']) 
print(queue)

# Appending
# ----------

# appending to the end of the queue
queue.append("end")
print(queue)

# appending to the beginning of the queue
queue.appendleft("beginning")
print(queue)


# Popping
# --------

# Popping from the end
queue.pop()
print(queue)

# Popping from the beginning
queue.popleft()
print(queue)


# Other operations
# ----------------

# getting index
print(queue.index("name"))
print(queue.index("name", 0,3)) # from 0 to 3
# print(queue.index("name", 1,3)) # will give error as name is not in 1 to 3


# inserting at particular index
queue.insert(2,"data")
print(queue)


# removing first occurances
queue.remove("data")
print(queue)


# counting number of occurances of the element
print(queue.count("name"))


# extending iterables to the end of the queue
queue.extend([1,2,4,5,5,6])
print(queue)


# extending iterables to the begining of the queue but the order will be reversed
queue.extendleft([1,2,4,5,5,6])
# deque([6, 5, 5, 4, 2, 1, 'name', 'age', 'DOB', 1, 2, 4, 5, 5, 6])
# means the last element of the iterable will be the first element
print(queue)

# reversing the order
queue.extend("arnaB")
print(queue)
queue.reverse()
print(queue)


# rotating the array
queue.rotate(2)
print(queue)