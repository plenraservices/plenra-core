from collections.abc import MutableMapping


class InMemoryIdempotencyStore:
    def __init__(self) -> None:
        self._store: MutableMapping[str, dict] = {}

    def has(self, key: str) -> bool:
        return key in self._store

    def get(self, key: str) -> dict | None:
        return self._store.get(key)

    def set(self, key: str, value: dict) -> None:
        self._store[key] = value
