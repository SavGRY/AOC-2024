with open(file="./data.txt") as file:
    col1, col2 = [], []
    for line in file:
        lines: str = line.rstrip()
        col1.append(lines.split()[0])
        col2.append(lines.split()[1])
    col1: list[str] = sorted(col1)
    col2: list[str] = sorted(col2)
    result: int = 0
    for item in col1:
        # multiplying the item for the number of its occurrence
        # and then adding it to result variable
        result: int = result + (int(item) * col2.count(item))
    print(result)
