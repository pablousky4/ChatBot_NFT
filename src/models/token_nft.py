from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class TokenNFT:
    token_id: str
    owner: str
    poll_id: str
    option: str
    issued_at: datetime

    @staticmethod
    def crear(owner, poll_id, option):
        return TokenNFT(
            token_id=str(uuid4()),
            owner=owner,
            poll_id=poll_id,
            option=option,
            issued_at=datetime.now()
        )
