def select_winner(a : int, b : int):
    if a == b:
        return None
    else:
        if 2 in (a, b):
            return max(a, b)
        else:
            return min(a, b)