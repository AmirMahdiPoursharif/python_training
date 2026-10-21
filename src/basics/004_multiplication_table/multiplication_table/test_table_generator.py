from multiplication_table.table_generator import multiplication_table


def test_default_table_size():
    table = multiplication_table()

    assert len(table) == 10
    assert all(len(row) == 10 for row in table)


def test_custom_table_size():
    table = multiplication_table(3)

    assert table == [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9],
    ]


def test_table_values():
    table = multiplication_table(5)

    assert table[0][0] == 1
    assert table[1][2] == 6
    assert table[4][4] == 25


def test_table_is_square():
    table = multiplication_table(7)

    assert len(table) == 7
    assert all(len(row) == len(table) for row in table)
