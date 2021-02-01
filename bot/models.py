from enum import Enum, auto
from typing import List, Tuple, Dict

class AutoNameEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class Position(AutoNameEnum):
    GK = auto(),
    RB = auto(),
    CBR = auto(),
    CBL = auto(),
    LB = auto(),
    DMF = auto(),
    CMF = auto(),
    AMF = auto(),
    RMF = auto(),
    LMF = auto(),
    RWF = auto(),
    LWF = auto(),
    SS = auto(),
    CF = auto(),
    NOBAL = auto(),


class Team:

    def __init__(self) -> None:
        self.positions: Dict[Position, Tuple[str, Position]] = {
            Position.GK: None,
            Position.LB: None,
            Position.RB: None,
            Position.CBR: None,
            Position.CBL: None,
            Position.DMF: None,
            Position.CMF: None,
            Position.AMF: None,
            Position.LWF: None,
            Position.RWF: None,
            Position.CF: None,
        }

    def join(self, position: Position, name: str, hint: Position = None) -> None:
        '''Assign a player to a specific position'''
        if position not in self.positions:
            raise PositionUnavailable

        occupiedPositions = set([v for v in self.positions.values() if v is not None])
        registeredPosition = set([k for k, _ in occupiedPositions if k == name])
        if registeredPosition:
            raise PositionDuplicated

        if self.positions[position] is not None:
            raise PositionOccupied

        self.positions[position] = (name, hint)

    def leave(self, name) -> None:
        '''Leave position where player previosely registered'''
        pass

    def clear(self, position: Position) -> None:
        '''Remove a player from desired position'''
        pass

    def reset(self) -> None:
        '''Clear all positions configured for the team'''
        pass

    def configure(self, positions: List[Position]) -> None:
        '''Configure positions available in the team'''
        pass

class PositionOccupied(Exception):
    pass

class PositionUnavailable(Exception):
    pass

class PositionDuplicated(Exception):
    pass