def print_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            print(" ", end="")
        for k in range(1, 2 * i):
            print("*", end="")
        print()

n = 5  # You can change this value to adjust the number of rows
print_pyramid(n)
