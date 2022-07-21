from enum import Enum


class Chart(str, Enum):
    bar = "bar"
    line = "line"
    pie = "pie"