import string
import sys

def count(stream):
    unique = set(string.ascii_lowercase)

    for line in map(str.strip, stream):
        if not line:
            yield len(unique)
            unique = set(string.ascii_lowercase)
        else:
            unique.intersection_update(line)

    yield len(unique)


print(sum(count(sys.stdin)))
