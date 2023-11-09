a = "Hello World"
b = 20
c = ["apple", "oranges", "banana"]
d = (1, 2, 3)
e = {1: "Object", 2: "Oriented", 3: "Programming", 4: "sucks"}

print(id(a))
a = "Goodbye"
a[1] = '3'
print(id(a))

b[0] = 40
b = 'a'

c[3] = "pineapple"
c[1] = "strawberry"

d[0] = 4

e[4] = "rocks!"
e[0] = "Wow!"

f = ([1, 2, 4], "four", "five")
f[0] = 3
f[0][2] = 3

print("{}\n{}\n{}\n{}\n{}\n{}\n".format(a, b, c, d, e, f))
print("\n---code fixed!---\n")
