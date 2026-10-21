def multiplication_table(size : int = 10):
    table = []

    for i in range(1, size + 1):
        row = []

        for j in range(1, size + 1):
            row.append(i * j)

        table.append(row)

    return table
