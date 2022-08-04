"""Hello world"""


def hello(name: str | None = None) -> str:
    return f"Hello, {name or 'world'}!"
