from math import sqrt, ceil, cos, sin

W, H = 800, 800


def setup():
    size(W, H)
    background(255)
    noLoop()


def draw():
    r, th = 0, 0
    for _, p in enumerate(sieve(5000)):
        x, y = polarToCartesian(r, th)
        point(x, y)
        stroke(255, 0, 0) if p else stroke(0)
        r += 0.1
        th += 0.1


def sieve(n):
    N = [True] * (n + 1)
    N[0] = N[1] = False
    for i in range(2, int(ceil(sqrt(len(N))))):
        if N[i]:
            for j in range(i ** 2, len(N), i):
                N[j] = False
    return N


def polarToCartesian(th, r):
    return [
        -(r * cos(th)) + W / 2,
        -(r * sin(th)) + H / 2
    ]
