from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    status: str = "в наличии"
