def add(a, b):
    c = (ord(a) + ord(b) - 130) % 26
    return chr(c + 65)

def diff(a, b):
    c = ord(a) - ord(b)
    if c < 0:
        c = c + 26
    return chr(c + 65)
