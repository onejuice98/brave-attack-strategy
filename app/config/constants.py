from enum import Enum


class ActionType(str, Enum):
    MOVE = "move"
    ATTACK = "attack"
    DEFEND = "defend"
    WAIT = "wait"
