a = [65, 23, 34, 50]
b = [60, 10, 720, 890]

print("Append Function:\n")
a.append(90)
print(a)

print("Extend Function:\n")
a.extend(b)
print(a)

print("Copy Function:\n")
a = b.copy()
print(a)

print("Sort Function:\n")
b.sort()
print(b)
a.sort(reverse=True)
print(a)

print("Insert Function:\n")
a.insert(2, 100)
print(a)

print("Remove Function:\n")
a.remove(890)
print(a)

print("Index Function:\n")
x=a.index(60)
print("Index is:",x)

print("Slicing:\n")
f=a[0:-1:2]
print(f)

print("Clear Function:\n")
b.clear()
print(b) 
