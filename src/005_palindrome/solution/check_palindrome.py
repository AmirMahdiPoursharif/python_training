def check(string: str):
    sample = ""

    for i in range(len(string) -1, -1, -1):
        sample += string[i]

    if sample == string:
        return sample, True
    else:
        return sample, False