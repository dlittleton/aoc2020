import sys

def count(stream):
    unique = set()

    for line in map(str.strip, stream):
        if not line:
            yield len(unique)
            unique.clear()
        else:
            unique.update(line)

    yield len(unique)


print(sum(count(sys.stdin)))
