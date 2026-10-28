def words_counter(path : str) -> tuple[list[str], int]:
    with open(path, mode="r", encoding="utf-8") as file:
        # words list
        wl : list[str] = []
        for line in file:
            word = line.split()
            wl += word

        return wl, len(wl)

def line_counter(path : str) -> int:
    with open(path, mode="r", encoding="utf-8") as file:
        counter = 0

        for line in file:
            if line.strip():
                counter += 1

        # شکل تک خطی بلاک بالا
        # counter += sum(1 for line in file if line.strip())

        return counter

def character_counter(path : str) -> int:
    with open(path, mode="r", encoding="utf-8") as file:
        return sum(len(line) for line in file)
