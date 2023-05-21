def abs_func(a, b, c):
    d1 = abs(a - b)
    d2 = abs(b - c)
    d3 = abs(a - c)
    return min(d1, d2, d3)


print(
    abs_func(1, 10, 100),
    abs_func(1, 10, 10),
    abs_func(5, 6, 7),  # Python allows trailing commas in argument lists. How nice is that?
)
