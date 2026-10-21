def to_celsius(temperature : int) -> float | int:
    return (temperature - 32) * 5/9

def to_fahrenheit(temperature : int) -> float | int:
    return (9/5 * temperature) + 32