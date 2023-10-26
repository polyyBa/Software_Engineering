def average(*args):
    if len(args) == 0:
        return None
    else:
        return sum(args) / len(args)

if __name__ == "__main__":
    print(average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(average(0))
    print(average())