from dataclasses import dataclass

@dataclass
class Frame:
    index: int
    offset: int
    length: int
    payload: bytes

    @property
    def strings(self):
        return []
