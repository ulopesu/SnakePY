from enum import IntEnum, auto


class Diretion(IntEnum):
    RIGHT = auto()
    LEFT = auto()
    UP = auto()
    DONW = auto()

    def is_contrary(self, dir_2: IntEnum):
        if (
            (self.value == self.RIGHT.value and dir_2.value == self.LEFT.value)
            or (dir_2.value == self.RIGHT.value and self.value == self.LEFT.value)
            or (self.value == self.UP.value and dir_2.value == self.DONW.value)
            or (dir_2.value == self.UP.value and self.value == self.DONW.value)
        ):
            return True
        return False

    def is_acceptable(self, dir_prev: IntEnum):
        if self.value != dir_prev.value and not self.is_contrary(dir_prev):
            return True
        return False
