import pytest
from bot.models import Position, PositionDuplicated, PositionOccupied, PositionUnavailable, Team


def test_team_join():
    team = Team()
    team.join(Position.CBR, 'John', Position.NOBAL)

    assert team.squad[Position.CBR] == ('John', Position.NOBAL)


def test_team_join_occupied_position():
    team = Team()
    team.join(Position.CBR, 'John', None)

    with pytest.raises(PositionOccupied):
        team.join(Position.CBR, 'Ron', None)


def test_team_join_unavailable_position():
    team = Team()

    with pytest.raises(PositionUnavailable):
        team.join(Position.NOBAL, 'John', None)


def test_team_join_different_position_after_already_joined():
    team = Team()
    team.join(Position.CBR, 'John', None)

    with pytest.raises(PositionDuplicated):
        team.join(Position.CF, 'John', None)


def test_team_join_same_position_to_update_hint():
    team = Team()
    team.join(Position.DMF, 'John', None)
    team.join(Position.DMF, 'John', Position.CMF)

    assert team.squad[Position.DMF] == ('John', Position.CMF)


def test_team_leave():
    team = Team()
    team.join(Position.CF, 'Ivan', None)
    team.leave('Ivan')

    assert team.squad[Position.CF] is None


def test_team_leave_without_assignment():
    team = Team()
    team.leave('Ivan')

    assert team.squad.items() == Team().squad.items()
