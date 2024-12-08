with open(file="./data.txt") as file:
    col1, col2 = [], []
    for line in file:
        lines: str = line.rstrip()
        col1.append(lines.split()[0])
        col2.append(lines.split()[1])
    col1: list[str] = sorted(col1)
    col2: list[str] = sorted(col2)
    a: list[int] = list(map(lambda x, y: abs(int(x) - int(y)), col1, col2))
    print(sum(a))
