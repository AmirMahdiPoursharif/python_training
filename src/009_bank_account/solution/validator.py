def validate_balance(balance: str) -> bool:
    try:
        return float(balance) > 0
    except ValueError:
        return False

def validate_name(name: str) -> bool:
    return len(name.strip()) > 3


def validate_password(password: str) -> bool:
    return len(password.strip()) > 6