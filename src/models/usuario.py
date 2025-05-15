from dataclasses import dataclass, field
from typing import List


@dataclass
class Usuario:
    username: str
    password_hash: str
    tokens: List[str] = field(default_factory=list)
