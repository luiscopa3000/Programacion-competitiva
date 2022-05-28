a, b, c, d = map(float, input().split())
y = ((b + d) * (b + d) + c * c) ** 0.5
x = (y * y - a * a) ** 0.5
print("{0:.2f}".format(x))