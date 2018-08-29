import cs50

while True:
    n = cs50.get_int("Height: ")
    if n >= 0 and n <= 23:
        break

# loop for lines
for i in range(n):
    # print s spaces
    s = n - 1 - i
    for j in range(s):
        print(" ", end="")

    # print h hashes
    h = n - s
    for k in range(h):
        print("#", end="")

    # print two spaces
    print("  ", end="")

    # print h hashes
    for l in range(h):
        print("#", end="")

    # new line
    print()