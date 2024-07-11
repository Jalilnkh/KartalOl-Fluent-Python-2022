from datetime import datetime
from enum import Enum
from typing import Set

FOLLOWERS_MULTIPLIER: int = 2
HACKTOBER_MONTH: int = 10
HACKTOBER_BONUS: int = 10
LANGUAGE_MULTIPLIER: int = 2


class Language(Enum):
    C = 1
    JAVA = 2
    PYTHON = 3
    SCALA = 4


class Developer:
    def __init__(
        self,
        accepted_contributions: int,
        followers: int,
        languages: Set[Language]
    ):
        self.accepted_contributions = accepted_contributions
        self.followers = followers
        self.languages = languages


def calculate(dev: Developer) -> int:
    followers_score = dev.followers * FOLLOWERS_MULTIPLIER
    language_score = (LANGUAGE_MULTIPLIER * len(dev.languages)) ** (int(Language.PYTHON in dev.languages) + 1)
    now = datetime.now()
    during_hacktober = bool(now.month == HACKTOBER_MONTH)
    if during_hacktober:
        return followers_score + language_score + HACKTOBER_BONUS
    return followers_score + language_score
