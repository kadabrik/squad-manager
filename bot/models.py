from enum import Enum, auto
from typing import List, Tuple, Dict, Optional


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
        self._formation = [
            Position.GK,
            Position.LB,
            Position.RB,
            Position.CBR,
            Position.CBL,
            Position.DMF,
            Position.CMF,
            Position.AMF,
            Position.LWF,
            Position.RWF,
            Position.CF,
        ]

        self._squad: Dict[Position, Optional[Tuple[str, Position]]] = {}
        self.reset()

    def _get_registered_position(self, name: str) -> Optional[Position]:
        occupied_positions = {(k, v) for k, v in self._squad.items() if v is not None}
        for k, (v, _) in occupied_positions:
            if v == name:
                return k
        return None

    def join(self, position: Position, name: str, hint: Position = None) -> None:
        """Assign a player to a specific position"""
        if position not in self._squad:
            raise PositionUnavailable

        registered_position = self._get_registered_position(name)

        if position != registered_position:
            if self._squad[position] is not None:
                raise PositionOccupied
            if registered_position is not None:
                raise PositionDuplicated

        self._squad[position] = (name, hint)

    def leave(self, name) -> None:
        """Leave position where player previously registered"""
        registered_position = self._get_registered_position(name)
        if registered_position is not None:
            self._squad[registered_position] = None

    def clear(self, position: Position) -> None:
        """Remove a player from desired position"""
        self._squad[position] = None

    def reset(self) -> None:
        """Clear all positions configured for the team"""
        self._squad = {i: None for i in self._formation}

    def configure(self, positions: List[Position]) -> None:
        """Configure positions available in the team"""
        pass


class PositionOccupied(Exception):
    pass


class PositionUnavailable(Exception):
    pass


class PositionDuplicated(Exception):
    pass
