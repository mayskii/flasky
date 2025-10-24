# class Cat:
#     def __init__(self, id, name, color, personality):
#         self.id = id
#         self.name = name
#         self.color = color
#         self.personality = personality

# cats = [
#     Cat(1, "Luna", "gray", "naughty"),
#     Cat(2, "Morty", "orange","happy"),
#     Cat(3, "Mimi", "gray", "chill"),
#     Cat(4, "Binx", "black", "hungry")
# ]

from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Cat(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    color: Mapped[str]
    personality: Mapped[str]

