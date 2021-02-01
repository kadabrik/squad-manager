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
        self.squad: Dict[Position, Optional[Tuple[str, Position]]] = {
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

    def _get_registered_position(self, name: str) -> Optional[Position]:
        occupied_positions = {(k, v) for k, v in self.squad.items() if v is not None}
        for k, (v, _) in occupied_positions:
            if v == name:
                return k
        return None

    def join(self, position: Position, name: str, hint: Position = None) -> None:
        """Assign a player to a specific position"""
        if position not in self.squad:
            raise PositionUnavailable

        registered_position = self._get_registered_position(name)

        if position != registered_position:
            if self.squad[position] is not None:
                raise PositionOccupied
            if registered_position is not None:
                raise PositionDuplicated

        self.squad[position] = (name, hint)

    def leave(self, name) -> None:
        """Leave position where player previously registered"""
        registered_position = self._get_registered_position(name)
        if registered_position is not None:
            self.squad[registered_position] = None

    def clear(self, position: Position) -> None:
        """Remove a player from desired position"""
        pass

    def reset(self) -> None:
        """Clear all positions configured for the team"""
        pass

    def configure(self, positions: List[Position]) -> None:
        """Configure positions available in the team"""
        pass


class PositionOccupied(Exception):
    pass


class PositionUnavailable(Exception):
    pass


class PositionDuplicated(Exception):
    pass
