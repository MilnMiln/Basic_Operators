#! /usr/bin/python3

a, b, c = 3, 5, 13
print("Integer operations:")
print(a, "+", b, "=", a+b)
print(b, "*", c, "=", b*c)
print(c, "-", a, "=", c-a)
print(c, "%", b, "=", c%b)
print(b, "**", a, "=", b**a)

hello = "hello"
world = "world"
print ("\nString operations:")
print(hello, "world")
print(hello, world)
print(hello, '+ " " +', world, "=", hello + " " + world)
print(hello, "* 5 =", hello * 5)
print("(",hello, ' + " ") * 5 =', (hello + " ") * 5)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
print("\nList Operations:")
print(odd_numbers, "+", even_numbers, "=", odd_numbers + even_numbers)
print(odd_numbers, "* 3 =", odd_numbers*3)

print("\nExercises:")
x = object()
y = object()

x_list = 10 * [x]
y_list = 10 * [y]
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

