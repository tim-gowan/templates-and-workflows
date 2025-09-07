# src/good_code.py


def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts the second number from the first."""
    return a - b


def get_greeting(name: str) -> str:
    """Returns a simple greeting string."""
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"
